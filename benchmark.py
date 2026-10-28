
import argparse
import csv
import time
from pathlib import Path

import cv2
import numpy as np
from ultralytics import YOLO


def benchmark_video(source, model_path, max_frames):
    model = YOLO(model_path)

    if source.isdigit():
        source = int(source)

    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        raise RuntimeError("Unable to open video source")

    times = []
    frame_count = 0

    try:
        while frame_count < max_frames:
            success, frame = cap.read()

            if not success:
                break

            start = time.perf_counter()

            model.track(
                frame,
                persist=True,
                tracker="bytetrack.yaml",
                verbose=False,
                conf=0.25,
            )

            elapsed = time.perf_counter() - start

            times.append(elapsed * 1000)
            frame_count += 1

    finally:
        cap.release()

    if not times:
        raise RuntimeError("No frames processed")

    duration = sum(times) / 1000
    fps = frame_count / duration

    results = {
        "frames": frame_count,
        "fps": round(fps, 2),
        "mean_latency_ms": round(float(np.mean(times)), 2),
        "median_latency_ms": round(float(np.median(times)), 2),
        "p95_latency_ms": round(float(np.percentile(times, 95)), 2),
        "p99_latency_ms": round(float(np.percentile(times, 99)), 2),
    }

    Path("reports").mkdir(exist_ok=True)

    with open("reports/benchmark.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=results.keys()
        )
        writer.writeheader()
        writer.writerow(results)

    print("\n===== VIDEO TRACKING BENCHMARK =====")

    for key, value in results.items():
        print(f"{key}: {value}")

    print("\nSaved to reports/benchmark.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--source", default="0")
    parser.add_argument("--model", default="yolo11n.pt")
    parser.add_argument("--frames", type=int, default=300)

    args = parser.parse_args()

    benchmark_video(
        args.source,
        args.model,
        args.frames,
    )

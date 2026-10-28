
import argparse
import time
from pathlib import Path

import cv2
from ultralytics import YOLO


def run_tracking(source, output, model_name):
    # Load YOLO11 object detection model
    model = YOLO(model_name)

    # Convert webcam source from string to integer
    if str(source).isdigit():
        source = int(source)

    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        raise RuntimeError(f"Cannot open video source: {source}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_fps = cap.get(cv2.CAP_PROP_FPS)

    if video_fps <= 0:
        video_fps = 30.0

    Path(output).parent.mkdir(parents=True, exist_ok=True)

    writer = cv2.VideoWriter(
        output,
        cv2.VideoWriter_fourcc(*"mp4v"),
        video_fps,
        (width, height)
    )

    if not writer.isOpened():
        cap.release()
        raise RuntimeError("Cannot create output video")

    total_frames = 0
    processing_times = []

    try:
        while True:
            success, frame = cap.read()

            if not success:
                break

            start_time = time.perf_counter()

            # YOLO detection with ByteTrack tracking
            results = model.track(
                frame,
                persist=True,
                tracker="bytetrack.yaml",
                conf=0.25,
                verbose=False
            )

            annotated = results[0].plot()

            elapsed = time.perf_counter() - start_time
            processing_times.append(elapsed)
            total_frames += 1

            current_fps = 1 / elapsed if elapsed > 0 else 0

            cv2.putText(
                annotated,
                f"FPS: {current_fps:.1f}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            writer.write(annotated)

            cv2.imshow(
                "Real-Time Object Detection and Tracking",
                annotated
            )

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        cap.release()
        writer.release()
        cv2.destroyAllWindows()

    if processing_times:
        average_latency = (
            sum(processing_times) / len(processing_times)
        ) * 1000

        average_fps = (
            len(processing_times) / sum(processing_times)
        )

        print("\n===== PERFORMANCE RESULTS =====")
        print(f"Processed Frames: {total_frames}")
        print(f"Average Processing FPS: {average_fps:.2f}")
        print(f"Average Processing Latency: {average_latency:.2f} ms")
        print(f"Output Video: {output}")
        print("===============================")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--source",
        default="0",
        help="Webcam index or input video path"
    )

    parser.add_argument(
        "--output",
        default="outputs/tracked_video.mp4"
    )

    parser.add_argument(
        "--model",
        default="yolo11n.pt"
    )

    args = parser.parse_args()

    run_tracking(
        args.source,
        args.output,
        args.model
    )

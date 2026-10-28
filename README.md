

# Real-Time Object Detection and Multi-Object Tracking



A Python-based real-time video analytics system using \*\*YOLO11, ByteTrack, and OpenCV\*\* to detect objects, maintain tracking identities across frames, generate annotated videos, and evaluate detection accuracy and processing performance.



\## Project Overview



This project implements a real-time object detection and multi-object tracking pipeline for webcam streams and recorded videos.



The system uses the pretrained YOLO11n object detection model to identify objects and ByteTrack to associate detections across consecutive frames.



OpenCV handles video acquisition, frame processing, visualization, and output video generation.



The project also includes benchmarking tools to measure FPS, average processing latency, and latency percentiles.



Detection performance was evaluated on the COCO128 dataset using mAP@50 and mAP@50–95.



\## Key Features



\- Real-time object detection using YOLO11n

\- Multi-object tracking using ByteTrack

\- Webcam and recorded-video support

\- Bounding boxes and object class labels

\- Persistent tracking IDs across frames

\- Confidence-based object detection

\- Live FPS display

\- Annotated MP4 output

\- Average processing FPS measurement

\- Mean, median, P95, and P99 latency benchmarking

\- CSV benchmark report generation

\- COCO128 detection accuracy evaluation



\## Technology Stack



| Technology | Purpose |

|---|---|

| Python | Core implementation |

| Ultralytics YOLO11 | Object detection |

| ByteTrack | Multi-object tracking |

| OpenCV | Video capture and processing |

| NumPy | Numerical analysis |

| Git and GitHub | Version control |



\## System Architecture



The application follows this workflow:



1\. Capture a frame from a webcam or video file.

2\. Pass the frame to the pretrained YOLO11 detector.

3\. Obtain bounding boxes, class labels, and confidence scores.

4\. Associate detections across frames using ByteTrack.

5\. Assign tracking IDs to detected objects.

6\. Annotate frames with detection and tracking information.

7\. Display the processed video and write an MP4 file.

8\. Record processing time and calculate performance metrics.



\## Experimental Results



\### Real-Time Webcam Performance



The initial webcam processing experiment produced the following results:



| Metric | Result |

|---|---:|

| Processed Frames | 1,086 |

| Average Processing FPS | 30.82 |

| Average Processing Latency | 32.45 ms |



These values measure YOLO tracking and frame annotation processing. They do not represent complete camera-to-display latency.



\### Detection Accuracy: COCO128



The pretrained YOLO11n model was evaluated on the COCO128 dataset.



| Metric | Result |

|---|---:|

| Validation Images | 128 |

| Ground-Truth Instances | 929 |

| Precision | 66.3% |

| Recall | 58.9% |

| mAP@50 | \*\*67.1%\*\* |

| mAP@50–95 | \*\*50.3%\*\* |

| CPU Inference Time | 30.8 ms/image |



\### Evaluation Environment



\- Model: YOLO11n pretrained weights

\- Dataset: COCO128

\- Input image size: 640

\- Device: CPU

\- Processor: Intel Core i7-13650HX

\- Python: 3.11.9

\- Ultralytics: 8.4.191



The mAP values measure object detection accuracy, not multi-object tracking accuracy.



\## Repository Structure



```text

Real-Time-Object-Detection-and-Tracking/

├── README.md

├── main.py

├── benchmark.py

├── requirements.txt

├── .gitignore

└── reports/

&#x20;   └── benchmark.csv

```



\### File Descriptions



\*\*main.py\*\*



Implements webcam/video processing, YOLO11 object detection, ByteTrack integration, annotated video export, and FPS/latency reporting.



\*\*benchmark.py\*\*



Evaluates processing performance across multiple frames and exports a CSV report containing FPS and latency statistics.



\*\*requirements.txt\*\*



Contains the Python package dependencies.



\*\*reports/benchmark.csv\*\*



Stores the measured video processing benchmark results.



\## Installation



\### 1. Clone the Repository



```bash

git clone https://github.com/DGSKOUSHIK/Real-Time-Object-Detection-and-Tracking.git

cd Real-Time-Object-Detection-and-Tracking

```



\### 2. Create a Virtual Environment



Windows:



```cmd

python -m venv .venv

.venv\\Scripts\\activate

```



\### 3. Install Dependencies



```bash

python -m pip install -r requirements.txt

```



On the first execution, Ultralytics may download the pretrained YOLO11n weights.



\## Running the Application



\### Webcam Detection and Tracking



```bash

python main.py --source 0

```



\### Recorded Video Detection and Tracking



```bash

python main.py --source test.mp4

```



\### Custom Output Video



```bash

python main.py --source test.mp4 --output outputs/result.mp4

```



\### Custom Model



```bash

python main.py --source 0 --model yolo11n.pt

```



Press \*\*Q\*\* in the video window to stop processing.



By default, annotated results are saved to:



```text

outputs/tracked\_video.mp4

```



\## Performance Benchmarking



The repository includes a benchmark script for measuring processing speed and latency.



Run a 300-frame webcam benchmark:



```bash

python benchmark.py --source 0 --frames 300

```



Run a benchmark using a recorded video:



```bash

python benchmark.py --source test.mp4 --frames 300

```



The benchmark calculates:



\- Total frames processed

\- Processing FPS

\- Mean latency

\- Median latency

\- P95 latency

\- P99 latency



Benchmark measurements cover the tracking operation and exclude video capture, display, and output-video writing.



The results are exported to:



```text

reports/benchmark.csv

```



\## Detection Accuracy Evaluation



To reproduce the COCO128 evaluation, run:



```bash

yolo detect val model=yolo11n.pt data=coco128.yaml imgsz=640 device=cpu

```



The validation command reports precision, recall, mAP@50, and mAP@50–95.



Results are stored in a local Ultralytics validation output directory.



\## Limitations



\- Processing speed depends on the available hardware.

\- The current implementation uses pretrained YOLO11n weights.

\- Detection accuracy results are from COCO128 and should not be interpreted as accuracy on arbitrary webcam footage.

\- Tracking quality has not yet been evaluated using IDF1, HOTA, or MOTA.

\- The reported processing FPS excludes some end-to-end system overhead.

\- Extended testing on challenging recorded-video sequences remains necessary.



\## Future Improvements



Planned enhancements include:



\- Tracking accuracy evaluation using labeled video datasets

\- Object counting and line-crossing analytics

\- Multi-camera video processing

\- Streamlit dashboard

\- FastAPI integration

\- Detailed per-frame performance logging

\- Additional automated tests

\- Hardware-specific model optimization

\- ONNX Runtime inference benchmarking



\## Project Status



The initial detection, tracking, video output, and performance benchmarking components have been implemented.



The application has completed an initial webcam processing test and pretrained detector validation on COCO128.



Additional tracking-quality evaluation and broader video testing remain future work.



\## Developer



\*\*Koushik Daggupati\*\*



GitHub: https://github.com/DGSKOUSHIK



Repository: https://github.com/DGSKOUSHIK/Real-Time-Object-Detection-and-Tracking




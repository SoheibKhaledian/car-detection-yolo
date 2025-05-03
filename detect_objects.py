import subprocess
import sys

def detect_objects():
    print("[STATUS]fining the test images")
    subprocess.run([sys.executable, "yolov5/detect.py",
                    "--weights", "yolov5/runs/train/exp/weights/best.pt",
                    "--source", "data/test/images",
                    "--save-txt",
                    "--save-conf",
                    "--project", "output"])
    print("[INFO]object detection is done check the output file")

if __name__ == "__main__":
    detect_objects()

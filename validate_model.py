import subprocess
import sys

def validate_model():
    print("[STATUS]doing validation on model...")
    subprocess.run([
    sys.executable, "yolov5/val.py",
    "--data", "data/data.yaml",
    "--weights", "yolov5/runs/train/exp/weights/best.pt"
    ])
    print("[INFO]validation is done")

if __name__ == "__main__":
    validate_model()

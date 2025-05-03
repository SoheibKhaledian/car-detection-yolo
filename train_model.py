import subprocess
import sys

def train_model():
    print("[STATUS]training")
    subprocess.run([sys.executable, "yolov5/train.py",
                    "--img", "640",
                    "--batch", "16",
                    "--epochs", "2",
                    "--data", "data/data.yaml",
                    "--cfg", "yolov5/models/yolov5s.yaml",
                    "--weights", "yolov5s.pt"])
    print("[INFO]training is done")

if __name__ == "__main__":
    train_model()

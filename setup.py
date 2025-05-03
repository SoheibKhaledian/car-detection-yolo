import os
import subprocess

def setup_environment():
    print("[STATUS]making a clone of Yolo-v5 REPOSITORY")
    if not os.path.exists("yolov5"):
        subprocess.run(["git", "clone", "https://github.com/ultralytics/yolov5.git"])
    
    print("[STATUS]downloading the packages")
    subprocess.run(["pip", "install", "-qr", "yolov5/requirements.txt"])
    subprocess.run(["pip", "install", "gdown"])
    subprocess.run(["pip", "install", "numpy"])


if __name__ == "__main__":
    setup_environment()
    print("[INFO] the environment is ready")

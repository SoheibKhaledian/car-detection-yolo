import gdown
import zipfile

DATA_URL = "https://drive.google.com/file/d/13v2bxm4T3Rp0_iPIa8u_dnWaOQJbXD4P/view?usp=sharing"
OUTPUT_PATH = "data.zip"

def download_and_extract_data():
    print("[STATUS]Downloading the data...")
    gdown.download(DATA_URL, OUTPUT_PATH, quiet=False, fuzzy=True)

    print("[INFO]unzipping the data...")
    with zipfile.ZipFile(OUTPUT_PATH, "r") as zip_ref:
        zip_ref.extractall("data")

    print("[STATUS]Data extraction is complete!")

if __name__ == "__main__":
    download_and_extract_data()

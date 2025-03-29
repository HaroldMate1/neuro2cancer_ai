import requests
from pathlib import Path

DATA_URL = (
    "https://go.drugbank.com/releases/latest/downloads/all-drugbank-vocabulary.csv.zip"
)
DATA_DIR = Path("data/raw/")


def download_drugbank():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    response = requests.get(DATA_URL)
    with open(DATA_DIR / "drugbank.zip", "wb") as f:
        f.write(response.content)
    print("DrugBank dataset downloaded.")


if __name__ == "__main__":
    download_drugbank()

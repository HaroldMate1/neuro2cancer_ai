import pandas as pd
import zipfile
import os
from pathlib import Path

RAW_ZIP_PATH = Path("C:\Users\ASUS\OneDrive\Escritorio\Repositories\neuro2cancer_ai\data\raw\drugbank.zip")
EXTRACTED_CSV_PATH = Path("data/raw/all-drugbank-vocabulary.csv")
PROCESSED_PATH = Path("data/processed/cleaned_drug_data.csv")

NEURO_KEYWORDS = [
    "antidepressant",
    "antipsychotic",
    "anticonvulsant",
    "dopamine",
    "serotonin",
    "neuroleptic",
    "CNS",
    "GABA",
    "epilepsy",
    "neurodegenerative",
]

CANCER_TARGETS = ["EGFR", "BRAF", "ALK", "HER2", "KRAS", "PIK3CA", "VEGFR", "MDM2"]


def contains_neuro_keyword(description):
    description = str(description).lower()
    return any(kw.lower() in description for kw in NEURO_KEYWORDS)


def mock_smiles_lookup(drug_name):
    return {
        "fluoxetine": "CNCCC(c1ccc(Cl)cc1)c1ccccc1",
        "olanzapine": "CN1CC2=C(C=C(C=C2)Cl)SC3=C1C=CC=C3",
    }.get(drug_name.lower(), None)


def mock_targets(drug_name):
    target_map = {"fluoxetine": ["BRAF"], "olanzapine": ["MDM2", "EGFR"]}
    return target_map.get(drug_name.lower(), [])


def extract_zip():
    print("Extracting CSV from zip file...")
    with zipfile.ZipFile(RAW_ZIP_PATH, "r") as zip_ref:
        zip_ref.extractall("data/raw")
    print("Extraction completed.")


def main():
    if not RAW_ZIP_PATH.exists():
        raise FileNotFoundError(f"ZIP file not found at {RAW_ZIP_PATH}")

    if not EXTRACTED_CSV_PATH.exists():
        extract_zip()

    print("Loading extracted DrugBank data...")
    df = pd.read_csv(EXTRACTED_CSV_PATH)

    print("Filtering neuroscience-related drugs...")
    df = df[df["description"].apply(contains_neuro_keyword)]

    print("Adding SMILES and cancer target annotations...")
    df["smiles"] = df["name"].apply(mock_smiles_lookup)
    df["targets"] = df["name"].apply(mock_targets)
    df = df.dropna(subset=["smiles"])

    df["cancer_related"] = df["targets"].apply(
        lambda t: bool(set(t) & set(CANCER_TARGETS))
    )

    selected_cols = ["drugbank_id", "name", "smiles", "targets", "cancer_related"]
    df_clean = df[selected_cols]

    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(PROCESSED_PATH, index=False)
    print(f"Processed dataset saved to {PROCESSED_PATH}")


if __name__ == "__main__":
    main()

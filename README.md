# Neuro2CancerAI

**Deep Learning-driven Drug Repurposing: Neuroscience Drugs for Cancer Treatment**

---

## Overview

**Neuro2CancerAI** leverages advanced deep learning techniques to identify existing neuroscience drugs suitable for repurposing as potential cancer therapies. Using publicly available biomedical datasets and graph neural networks (GNNs) or transformers, it provides an end-to-end pipeline from data ingestion to inference.

---

## Project Structure

```
neuro2cancer_ai/
├── data/
│   ├── raw/                 # Original downloaded datasets
│   └── processed/           # Processed datasets
│
├── notebooks/               # Exploratory analysis and reporting
│   └── exploratory_analysis.ipynb
│
├── src/
│   ├── config/
│   │   └── config.yaml      # Experiment configurations
│   ├── data/
│   │   ├── download.py      # Data downloading scripts
│   │   ├── preprocess.py    # Data preprocessing pipeline
│   │   └── dataloader.py    # Data loader utilities
│   ├── models/
│   │   ├── gnn_model.py
│   │   └── transformer_model.py
│   ├── training/
│   │   └── trainer.py
│   ├── evaluation/
│   │   └── evaluate.py
│   ├── inference/
│   │   └── inference.py
│   ├── utils/
│   │   ├── logging.py
│   │   └── helpers.py
│   └── visualization/
│       └── plot_results.py
│
├── models/                   # Trained models
├── outputs/                  # Experiment logs and outputs
├── tests/                    # Automated tests
│   └── test_dataloader.py
│
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/neuro2cancer_ai.git
cd neuro2cancer_ai
pip install -r requirements.txt
```

---

## Data Pipeline

### Download and Preprocess DrugBank Data

Download DrugBank dataset:

```bash
python src/data/download.py
```

Preprocess dataset:

```bash
python src/data/preprocess.py
```

The processed dataset will be saved at:

```
data/processed/cleaned_drug_data.csv
```

---

## Model Training

Run model training:

```bash
python src/training/trainer.py
```

This script uses configurations specified in `src/config/config.yaml`.

---

## Inference

Predict repurposing potential for a new molecule:

```bash
python src/inference/inference.py --smiles "<your_smiles_here>" --checkpoint models/best.ckpt
```

Example:

```bash
python src/inference/inference.py --smiles "CNCCC(c1ccc(Cl)cc1)c1ccccc1" --checkpoint models/best.ckpt
```

---

## Exploratory Analysis

Explore data and preliminary results with notebooks:

```bash
jupyter notebook notebooks/exploratory_analysis.ipynb
```

---

## References & Data Sources

* [DrugBank Open Data](https://go.drugbank.com/releases/latest#open-data)
* [PubChem](https://pubchem.ncbi.nlm.nih.gov/)
* [ChEMBL](https://www.ebi.ac.uk/chembl/)

---

## Contributing

Contributions are welcome! Please create a pull request and follow best practices in modularity and code readability.

---

## License

This project is licensed under the MIT License.

---

**Neuro2CancerAI** © 2025

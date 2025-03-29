import torch
import argparse
from src.models.gnn_model import DrugRepurposingGNN
from src.data.dataloader import preprocess_single_smiles


def load_model(checkpoint_path):
    model = DrugRepurposingGNN.load_from_checkpoint(checkpoint_path)
    model.eval()
    return model


def predict(model, smiles):
    data = preprocess_single_smiles(smiles)
    with torch.no_grad():
        pred = model(data)
    return pred.item()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--smiles", type=str, required=True)
    parser.add_argument("--checkpoint", type=str, required=True)
    args = parser.parse_args()

    model = load_model(args.checkpoint)
    prediction = predict(model, args.smiles)
    print(f"Repurposing prediction score: {prediction:.4f}")

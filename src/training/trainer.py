import hydra
from omegaconf import DictConfig
import pytorch_lightning as pl
from src.data.dataloader import DrugDataModule
from src.models.gnn_model import DrugRepurposingGNN
from pytorch_lightning.callbacks import EarlyStopping, ModelCheckpoint


@hydra.main(config_path="../config", config_name="config")
def main(cfg: DictConfig):
    dm = DrugDataModule(cfg)
    model = DrugRepurposingGNN(cfg)

    callbacks = [
        EarlyStopping(monitor="val_loss", patience=5),
        ModelCheckpoint(dirpath="models/", save_top_k=1, monitor="val_loss"),
    ]

    trainer = pl.Trainer(
        max_epochs=cfg.train.epochs,
        callbacks=callbacks,
        accelerator="auto",
    )

    trainer.fit(model, dm)


if __name__ == "__main__":
    main()

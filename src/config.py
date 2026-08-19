import logging
from pathlib import Path

# Diretórios base
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# Parâmetros de Coleta (TSE)
BASE_URL = "https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
YEARS = [2012, 2016, 2020, 2024]
TARGET_UF = "SP"


def setup_logging(level: int = logging.INFO) -> None:
    """Configura o formato padrão de logs para o projeto."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

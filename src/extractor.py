import logging
import zipfile
from pathlib import Path

from src.config import RAW_DIR, TARGET_UF

logger = logging.getLogger(__name__)


def extract_zips(raw_dir: Path = RAW_DIR, uf: str = TARGET_UF) -> None:
    """Extrai apenas o arquivo CSV do estado (UF) selecionado de cada .zip."""
    zip_files = list(raw_dir.glob("*.zip"))
    if not zip_files:
        logger.warning("Nenhum arquivo .zip encontrado em '%s'.", raw_dir)
        return

    uf_suffix = f"_{uf.upper()}.CSV"

    for zip_path in zip_files:
        target_dir = raw_dir / zip_path.stem
        target_dir.mkdir(parents=True, exist_ok=True)

        try:
            with zipfile.ZipFile(zip_path, "r") as zf:
                uf_files = [f for f in zf.namelist() if f.upper().endswith(uf_suffix)]
                if not uf_files:
                    logger.warning(
                        "Nenhum arquivo para a UF '%s' encontrado em '%s'.",
                        uf,
                        zip_path.name,
                    )
                    continue

                for file_name in uf_files:
                    dest_file = target_dir / file_name
                    if dest_file.exists():
                        logger.info(
                            "Arquivo '%s' já extraído em '%s'. Pulando.",
                            file_name,
                            target_dir.name,
                        )
                        continue

                    logger.info("Extraindo '%s' -> '%s/'", file_name, target_dir.name)
                    zf.extract(file_name, target_dir)

            logger.info("Extração de '%s' (UF: %s) finalizada com sucesso.", target_dir.name, uf)
        except zipfile.BadZipFile:
            logger.error("O arquivo '%s' está corrompido ou é inválido.", zip_path.name)
        except Exception as e:
            logger.exception("Erro ao extrair '%s': %s", zip_path.name, e)


if __name__ == "__main__":
    from src.config import setup_logging

    setup_logging()
    extract_zips()

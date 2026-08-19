import logging
from pathlib import Path
import requests

from src.config import BASE_URL, HEADERS, RAW_DIR, YEARS

logger = logging.getLogger(__name__)


def download_tse_cand(
    years: list[int] = YEARS,
    dest_dir: Path = RAW_DIR,
    timeout: int = 60,
) -> None:
    """Baixa os arquivos zip de candidatos do TSE para os anos selecionados."""
    dest_dir.mkdir(parents=True, exist_ok=True)

    with requests.Session() as session:
        for year in years:
            filename = f"consulta_cand_{year}.zip"
            dest_path = dest_dir / filename
            temp_path = dest_dir / f"{filename}.part"

            if dest_path.exists():
                logger.info("Arquivo '%s' já existe em '%s'. Pulando.", filename, dest_dir.name)
                continue

            logger.info("Iniciando download de '%s'...", filename)
            url = f"{BASE_URL}/{filename}"

            try:
                with session.get(url, headers=HEADERS, stream=True, timeout=timeout) as response:
                    response.raise_for_status()
                    with open(temp_path, "wb") as f:
                        for chunk in response.iter_content(chunk_size=1024 * 1024):
                            if chunk:
                                f.write(chunk)

                # Renomeia o arquivo temporário somente após download 100% concluído
                temp_path.rename(dest_path)
                logger.info("Download concluído e salvo com sucesso: '%s'", filename)

            except requests.RequestException as e:
                logger.error("Erro de conexão ao baixar '%s' de %s: %s", filename, url, e)
                if temp_path.exists():
                    temp_path.unlink()  # Remove arquivo parcial corrompido
            except Exception as e:
                logger.exception("Erro inesperado ao processar '%s': %s", filename, e)
                if temp_path.exists():
                    temp_path.unlink()


if __name__ == "__main__":
    from src.config import setup_logging
    setup_logging()
    download_tse_cand()


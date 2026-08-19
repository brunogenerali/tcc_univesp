from src import downloader, extractor
from src.config import setup_logging


def main() -> None:
    setup_logging()
    downloader.download_tse_cand()
    extractor.extract_zips()


if __name__ == "__main__":
    main()

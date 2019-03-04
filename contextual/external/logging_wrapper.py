import logging
import logging.handlers
from PyQt5.QtWidgets import qApp

from contextual.external.data_file import app_dir


def setup_logging():
    handlers = [
        logging.handlers.RotatingFileHandler(
            app_dir.joinpath(f"{qApp.applicationName().lower()}.log"),
            maxBytes=1000000, backupCount=1
        )
    ]

    logging.basicConfig(
        handlers=handlers,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M',
        level=logging.DEBUG
    )
    logging.captureWarnings(capture=True)

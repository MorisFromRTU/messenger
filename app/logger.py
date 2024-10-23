import logging
import colorlog

def setup_logging():
    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(levelname)s:     %(message)s %(asctime)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logging.basicConfig(level=logging.INFO, handlers=[handler])

setup_logging()

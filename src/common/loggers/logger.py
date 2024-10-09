import sys
from os import getpid
from loguru import logger
from .enums.ansi_colors_enum import ANSIColors


class AppLogger:
    def __init__(self, log_level="DEBUG", label="App"):
        self.logger = logger.bind(label=label)
        self._configure_logger(log_level)

    def _configure_logger(self, log_level):
        logger.remove()
        logger.add(
            sys.stderr,
            format=(
                f"{ANSIColors.YELLOW.value}[FastAPI] {{extra[pid]}} - {ANSIColors.RESET.value}"
                f"{ANSIColors.WHITE.value}{{time:MMM-DD-YY HH:mm:ss}} - {ANSIColors.RESET.value}"
                f"{ANSIColors.YELLOW.value}[{{extra[label]}}] - {ANSIColors.RESET.value}"
                "<level>{level}</level>: <level>{message}</level>"
            ),
            colorize=True,
            level=log_level,
        )
        self.logger = self.logger.bind(pid=getpid())

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def set_level(self, level):
        self._configure_logger(level)

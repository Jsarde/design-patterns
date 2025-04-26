import logging


class Logger:
    def __init__(self, name: str) -> None:
        logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=logging.INFO,
        )

        self.logger = logging.getLogger(name)

    def get_logger(self) -> logging.Logger:
        return self.logger

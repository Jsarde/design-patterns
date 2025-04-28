from src.creational_patterns.factory_method.creator import DocumentCreator
from src.creational_patterns.factory_method.creator import PDFDocumentCreator
from src.creational_patterns.factory_method.creator import TextDocumentCreator
from src.logger import Logger


# ----- Client code -----
def client_code(creator: DocumentCreator, logger: Logger) -> None:
    """
    The client works with creators and products through their abstract interfaces,
    without being aware of the concrete classes.
    """
    logger.info(f"{creator.operation()}")


if __name__ == "__main__":
    logger = Logger("FactoryMethodLogger").get_logger()

    logger.info("App: Launched with the PDFDocumentCreator.")
    client_code(creator=PDFDocumentCreator(), logger=logger)

    logger.info("App: Launched with the TextDocumentCreator.")
    client_code(creator=TextDocumentCreator(), logger=logger)

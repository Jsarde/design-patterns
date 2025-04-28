from abc import ABC
from abc import abstractmethod

from src.creational_patterns.factory_method.product import Document
from src.creational_patterns.factory_method.product import PDFDocument
from src.creational_patterns.factory_method.product import TextDocument


# ----- Creator Interface -----
class DocumentCreator(ABC):
    """
    This abstract class declares the factory method,
    that returns a Document object.
    """

    @abstractmethod
    def factory_method(self) -> Document:
        pass

    def operation(self) -> str:
        # Call the factory method to create a Document object
        document = self.factory_method()

        # Use the document
        result = f"DocumentCreator: {document.create()}"
        return result


# ----- Concrete Creators -----
class PDFDocumentCreator(DocumentCreator):
    """
    This concrete creator class overrides the factory method
    to return a PDFDocument object.
    """

    def factory_method(self) -> Document:
        return PDFDocument()


class TextDocumentCreator(DocumentCreator):
    """
    This concrete creator class overrides the factory method
    to return a TextDocument object.
    """

    def factory_method(self) -> Document:
        return TextDocument()

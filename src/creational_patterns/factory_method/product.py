from abc import ABC
from abc import abstractmethod


# ----- Product Interface -----
class Document(ABC):
    """
    This abstract base class defines the interface for different types of documents.
    """

    @abstractmethod
    def create(self) -> None:
        pass


# ----- Concrete Products -----
class PDFDocument(Document):
    """
    Concrete implementation of a PDF document.
    """

    def create(self) -> str:
        return "Creating a PDF document."


class TextDocument(Document):
    """
    Concrete implementation of a text document.
    """

    def create(self) -> str:
        return "Creating a text document."

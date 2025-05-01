from abc import ABC
from abc import abstractmethod


# ---------- Adaptee ----------
class MetricDistanceCalculator:
    """
    The Adaptee class that works with metric units (meters and kilometers).
    This represents a class with an incompatible interface.
    """

    def get_distance_in_meters(self, point_a: float, point_b: float) -> float:
        """Calculate distance between two points in meters"""
        return abs(point_b - point_a)

    def get_distance_in_kilometers(self, point_a: float, point_b: float) -> float:
        """Calculate distance between two points in kilometers"""
        return self.get_distance_in_meters(point_a, point_b) / 1000

    def display_distance_info(self, point_a: float, point_b: float) -> str:
        """Display distance information in metric units"""
        meters = self.get_distance_in_meters(point_a, point_b)
        kilometers = self.get_distance_in_kilometers(point_a, point_b)
        return f"Distance in metric units: {meters:.2f} meters ({kilometers:.2f} kilometers)"


# ---------- Target interface ----------
class ImperialDistanceCalculator(ABC):
    """
    Target interface that the client expects to work with.
    This defines the methods the client code will use.
    """

    @abstractmethod
    def get_distance_in_feet(self, point_a: float, point_b: float):
        """Calculate distance between two points in feet"""
        pass

    @abstractmethod
    def get_distance_in_miles(self, point_a: float, point_b: float):
        """Calculate distance between two points in miles"""
        pass

    @abstractmethod
    def display_distance_info(self, point_a: float, point_b: float):
        """Display distance information in imperial units"""
        pass

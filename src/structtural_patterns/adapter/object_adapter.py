from src.structtural_patterns.adapter.adapter import ImperialDistanceCalculator
from src.structtural_patterns.adapter.adapter import MetricDistanceCalculator


# ---------- Object Adapter ----------
class ImperialAdapter(ImperialDistanceCalculator):
    """
    The Object Adapter class that makes Adaptee class (MetricDistanceCalculator)
    compatible with the Target interface (ImperialDistanceCalculator).
    """

    # Conversion constants
    METERS_TO_FEET = 3.28084
    KILOMETERS_TO_MILES = 0.621371

    def __init__(self, metric_calculator: MetricDistanceCalculator) -> None:
        """Initialize with the adaptee instance"""
        self.metric_calculator = metric_calculator

    def get_distance_in_feet(self, point_a: float, point_b: float) -> float:
        """Adapt meters to feet"""
        meters = self.metric_calculator.get_distance_in_meters(point_a, point_b)
        return meters * self.METERS_TO_FEET

    def get_distance_in_miles(self, point_a: float, point_b: float) -> float:
        """Adapt kilometers to miles"""
        kilometers = self.metric_calculator.get_distance_in_kilometers(point_a, point_b)
        return kilometers * self.KILOMETERS_TO_MILES

    def display_distance_info(self, point_a: float, point_b: float) -> str:
        """Display distance information in imperial units"""
        feet = self.get_distance_in_feet(point_a, point_b)
        miles = self.get_distance_in_miles(point_a, point_b)
        return f"Distance in imperial units  using the Object Adapter: {feet:.2f} feet ({miles:.2f} miles)"

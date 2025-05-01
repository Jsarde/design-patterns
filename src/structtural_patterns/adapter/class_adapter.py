from src.structtural_patterns.adapter.adapter import ImperialDistanceCalculator
from src.structtural_patterns.adapter.adapter import MetricDistanceCalculator


# ---------- Class Adapter ----------
class MetricToImperialAdapter(MetricDistanceCalculator, ImperialDistanceCalculator):
    """
    The Class Adapterinherits directly from both Adaptee class (MetricDistanceCalculator)
    and the Target interface (ImperialDistanceCalculator).

    Implement the target interface methods using the adaptee's functionality
    """

    # Conversion constants
    METERS_TO_FEET = 3.28084
    KILOMETERS_TO_MILES = 0.621371

    def get_distance_in_feet(self, point_a: float, point_b: float) -> float:
        # Directly use the inherited method from MetricDistanceCalculator
        meters = self.get_distance_in_meters(point_a, point_b)
        return meters * self.METERS_TO_FEET

    def get_distance_in_miles(self, point_a: float, point_b: float) -> float:
        kilometers = self.get_distance_in_kilometers(point_a, point_b)
        return kilometers * self.KILOMETERS_TO_MILES

    def display_distance_info(self, point_a: float, point_b: float) -> str:
        feet = self.get_distance_in_feet(point_a, point_b)
        miles = self.get_distance_in_miles(point_a, point_b)
        return f"Distance in imperial units using the Class Adapter: {feet:.2f} feet ({miles:.2f} miles)"

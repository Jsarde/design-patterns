from src.logger import Logger
from src.structtural_patterns.adapter.adapter import ImperialDistanceCalculator
from src.structtural_patterns.adapter.adapter import MetricDistanceCalculator
from src.structtural_patterns.adapter.class_adapter import MetricToImperialAdapter
from src.structtural_patterns.adapter.object_adapter import ImperialAdapter


# ---------- Client code ----------
def client_code(
    logger: Logger,
    distance_calculator: ImperialDistanceCalculator,
    point_a: float,
    point_b: float,
) -> None:
    """
    Client code that works with the ImperialDistanceCalculator interface.
    This represents code that expects to work with imperial units.
    """
    if isinstance(distance_calculator, ImperialDistanceCalculator):
        logger.info(distance_calculator.display_distance_info(point_a, point_b))
    else:
        logger.error("Error: Expected an ImperialDistanceCalculator")


if __name__ == "__main__":
    logger = Logger("AdapterLogger").get_logger()

    point_a = 120
    point_b = 2571.4

    # ----- Original metric calculator -----
    metric_calculator = MetricDistanceCalculator()
    logger.info(metric_calculator.display_distance_info(point_a, point_b))

    # ----- Object Adapter -----
    object_adapter = ImperialAdapter(metric_calculator)
    client_code(
        logger=logger,
        distance_calculator=object_adapter,
        point_a=point_a,
        point_b=point_b,
    )

    # ----- Class Adapter -----
    class_adapter = MetricToImperialAdapter()
    client_code(
        logger=logger,
        distance_calculator=class_adapter,
        point_a=point_a,
        point_b=point_b,
    )

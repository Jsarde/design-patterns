from src.logger import Logger


class Singleton:
    # Private class-level attribute to store the single instance
    __instance = None

    def __new__(cls, *args, **kwargs) -> "Singleton":
        """
        Dunder method responsible for creating the instance of the class.
        --
        It ensures only one instance of the class is created.
        """
        if not cls.__instance:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, *args, **kwargs) -> None:
        """
        Dunder method responsible for initializing the object's state.
        --
        It ensures that initialization code runs only once.

        Normally, it runs every time an object is instantiated,
        even if the object was already created earlier.
        """
        if not hasattr(self, "_initialized"):
            self._initialized = True


if __name__ == "__main__":
    logger = Logger("SingletonLogger").get_logger()

    s1 = Singleton()
    s2 = Singleton()

    if s1 is s2:
        logger.info("😎 Singleton works, both variables contain the same instance.")
    else:
        logger.error("😭 Singleton failed, variables contain different instances.")

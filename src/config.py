import os


class _Config:
    """Base Config class to hold configuration"""

    ENV = None  # placeholder

    def __init__(self) -> None:
        """Initializer for `Config`"""
        self.LOGGER_LEVEL = os.getenv("logger_level") or os.getenv("LOGGER_LEVEL") or "INFO"


class _DevelopmentConfig(_Config):
    """Development environment configuration"""

    ENV = "development"

    def __init__(self) -> None:
        """Initializer for `DevelopmentConfig`"""
        super().__init__()

        self.LOGGER_LEVEL = "DEBUG"


class _ProductionConfig(_Config):
    """Production environment configuration"""

    ENV = "production"

    def __init__(self) -> None:
        """Initializer for `ProductionConfig`"""
        super().__init__()


_ENV_CONFIG_MAPPING: dict[str, type[_ProductionConfig] | type[_DevelopmentConfig]] = {
    "production": _ProductionConfig,
    "development": _DevelopmentConfig,
}

_curr_env: str = os.getenv("env") or os.getenv("ENV") or "development"

config = _ENV_CONFIG_MAPPING[_curr_env]()

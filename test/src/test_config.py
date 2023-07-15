from src.config import (
    _ENV_CONFIG_MAPPING,
    _Config,
    _DevelopmentConfig,
    _ProductionConfig,
)


class TestConfig:
    def test__config_should_exist(self):
        assert _Config


class TestDevelopmentConfig:
    def test__development_config_should_exist(self):
        assert _DevelopmentConfig


class TestProductionConfigConfig:
    def test__production_config_should_exist(self):
        assert _ProductionConfig


class TestEnvConfigMapping:
    def test__env_config_mapping_should_have_expected_env(self):
        assert _ENV_CONFIG_MAPPING.get("production")
        assert _ENV_CONFIG_MAPPING.get("development")

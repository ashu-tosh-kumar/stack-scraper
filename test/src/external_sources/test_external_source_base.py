from src.external_sources.external_source_base import ExternalSource


class TestExternalSource:
    def test_external_source(self):
        class DummyExternalSource(ExternalSource):
            def run():
                pass

        dummy_external_source = DummyExternalSource()

        assert dummy_external_source

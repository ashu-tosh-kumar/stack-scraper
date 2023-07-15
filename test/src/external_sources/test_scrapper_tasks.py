from unittest.mock import Mock

from src.external_sources.scrapper_tasks import run_all_scrappers


class TestRunAllScrappers:
    def test_run_all_scrappers_should_run_all_scrappers(self):
        spy_scrapper_1 = Mock()
        spy_scrapper_1.__name__ = "mock-scrapper-1"
        spy_scrapper_2 = Mock()
        spy_scrapper_2.__name__ = "mock-scrapper-2"

        run_all_scrappers([spy_scrapper_1, spy_scrapper_2])

        assert spy_scrapper_1.return_value.run.called
        assert spy_scrapper_2.return_value.run.called

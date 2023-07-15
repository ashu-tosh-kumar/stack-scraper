import logging

from src.external_sources.scrappers.stack_overflow import StackOverflow

logger = logging.getLogger(__name__)
ALL_SCRAPPERS = [StackOverflow]


def run_all_scrappers(all_scrappers: list = ALL_SCRAPPERS) -> None:
    """Wrapper to trigger all scrappers

    Args:
        all_scrappers (list, optional): List of scrappers to trigger. Defaults to
        ALL_SCRAPPERS.
    """
    for scrapper in all_scrappers:
        logger.info(f"Triggering scrapper: {scrapper.__name__}")
        try:
            scrapper_instance = scrapper()
            scrapper_instance.run()
            logger.info(f"Scrapper: {scrapper.__name__} ran successfully")
        except Exception:
            logger.exception(f"Error in running scrapper: {scrapper.__name__}")

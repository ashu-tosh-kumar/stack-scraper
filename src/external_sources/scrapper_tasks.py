import logging

from src.external_sources.scrappers.stack_overflow import StackOverflow

logger = logging.getLogger(__name__)
ALL_SCRAPPERS = [StackOverflow]


def run_all_scrappers() -> None:
    """Wrapper to trigger all scrappers"""

    for scrapper in ALL_SCRAPPERS:
        logger.info(f"Triggering scrapper: {scrapper.__name__}")
        try:
            scrapper_instance = scrapper()
            scrapper_instance.run()
            logger.info(f"Scrapper: {scrapper.__name__} ran successfully")
        except Exception:
            logger.exception(f"Error in running scrapper: {scrapper.__name__}")

from abc import ABC, abstractmethod


class ExternalSource(ABC):
    """Base class for all external Scrappers and Apis"""

    @abstractmethod
    def run(self) -> None:
        """Main method that will be called on any `ExternalSource` and should be
        responsible for scraping and ingesting the scraped data into the database
        """
        pass

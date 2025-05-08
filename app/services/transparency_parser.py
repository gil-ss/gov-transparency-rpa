"""Service to extract benefit data from the transparency portal HTML."""

from bs4 import BeautifulSoup
from typing import List
from app.models.benefit import Benefit


class TransparencyParser:
    def parse(self, html: str) -> List[Benefit]:
        """Parse the given HTML and extract benefit data.

        Args:
            html (str): Raw HTML content from the transparency portal.

        Returns:
            List[Benefit]: A list of extracted benefit records.
        """
        soup = BeautifulSoup(html, "html.parser")
        return []

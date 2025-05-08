"""Pydantic model to represent benefit data from the transparency portal."""

from pydantic import BaseModel
from typing import Optional


class Benefit(BaseModel):
    full_name: str
    nis: Optional[str] = None
    cpf: Optional[str] = None
    benefit_type: str
    month: str
    year: int
    amount: float

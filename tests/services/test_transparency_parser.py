"""Unit tests for the TransparencyParser service."""

import pytest
from app.services.transparency_parser import TransparencyParser


@pytest.fixture
def sample_html():
    return """
    <html>
        <body>
            <table>
                <tr>
                    <td>Nome</td><td>CPF</td><td>Benefício</td><td>Mês</td><td>Ano</td><td>Valor</td>
                </tr>
                <tr>
                    <td>Maria Silva</td><td>12345678900</td><td>Bolsa Família</td><td>Março</td><td>2023</td><td>600.00</td>
                </tr>
            </table>
        </body>
    </html>
    """


def test_parser_returns_empty_list(sample_html):
    parser = TransparencyParser()
    result = parser.parse(sample_html)
    assert isinstance(result, list)
    assert len(result) == 0

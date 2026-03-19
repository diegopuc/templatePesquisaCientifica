"""
Configurações centrais do projeto.
"""

from pathlib import Path

RAIZ_PROJETO = Path(__file__).resolve().parents[2]
PASTA_DADOS = RAIZ_PROJETO / "02_dados"
PASTA_RESULTADOS = RAIZ_PROJETO / "07_resultados"

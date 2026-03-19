"""
Pipeline principal do projeto.
"""

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PACOTE_CODIGO = RAIZ / "04_codigo"
if str(PACOTE_CODIGO) not in sys.path:
    sys.path.append(str(PACOTE_CODIGO))

from utilitarios.helpers import registrar_mensagem

def executar_pipeline():
    registrar_mensagem("Início da execução do pipeline.")
    registrar_mensagem("Substituir esta implementação pelo fluxo real do projeto.")
    registrar_mensagem("Fim da execução do pipeline.")

if __name__ == "__main__":
    executar_pipeline()

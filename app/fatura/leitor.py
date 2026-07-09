# Leitura da fatura Bradesco
#
# Este módulo vai concentrar a lógica de extração de lançamentos
# a partir do PDF da fatura Bradesco.
#
# Status: aguardando um PDF de exemplo (real, com dados sensíveis
# mascarados se necessário) pra entender a estrutura de fato:
# - como cada linha de lançamento aparece
# - como parcelas são indicadas (ex: "3/10")
# - se o texto é extraível direto ou se tem trecho escaneado
#
# Depois que o exemplo chegar, este arquivo vira um script
# testável isoladamente no terminal, sem depender da API.

import pdfplumber


def extrair_lancamentos(caminho_pdf: str):
    """
    Ainda não implementado - placeholder.
    Vai retornar uma lista de lançamentos brutos extraídos do PDF.
    """
    raise NotImplementedError(
        "Aguardando PDF de exemplo da fatura Bradesco para implementar a extração."
    )

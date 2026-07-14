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
import sys
import re



def extrair_lancamentos(pdf_path: str):
    """
    Ainda não implementado - placeholder.
    Vai retornar uma lista de lançamentos brutos extraídos do PDF.
    """
    raise NotImplementedError(
        "Aguardando a lógica de extração (em construção)."
    )

# Este bloco só roda quando você executa "python leitor.py <caminho>"
# direto no terminal. Se este arquivo for importado por outro módulo
# (ex: a API depois), este trecho é ignorado.
# É por isso que ele fica FORA da função, sem indentação: pertence
# ao arquivo inteiro, não a extrair_lancamentos.
if __name__ == "__main__":
    caminho_pdf = sys.argv[1]  # sys.argv[0] é o nome do script; [1] é o 1º argumento

    with pdfplumber.open(caminho_pdf) as pdf:
        texto_completo = ""
        for page in pdf.pages:
            coluna_esquerda = page.crop((0, 0, 358, page.height))
            texto_completo += coluna_esquerda.extract_text()

        total_despesas = 0.0
        linhas = texto_completo.split('\n')
        for linha in linhas:
            if re.match(r"\d{2}/\d{2} ", linha):
                achado = re.search(r"(\d[\d.]*,\d{2})(-?)\s*$", linha)
                valor_texto = achado.group(1)   # ex: "1.940,44"  (o número)
                sinal = achado.group(2)         # "-" se pagamento, "" se despesa
                valor_float = float(valor_texto.replace('.', '').replace(',', '.'))  # ex: 1940.44
                if sinal == "-":
                    continue  # é pagamento/crédito, não entra na soma de despesas
                total_despesas += valor_float
        print(f"Total de despesas: R$ {total_despesas:.2f}")



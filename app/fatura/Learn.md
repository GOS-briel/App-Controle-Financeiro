re.match ou re.search
Ferramentas de detecção de datas, que são partes das módulo re das  blibiotecas do Python
Usado o re.match, neste codigo para possibilitar a identificação do padrão de datas que aparece na fatura : "20/07(DD/MM)

Linha de código com condicional + Loop + Modulo re + print 

For linha in linhas:
if re.match(r"\d{2}/\d{2}",linha):
print(linha)


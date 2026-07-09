# App de Controle Financeiro — Backend (trilha PWA + Python)

Esqueleto inicial do backend, seguindo o plano definido em `contexto_pwa.md`.

## Estrutura

```
backend/
├── main.py                  # API Flask (esqueleto)
├── requirements.txt
└── app/
    └── fatura/
        └── leitor.py         # Leitura da fatura Bradesco (aguardando exemplo)
```

## Como rodar (localmente, na sua máquina)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # no Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Depois é só abrir `http://localhost:5000` no navegador (health check).

Sem Swagger automático aqui — se quiser ver o retorno da API, é no
navegador mesmo ou com uma ferramenta tipo Postman/Insomnia/curl.
Isso é justamente a troca consciente que você fez ao escolher Flask
em vez de FastAPI: menos coisa pronta, mais controle manual.

## Próximo passo

Implementar `app/fatura/leitor.py` — depende de um PDF real da
fatura Bradesco pra mapear a estrutura de lançamentos e parcelas.
Isso vem **antes** de qualquer endpoint da API: a ideia é testar a
extração isolada, no terminal, antes de plugar em qualquer coisa.

## Decisões já travadas (não mexer sem motivo)

- Framework: Flask (escolhido conscientemente por foco em aprendizado, mesmo com curva mais lenta)
- Persistência: SQLite (a confirmar: local no backend vs IndexedDB no navegador)
- Categorias macro fixas: Alimentação, Lazer, Compras, Saúde, Educação, Esporte, Transporte, Outros
- Escopo v1 e anti-escopo: ver `contexto_pwa.md`

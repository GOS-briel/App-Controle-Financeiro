# App de Controle Financeiro — trilha PWA + Python (v1 rápida)

## Contexto do projeto

App de controle financeiro pessoal, desenvolvido em duas trilhas paralelas:
- **Trilha 1 (PWA + Python — este chat):** protótipo funcional rápido, roda no navegador do celular como app instalado, resolve o problema imediato de registrar gastos e valida o produto antes de investir na curva do Flutter
- **Trilha 2 (Flutter — chat paralelo):** app nativo "de verdade", instalável via Play Store/App Store, para distribuição posterior a outras pessoas

Esta trilha é o **rascunho funcional**. Objetivo: v1 no bolso em 6–8 semanas. Não vai virar produto distribuído — quem faz esse papel é o Flutter, depois.

## Perfil do desenvolvedor

Gabriel, CLT em concessionária de energia elétrica, primeiro semestre de ADS. Iniciante em Python, Excel, Power BI. Disponibilidade fragmentada de 8–12h/semana. Prefere aprender no ritmo dele, validando cada decisão antes de avançar.

## Princípios de produto (não-negociáveis)

1. **Fricção baixa** — registrar um gasto em <10 segundos
2. **Controle por tetos macro** — o app responde "estou no controle?" antes de qualquer outra pergunta
3. **Aprender com o uso** — categorização de fatura melhora com o tempo, sem configuração pesada

## Decisões travadas — mockups das 4 telas

### Tela 1 — Dashboard (híbrido)
- Header com mês atual + nome do usuário
- Hero: gasto vs orçamento total do mês (barra de progresso, R$ X de R$ Y, "X% do orçamento, faltam N dias")
- Lista de categorias com mini-barras, **ordem inteligente**: estouradas (vermelho + aviso "+R$ X acima do teto") → quase no teto → folgadas
- 3 últimos registros no rodapé
- Navegação inferior com **botão + preto centralizado** (leva pra tela de registrar)

### Tela 2 — Registrar gasto
- Campo Valor com **teclado nativo do sistema**, foco automático
- Pills opcionais de data (default = hoje) e nota
- Grid 4x2 de categorias macro
- Subcategorias aparecem **inline** após escolher a macro
- Subcategoria selecionada em preto sólido; opção "+" para criar nova
- Botão "Salvar gasto" no rodapé

### Tela 3 — Histórico
- Navegação entre meses por chevrons no topo
- Total do mês em destaque
- **Agrupado por categoria** (não cronológico), colapsável, com total ao lado
- Ordem inteligente (estouradas → quase teto → folgadas)
- 2 categorias mais ativas começam expandidas
- Cada lançamento: descrição, data, subcategoria, valor

### Tela 4 — Importar fatura
- Upload de PDF (Bradesco no começo)
- **Caminho B — semi-automático:** app extrai lançamentos, sugere categoria quando reconhece padrão de faturas anteriores, pede manualmente quando não reconhece
- Barra de progresso "X de N categorizados"
- **Opção Y — parcelados:** registra a parcela do mês + gera lançamentos futuros automáticos ("parcela 3/10 · gera +7 futuras")
- Resumo de impacto antes de confirmar ("importar 23 lançamentos · gera 35 futuros")
- Categorizados aparecem em chip preto com ✓; não-categorizados em chip cinza com chevron

## Categorização

**Macro (8, fixas):** Alimentação, Lazer, Compras, Saúde, Educação, Esporte, Transporte, Outros
**Subcategorias:** customizáveis pelo usuário, criadas conforme aparece a necessidade

## Escopo v1 — o que ENTRA

- 4 telas descritas acima
- Persistência local no navegador (IndexedDB via biblioteca ou localStorage pra começar)
- Tetos por categoria editáveis
- Importação de fatura Bradesco
- Funcionamento offline após primeira carga (Service Worker)

## Escopo v1 — o que NÃO ENTRA (anti-escopo)

- Múltiplas contas/cartões
- Receitas e saldo (só despesas)
- Múltiplos bancos na importação (só Bradesco na v1)
- Gráficos avançados (pizza, tendência, comparativos)
- Metas de economia
- Sincronização entre dispositivos
- Multiusuário
- Notificações push
- Categorização automática total (Caminho A) — só aprende repetidos
- Distribuição pra outras pessoas (isso é papel do Flutter, na outra trilha)

## Definição de "pronto"

A v1 está pronta quando Gabriel consegue, sem travar:
1. Registrar um gasto em <10s
2. Responder em 5s "estou estourando algum teto?"
3. Importar fatura, categorizar tudo, ver impacto no dashboard
4. Voltar 2 meses no histórico e ver gastos de uma categoria
5. Editar o teto de uma categoria

## Stack — PWA + Python

**Backend:** Python (FastAPI ou Flask) — a definir na primeira sessão
**Frontend:** HTML + CSS + JavaScript simples; possivelmente Alpine.js ou HTMX pra reduzir complexidade
**Persistência:** SQLite no backend (para os dados do Gabriel) — decisão a validar; alternativa: dados no navegador via IndexedDB
**Leitura de PDF:** pdfplumber (Python)
**PWA:** manifest.json + Service Worker pra instalação e cache offline
**Distribuição:** link direto — Gabriel abre no navegador do celular e adiciona à tela inicial
**Hospedagem:** a definir (opções baratas: Railway, Fly.io, PythonAnywhere, ou rodar local na rede de casa)
**Ambiente:** Claude Code para desenvolvimento

## Por que PWA foi escolhido pra esta trilha

- Reusa o Python que Gabriel já mexe (curva de aprendizado mínima)
- Leitura de PDF em Python é trivial e madura (pdfplumber, PyPDF2)
- Sem loja de apps, sem taxa, sem aprovação
- Primeira versão funcional em 1–2 semanas
- Serve como protótipo validado pra reconstruir em Flutter depois

## Trade-offs aceitos

- Sensação de "app de verdade" é menor (roda no navegador em tela cheia)
- Precisa de servidor rodando em algum lugar (custo baixo, $5-10/mês, ou grátis em tiers iniciais)
- Não fica em loja de apps — distribuição via link
- Acesso offline exige Service Worker (configuração extra)

## Estado atual (ponto de partida)

- Mockups: definidos ✓
- Escopo v1: definido ✓
- Stack: definido (PWA + Python) ✓
- **Próximo passo:** decidir framework backend (FastAPI vs Flask), estrutura inicial do projeto, e começar pela **camada de leitura de fatura Bradesco em Python puro** — testável sem interface, ganho imediato

## Estratégia de construção sugerida

Começar de dentro pra fora, ao contrário do Flutter:

1. **Leitura de fatura Bradesco em Python** (script puro, testável no terminal) — 1 semana
2. **Modelo de dados** (categorias, tetos, lançamentos) em SQLite — 3 dias
3. **API mínima** com FastAPI (endpoints de listar/criar/atualizar) — 1 semana
4. **Frontend das 4 telas** em HTML/CSS — 2 semanas
5. **PWA config** (manifest, service worker) — 3 dias
6. **Deploy + primeiro uso real** — 3 dias

Total estimado: 5–6 semanas de trabalho, considerando 8–12h/semana.

## Interseção com a trilha Flutter

O que essa trilha PWA vai produzir e é reutilizável no Flutter depois:
- Toda a lógica de categorização de fatura (transferível como referência, mesmo em outra linguagem)
- Clareza do que funciona/não funciona no dia a dia (validação de produto)
- Aprendizado sobre modelo de dados, edge cases da fatura Bradesco, padrões de UX que testou na prática

Nada de código Python será literalmente reaproveitado no Flutter — mas a **especificação implícita** que o PWA vai gerar reduz drasticamente o risco da curva do Flutter.

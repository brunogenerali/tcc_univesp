# Análise de Dados Eleitorais do TSE - UNIVESP TCC

Projeto de coleta, extração, tratamento e análise exploratória de dados abertos de candidaturas do Tribunal Superior Eleitoral (TSE) para as eleições municipais no Estado de São Paulo nos pleitos de **2012, 2016, 2020 e 2024**.

---

## 📁 Estrutura do Projeto

```text
univesp_tcc/
├── .devcontainer/
│   └── devcontainer.json   # Configuração do ambiente Docker unificado
├── data/
│   ├── raw/                # Arquivos .zip e CSVs brutos baixados do TSE
│   └── processed/          # Dados tratados e consolidados
├── notebooks/
│   ├── 01_analise_genero_candidatos.ipynb        # Análise temporal de representação e cotas de gênero
│   └── 02_analise_escolaridade_candidatos.ipynb  # Análise do perfil educacional e interseccional
├── output/                 # Exportações geradas (relatórios HTML, gráficos)
├── publicacao/             # Artefatos e documentos para publicação acadêmica
├── src/
│   ├── __init__.py         # Definição do pacote Python
│   ├── config.py           # Configurações centralizadas (URLs, anos 2012-2024, caminhos, logs)
│   ├── downloader.py       # Download seguro e idempotente dos dados do TSE
│   └── extractor.py        # Extração seletiva dos arquivos CSV por UF
├── main.py                 # Ponto de entrada e orquestração do pipeline de dados
├── pyproject.toml          # Dependências do projeto e configurações de ferramentas (Ruff, Pyright)
├── uv.lock                 # Lockfile determinístico de dependências
└── README.md
```

---

## 📊 Análises e Notebooks

O projeto conta com notebooks temáticos estruturados para responder a questões centrais de representatividade política no Estado de SP:

### 1. [01_analise_genero_candidatos.ipynb](notebooks/01_analise_genero_candidatos.ipynb)
- **Evolução Histórica**: Acompanhamento da proporção de candidaturas femininas e masculinas entre 2012 e 2024.
- **Aderência às Cotas de Gênero**: Avaliação do cumprimento do percentual mínimo de 30% estabelecido pela Lei nº 9.504/1997.
- **Recorte por Cargo**: Disparidade de gênero no Legislativo (*Vereador*) versus Executivo (*Prefeito* e *Vice-Prefeito*).
- **Taxa de Sucesso Eleitoral**: Relação entre o volume de candidaturas femininas e a taxa efetiva de eleitas.

### 2. [02_analise_escolaridade_candidatos.ipynb](notebooks/02_analise_escolaridade_candidatos.ipynb)
- **Evolução do Perfil Educacional**: Mudanças nos graus de instrução ao longo dos quatro pleitos municipais, destacando o avanço do Ensino Superior Completo.
- **Exigência Prática por Cargo**: Distribuição de escolaridade comparativa entre candidatos a Prefeito, Vice-Prefeito e Vereador.
- **Taxa de Sucesso por Escolaridade**: Correlação entre o grau de instrução e o percentual de sucesso nas urnas.
- **Análise Interseccional**: Comparativo da proporção de candidatas e eleitas com nível superior frente aos candidatos e eleitos do sexo masculino.

---

## 🛠️ Ambiente de Desenvolvimento

Você pode rodar este projeto de duas formas: usando **Dev Container (Docker)** ou **Localmente com `uv`**.

### Opção 1: Usando Dev Container (Recomendado)
Ideal para garantir que todos trabalhem no mesmo ambiente Linux com Python, Jupyter, extensões e dependências pré-instaladas, sem conflitos entre sistemas operacionais (Windows, Mac ou Linux).

1. Tenha o **Docker Desktop** e a extensão **Dev Containers** instalados no VS Code / Cursor.
2. Abra a pasta do projeto e selecione a opção **"Reopen in Container"** (ou `Ctrl+Shift+P` > `Dev Containers: Reopen in Container`).
3. O ambiente será montado e as dependências serão sincronizadas automaticamente via `postCreateCommand`.

---

### Opção 2: Instalação Local (via `uv`)

1. Instale o gerenciador [uv](https://docs.astral.sh/uv/):
   ```bash
   # Windows (PowerShell)
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

   # Linux/macOS
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Instale as dependências do projeto:
   ```bash
   uv sync
   ```

---

## 🚀 Execução do Pipeline e dos Notebooks

### 1. Download e Extração dos Dados do TSE
Para baixar os arquivos brutos e extrair os dados da UF configurada (padrão: `SP` para os anos de `2012`, `2016`, `2020` e `2024`):

```bash
uv run python main.py
```

### 2. Execução dos Notebooks
Com o ambiente configurado (ou via Dev Container), execute os notebooks pelo VS Code / Jupyter Lab ou via linha de comando:

```bash
# Iniciar o servidor Jupyter Lab
uv run jupyter lab
```

### 3. Publicação e Visualização dos Notebooks (HTML & GitHub Pages)
Os notebooks podem ser exportados para HTML e publicados automaticamente via **GitHub Pages**:

```bash
# Converter todos os notebooks para a pasta de publicação
uv run jupyter nbconvert --to html notebooks/*.ipynb --output-dir=publicacao/
```

- A pasta [`publicacao/`](file:///workspaces/univesp_tcc/publicacao) contém o portal [`index.html`](file:///workspaces/univesp_tcc/publicacao/index.html) e os relatórios exportados.
- O repositório conta com um workflow automatizado em [`.github/workflows/deploy-pages.yml`](file:///workspaces/univesp_tcc/.github/workflows/deploy-pages.yml) que atualiza o GitHub Pages automaticamente a cada `git push` na branch `main`.

---

## 🧹 Qualidade e Padronização de Código (Ruff)

Para manter a formatação e os padrões de código uniformes:

- **Verificar problemas de linting / imports:**
  ```bash
  uv run ruff check .
  ```
- **Aplicar correções automáticas:**
  ```bash
  uv run ruff check --fix .
  ```
- **Formatar todo o código:**
  ```bash
  uv run ruff format .
  ```


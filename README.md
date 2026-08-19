# Análise de Dados Eleitorais do TSE - UNIVESP TCC

Projeto de coleta, extração e análise de dados abertos de candidaturas do Tribunal Superior Eleitoral (TSE) para as eleições municipais no Estado de São Paulo (2016, 2020 e 2024).

---

## 📁 Estrutura do Projeto

```text
univesp_tcc/
├── .devcontainer/
│   └── devcontainer.json # Configuração do ambiente Docker unificado
├── data/
│   ├── raw/              # Arquivos .zip e CSVs brutos baixados do TSE
│   └── processed/        # Dados tratados e consolidados (Parquet/Pandas)
├── src/
│   ├── __init__.py       # Definição do pacote Python
│   ├── config.py         # Configurações centralizadas (URLs, anos, caminhos, logs)
│   ├── downloader.py     # Download seguro e idempotente dos dados do TSE
│   └── extractor.py      # Extração seletiva dos arquivos CSV por UF
├── main.py               # Ponto de entrada e orquestração do pipeline
├── pyproject.toml        # Dependências, configurações do Ruff e Pyright
├── uv.lock               # Lockfile de dependências determinísticas
└── README.md
```

---

## 🛠️ Ambiente de Desenvolvimento

Você pode rodar este projeto de duas formas: usando **Dev Container (Docker)** ou **Localmente com `uv`**.

### Opção 1: Usando Dev Container (Recomendado para o Grupo)
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

## 🚀 Execução do Pipeline

Para baixar os arquivos brutos e extrair os dados da UF configurada (padrão: `SP` para 2016, 2020 e 2024):

```bash
uv run python main.py
```

---

## 🧹 Qualidade e Padronização de Código (Ruff)

Para manter a formatação e os padrões de código uniformes entre os integrantes da equipe:

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

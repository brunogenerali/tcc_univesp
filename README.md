# Análise de Dados Eleitorais do TSE - UNIVESP TCC

Projeto de coleta, extração e análise de dados abertos de candidaturas do Tribunal Superior Eleitoral (TSE) para as eleições municipais no Estado de São Paulo.

---

## 📁 Estrutura do Projeto

```text
univesp_tcc/
├── data/
│   ├── raw/           # Arquivos .zip e CSVs brutos baixados do TSE
│   └── processed/     # Dados tratados e consolidados (Pandas)
├── src/
│   ├── __init__.py    # Definição do pacote Python
│   ├── config.py      # Configurações centralizadas (URLs, anos, caminhos, logs)
│   ├── downloader.py  # Download seguro e idempotente dos dados do TSE
│   └── extractor.py   # Extração seletiva dos arquivos CSV por UF
├── main.py            # Ponto de entrada e orquestração do pipeline
├── pyproject.toml     # Dependências e configurações do ambiente
└── README.md
```

---

## 🚀 Como Executar

### 1. Pré-requisitos
- Python `>= 3.12` (ou via [uv](https://docs.astral.sh/uv/))

### 2. Instalação de Dependências
Utilizando o gerenciador `uv`:
```bash
uv sync
```

### 3. Execução do Pipeline
Para baixar os arquivos e extrair os dados da UF configurada (padrão: `SP` para 2016, 2020 e 2024):
```bash
python main.py
```
*(ou usando o ambiente virtual gerenciado por uv)*:
```bash
uv run python main.py
```

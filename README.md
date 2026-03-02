# Analisador de Logs em Python 📊

![Python](https://img.shields.io/badge/Python-3.6+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.0-orange)


Um script em Python desenvolvido para **analisar arquivos de log automaticamente**, identificando e consolidando ocorrências dos níveis `INFO`, `WARNING` e `ERROR`.

Logs são registros gerados por sistemas e aplicações que documentam eventos relevantes durante a execução, como inicialização de serviços, alertas e falhas. Eles são essenciais para **monitoramento, diagnóstico de problemas, auditoria e análise de desempenho** em ambientes de produção.

Neste projeto, os arquivos de log são processados de forma automatizada, gerando um **relatório estruturado em CSV**, pronto para análise em ferramentas como **Excel ou Google Sheets**, facilitando a visualização e a tomada de decisão.
---

## 🌟 Funcionalidades

- Lê todos os arquivos `.log` da pasta `logs/`  
- Conta `INFO`, `WARNING` e `ERROR`  
- Gera **resumo por arquivo** e **total geral**  
- Cria relatório **CSV profissional** (ponto e vírgula como separador)  
- Fácil de usar e personalizar  

---

## 📁 Estrutura do Projeto

analisador-de-logs/
│
├─ logs/ ← Coloque seus arquivos .log aqui
│ ├─ sistema1.log
│ └─ sistema2.log
│
├─ analisador.py ← Script principal
└─ README.md ← Este arquivo


---

## 🚀 Como usar

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/analisador-de-logs.git
cd analisador-de-logs
```
2. Adicione seus arquivos .log na pasta logs/

3. Execute o script:

```bash
python3 analisador.py
```

4. Resultado no termial:

Resumo do arquivo sistema1.log:
INFO: 3
WARNING: 2
ERROR: 1

Resumo do arquivo sistema2.log:
INFO: 2
WARNING: 1
ERROR: 0

Resumo total de todos os logs:
INFO: 5
WARNING: 3
ERROR: 1

Relatório gerado: relatorio_logs.csv

5. Resultado no relatório_logs.csv

| Arquivo      | INFO | WARNING | ERROR |
| ------------ | ---- | ------- | ----- |
| sistema1.log | 3    | 2       | 1     |
| sistema2.log | 2    | 1       | 0     |
| **TOTAL**    | 5    | 3       | 1     |

Pode ser aberto no Excel ou Google Sheets.

## 💻 Requisitos

Python 3.6 ou superior

Bibliotecas padrão: os e csv (já inclusas no Python)


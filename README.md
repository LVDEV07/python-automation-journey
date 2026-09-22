# 🐍 Python: Da Base à Automação, Web Scraping e RPA

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20andamento-yellow)
![Foco](https://img.shields.io/badge/foco-automação%20%7C%20web%20scraping%20%7C%20RPA-informational)

## 📌 Sobre este repositório

Este repositório documenta minha trajetória de estudo de Python, estruturada em módulos progressivos, partindo dos fundamentos da linguagem até a construção de robôs de automação, scraping de dados na web e RPA (Robotic Process Automation).

Cada módulo é tratado como uma entrega independente: contém explicação do conceito, código comentado, exemplos aplicados a cenários reais de mercado e exercícios resolvidos. O objetivo não é só "aprender a sintaxe", mas desenvolver a capacidade de transformar um problema real (dados espalhados, tarefas repetitivas, processos manuais) em uma solução automatizada e confiável.

## 🎯 Objetivo final do estudo

Construir um robô completo em Python capaz de:
- Coletar dados de sites, incluindo páginas dinâmicas que dependem de JavaScript
- Consolidar e tratar esses dados em planilhas Excel
- Automatizar tarefas repetitivas de sistema e desktop
- Enviar relatórios por e-mail automaticamente
- Rodar de forma agendada, com logs e tratamento de erros, sem intervenção manual

Esse robô é desenvolvido como projeto final, integrando o conteúdo de todos os módulos.

## 🧠 O que este repositório demonstra

| Competência | Onde aparece |
|---|---|
| Lógica de programação e fundamentos de Python | Módulos 1 a 7 |
| Manipulação e limpeza de dados (strings, arquivos, CSV/JSON) | Módulos 1, 6, 9 |
| Consumo de APIs e requisições HTTP | Módulo 10 |
| Web scraping (conteúdo estático e dinâmico com JS) | Módulos 11 e 12 |
| Automação de desktop e RPA | Módulo 13 |
| Boas práticas para robôs em produção (logs, variáveis de ambiente, agendamento) | Módulo 14 |
| Capacidade de documentar o próprio trabalho de forma clara | Todo o repositório |

## 🛠️ Stack e ferramentas

`Python 3` · `pandas` · `openpyxl` · `requests` · `BeautifulSoup` · `Playwright/Selenium` · `PyAutoGUI` · `smtplib` · `logging` · `venv`

## 📦 Estrutura do repositório

```
├── modulo-01-variaveis-tipos-strings/
├── modulo-02-estruturas-de-dados/
├── modulo-03-lacos-de-repeticao/
├── modulo-04-funcoes/
├── modulo-05-tratamento-de-erros/
├── modulo-06-arquivos-modulos-ambiente/
├── modulo-07-orientacao-a-objetos/
├── modulo-08-automacao-arquivos-sistema/
├── modulo-09-planilhas-e-dados/
├── modulo-10-http-e-apis/
├── modulo-11-web-scraping-estatico/
├── modulo-12-web-scraping-dinamico/
├── modulo-13-rpa-automacao-desktop/
├── modulo-14-robos-em-producao/
└── projeto-final/
```

Cada pasta de módulo contém seu próprio README com a explicação do tópico, exemplos comentados, armadilhas comuns e os exercícios propostos e resolvidos.

## ✅ Progresso

- [ ] Parte 1: Base (Módulos 1 a 7)
- [ ] Parte 2: Automação, Scraping e RPA (Módulos 8 a 14)
- [ ] Projeto final integrador

## 🏗️ Projeto final

Robô de monitoramento de preços para e-commerce: acessa sites de concorrentes (estáticos e dinâmicos), coleta produtos e preços, consolida os dados em planilha Excel com histórico, envia relatório por e-mail e roda automaticamente todos os dias, com logs e tratamento de falhas.
# Horímetro App

Sistema em Python para cálculo de tempo de corte de máquinas multifio utilizadas no setor de mármore e granitos.

---

## Sobre o projeto

Trabalho no setor de multifio em uma empresa de mármore e granitos, onde os operadores anotam o horímetro inicial e final das máquinas durante o corte dos blocos.

O cálculo era feito manualmente utilizando calculadora, então decidi desenvolver este sistema em Python para automatizar o processo e facilitar o cálculo do tempo total de corte das máquinas.

---

## Como funciona

O usuário informa:

- Horímetro inicial
- Horímetro final

Formato:

HORAS:MINUTOS

Exemplo:

12325:56
12330:20

O sistema:

- valida os dados
- converte para minutos
- calcula a diferença
- retorna o tempo total de corte

---

## Funcionalidades atuais

- Validação de horímetro
- Conversão para minutos
- Cálculo de diferença
- Formatação do tempo

---

## Próximas melhorias

- Histórico de cortes
- Exportação para Excel
- Interface gráfica com Flet
- Cadastro de máquinas
- Relatórios

---

## Tecnologias

- Python
- Flet (em desenvolvimento) - interface visual com finalidade de ser intuitiva para o usuário.
- Pandas (futuramente)


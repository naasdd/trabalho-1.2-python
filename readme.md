# Campo Minado em Python

Este é um trabalho de Introdução à programação em Python, onde o objetivo é construir um Campo Minado, utilizando a biblioteca **numpy** e leitura de arquivos txt.

---

## Sobre o Jogo

O jogo consiste em um **campo retangular** composto por quadrados. Cada quadrado pode ser:

- Revelado ao ser selecionado.
- Se o quadrado tiver uma **mina**, o jogo termina imediatamente.
- Se o quadrado não tiver mina:
  - Um **número** aparece indicando quantos quadrados adjacentes contêm minas.
  - Nenhum número aparece (`#`), revelando automaticamente os quadrados adjacentes que também não contêm minas.

O jogo é **vencido** quando todos os quadrados sem minas forem revelados.

---

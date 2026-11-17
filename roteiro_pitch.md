# Roteiro do Vídeo Pitch – FILA ZERO (1 a 2 minutos)

**Apresentador:** Felipe Arruda Calixto (RM574454)
**Integrantes do grupo:** Felipe Arruda Calixto (RM574454) e Felipe Oliveira Barcelos (RM576561) – Turma 1CCPR
**Vídeo publicado:** https://youtu.be/a0WjoFRxdUY
**Duração-alvo:** cerca de 1min50s
**Formato:** câmera no começo e no fim; gravação de tela do terminal e do código no meio.

> **Atenção à regra do enunciado:** "Todos os integrantes devem ser identificados."
> Basta uma pessoa apresentar, mas o nome e o RM **dos dois** precisam aparecer no vídeo.
> Por isso a abertura fala os dois nomes e mostra um texto na tela com nomes e RMs.

---

### [0:00 – 0:15] Abertura e identificação (câmera)

*(Texto na tela durante toda a abertura:)*
```
FILA ZERO – Global Solution 2026.2 | CitizenTech
Felipe Arruda Calixto – RM574454
Felipe Oliveira Barcelos – RM576561
Turma 1CCPR
```

> "Olá! Eu sou o **Felipe Arruda Calixto, RM574454**, e faço este projeto em dupla com o
> **Felipe Oliveira Barcelos, RM576561**, da turma 1CCPR. Este é o **Fila Zero**, nossa
> solução para a Global Solution CitizenTech."

### [0:15 – 0:35] Problema, público e ODS (câmera)

> "Quem usa a UBS conhece a fila: a pessoa pode passar horas esperando, perder o dia
> de trabalho ou até desistir da consulta. O Fila Zero ajuda **usuários do SUS,
> agentes comunitários e gestores de saúde** a descobrir quais unidades estão mais
> sobrecarregadas. Ele se liga ao **ODS 3, Saúde e Bem-Estar**, e também aos ODS 10 e 11."

### [0:35 – 1:10] Demonstração do programa (gravação de tela)

1. Rodar `python fila_zero.py` e mostrar a introdução e o menu.
2. **Opção 1**: cadastrar uma UBS e digitar "quarenta" no tempo de propósito,
   para mostrar a validação. Depois digitar 72.
3. **Opção 4**: carregar os 3 registros de teste.
4. **Opção 3**: mostrar o relatório.

> "Aqui eu cadastro a UBS com nome, bairro, tempo de espera e atendimentos por dia.
> Se eu digito texto onde vai número, o programa avisa e pergunta de novo. No
> relatório aparecem a tabela, a média de espera, a UBS com maior e com menor espera,
> o total de atendimentos e o percentual de cada categoria. No final vem a
> recomendação automática: qual unidade priorizar e para onde o cidadão pode ir."

### [1:10 – 1:40] Explicação da lógica (gravação de tela no código)

*(Mostrar `classificar_espera`, a lista `registros` e o `while` do menu.)*

> "Cada UBS é uma **lista** com quatro dados, e todas ficam na lista `registros`.
> A função `classificar_espera` usa **if, elif e else**: até 30 minutos é *Adequado*,
> até 60 é *Atenção* e acima disso é *Crítico*. Os laços **for** percorrem os
> registros para calcular a média, achar o maior e o menor tempo e contar cada
> categoria. O **while** mantém o menu rodando até o usuário digitar zero. Ao todo
> são 20 funções, e os testes automáticos conferem os cálculos."

### [1:40 – 1:55] Encerramento (câmera)

> "Com o Fila Zero, o gestor sabe onde agir primeiro e o cidadão sabe para onde ir.
> Projeto de Felipe Arruda Calixto e Felipe Oliveira Barcelos. Obrigado!"

---

### Checklist antes de enviar
- [ ] O apresentador aparece na câmera
- [ ] Os **dois** integrantes estão identificados (fala + texto na tela com nome e RM)
- [ ] Problema, público e ODS foram apresentados
- [ ] O programa foi executado na tela (cadastro, validação, relatório)
- [ ] A lógica do código foi explicada (listas, if/elif/else, for/while, funções)
- [ ] O vídeo tem entre 1 e 2 minutos
- [ ] O link está público ou "não listado" e foi colado no README.md

# FILA ZERO – Monitor de Tempo de Espera nas UBS

![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)
![Sem dependências externas](https://img.shields.io/badge/depend%C3%AAncias-nenhuma-brightgreen)
[![Testes](https://github.com/FelipeArrudaCalixto/fila-zero-ubs/actions/workflows/testes.yml/badge.svg)](https://github.com/FelipeArrudaCalixto/fila-zero-ubs/actions/workflows/testes.yml)

Programa de terminal em Python que monitora o tempo de espera das Unidades Básicas de
Saúde, classifica cada unidade como **Adequado**, **Atenção** ou **Crítico** e gera
recomendações automáticas: para o gestor, onde reforçar equipes; para o cidadão, qual
UBS procurar.

**[Assista ao vídeo pitch (YouTube)](https://youtu.be/a0WjoFRxdUY)**

### Destaques

- **Python puro:** 20 funções, nenhuma biblioteca externa.
- **5 indicadores** (média, maior e menor espera, total de atendimentos, distribuição por categoria) e uma recomendação automática gerada por regras.
- **Entradas validadas:** texto vazio, números fora da faixa e opções inválidas são tratados sem quebrar o programa.
- **Testes automatizados** que rodam a cada push via GitHub Actions.

### Teste em 30 segundos

```bash
git clone https://github.com/FelipeArrudaCalixto/fila-zero-ubs.git
cd fila-zero-ubs
python fila_zero.py
```

No menu, escolha **4** para carregar 3 UBS de exemplo e depois **3** para ver o relatório.

---

**FIAP – 1º ano de Ciência da Computação – Turma 1CCPR**
Pensamento Computacional e Automação em Python – Prof. Allan Roberto Molto
**Global Solution 2026.2 | CitizenTech**

## Integrantes

| Nome                      | RM       | GitHub |
|---------------------------|----------|--------|
| Felipe Arruda Calixto     | RM574454 | [@FelipeArrudaCalixto](https://github.com/FelipeArrudaCalixto) |
| Felipe Oliveira Barcelos  | RM576561 | |

---

## 1. Introdução

Nas Unidades Básicas de Saúde (UBS), as filas longas fazem o cidadão perder horas
do dia e, muitas vezes, desistir do atendimento. Isso atinge mais quem depende só
do SUS. O público beneficiado são os usuários das UBS, os agentes comunitários de
saúde e os gestores da saúde no bairro.
O **Fila Zero** é um programa de terminal que registra o tempo médio de espera e o
número de atendimentos diários de cada UBS, classifica as unidades (Adequado,
Atenção ou Crítico), calcula indicadores e gera uma recomendação automática para
apoiar a decisão: onde reforçar equipes e qual unidade o cidadão pode procurar.
**ODS relacionados:** ODS 3 – Saúde e Bem-Estar (principal); ODS 10 – Redução das
Desigualdades; ODS 11 – Cidades e Comunidades Sustentáveis.

---

## 2. Arquivos do projeto

| Arquivo                 | Descrição                                                     |
|-------------------------|---------------------------------------------------------------|
| `fila_zero.py`          | Programa principal (código-fonte executável)                  |
| `testes_fila_zero.py`   | Testes automáticos das funções de cálculo e classificação     |
| `exemplo_execucao.txt`  | Execução completa registrada, incluindo entradas inválidas    |
| `roteiro_pitch.md`      | Roteiro do vídeo pitch (1 a 2 minutos)                        |
| `README.md`             | Este documento                                                |
| `.github/workflows/testes.yml` | Roda os testes automáticos no GitHub Actions a cada push |

---

## 3. Como executar

Requisito: Python 3.8 ou superior (não usa nenhuma biblioteca externa).

```bash
python fila_zero.py
```

Para rodar os testes automáticos:

```bash
python testes_fila_zero.py
```

> No Linux/macOS pode ser necessário usar `python3` no lugar de `python`.

### Menu do programa

| Opção | Ação                                                          |
|-------|---------------------------------------------------------------|
| 1     | Cadastrar UBS (nome, bairro, tempo de espera, atendimentos/dia) |
| 2     | Listar as UBS cadastradas em tabela                            |
| 3     | Consultar relatório: indicadores + conclusão automática        |
| 4     | Carregar 3 UBS de teste (uma de cada categoria)                |
| 5     | Ver as regras de classificação                                 |
| 0     | Encerrar o programa                                            |

Dica para a demonstração: use a opção **4** para carregar os dados de teste e depois a
opção **3** para ver o relatório. Ou cadastre as suas próprias UBS com a opção **1**.

---

## 4. Registros e atributos

Cada UBS é guardada como uma **lista** com 4 atributos, e todas ficam na lista
`registros`:

```python
registros = [
    ["UBS Vila Esperança",    "Penha",    25, 180],
    ["UBS Jardim das Flores", "Itaquera", 48, 240],
    ["UBS Parque Central",    "Sé",       95, 320],
]
#   [nome,                    bairro, espera (min), atendimentos/dia]
```

---

## 5. Regras de classificação

Critério: **tempo médio de espera** da UBS, em minutos.

| Situação     | Regra               | Significado                                   |
|--------------|---------------------|-----------------------------------------------|
| **Adequado** | até 30 min          | Espera aceitável, manter as práticas atuais   |
| **Atenção**  | de 31 a 60 min      | Espera alta, a unidade precisa de acompanhamento |
| **Crítico**  | acima de 60 min     | Espera excessiva, a unidade precisa de ação imediata |

Por que esses limites: 30 minutos foi a meta de espera que o grupo adotou para um
atendimento de atenção básica. Passando de 1 hora, o cidadão perde boa parte do
turno de trabalho ou de estudo, e a chance de desistir da consulta aumenta.

Implementação (`if/elif/else`):

```python
def classificar_espera(tempo):
    if tempo <= 30:
        return "Adequado"
    elif tempo <= 60:
        return "Atenção"
    else:
        return "Crítico"
```

### Regras da conclusão automática

| Condição                                    | Recomendação gerada                                        |
|---------------------------------------------|------------------------------------------------------------|
| 50% ou mais das UBS em "Crítico"            | Situação grave: pedir reforço emergencial de equipes       |
| Pelo menos 1 UBS "Crítico"                  | Priorizar essas unidades na distribuição de profissionais  |
| Nenhuma crítica, mas alguma em "Atenção"    | Manter monitoramento semanal                               |
| Todas "Adequado"                            | Manter as práticas atuais                                  |
| Média geral > 30 min                        | Informa quantos minutos passa da meta e sugere agendamento prévio |
| Sempre (se os tempos forem diferentes)      | Indica ao cidadão a UBS de menor espera como alternativa à de maior espera |

---

## 6. Conceitos da disciplina aplicados

| Conceito                     | Onde aparece no código                                                     |
|------------------------------|----------------------------------------------------------------------------|
| Entrada e saída de dados     | `input()` no cadastro e no menu; `print()` com f-strings formatando a tabela |
| Operadores                   | Aritméticos (soma, média, %), relacionais (`<=`, `>`), lógicos (`or`, `and`, `not`) |
| Condicionais `if/elif/else`  | `classificar_espera`, `contar_por_categoria`, `gerar_recomendacao`, menu   |
| Repetição `while`            | Loop do menu, cadastro de várias UBS, validação das entradas               |
| Repetição `for`              | Percorrer os registros para somar, achar maior/menor, contar e exibir      |
| Listas                       | `registros` (lista de listas), lista de contagem, lista de recomendações   |
| Funções                      | 20 funções, entre elas `classificar_espera` (classificação), `calcular_media_espera` e `calcular_percentual` (cálculo) |

### Tratamento de entradas

- Campos de texto vazios não são aceitos.
- Tempo e atendimentos precisam ser números inteiros (`isdigit()`) dentro de uma faixa
  válida (tempo: 0 a 600 min; atendimentos: 1 a 2000).
- Respostas S/N e opções de menu inválidas mostram uma mensagem e o programa pergunta de novo.
- Relatório e listagem sem registros mostram um aviso em vez de dar erro.
- Divisão por zero é evitada no cálculo de média e percentual.

---

## 7. Indicadores calculados

1. **Tempo médio de espera** (e a classificação dessa média)
2. **Maior tempo de espera** (UBS e bairro)
3. **Menor tempo de espera** (UBS e bairro)
4. **Total de atendimentos por dia** na rede
5. **Quantidade e percentual de UBS por categoria**, com barra gráfica em texto

---

## 8. Testes e resultados

### 8.1 Testes automáticos (`testes_fila_zero.py`)

Os testes conferem os limites exatos de cada faixa (30/31 e 60/61 min), média, total,
maior e menor valor, contagem por categoria, percentual, lista vazia, divisão por zero
e os três tipos de recomendação. Eles rodam automaticamente no GitHub Actions a cada
push (workflow `.github/workflows/testes.yml`). Saída obtida:

```
[OK] classificar_espera
[OK] indicadores (média, total, maior, menor, categorias, %)
[OK] gerar_recomendacao

Todos os testes passaram com sucesso!
```

### 8.2 Resultado com os 3 registros de teste (opção 4 → opção 3)

```
 Nº  UBS                      Bairro            Espera Atend./dia  Situação
 1   UBS Vila Esperança       Penha              25 min        180  Adequado
 2   UBS Jardim das Flores    Itaquera           48 min        240  Atenção
 3   UBS Parque Central       Sé                 95 min        320  Crítico

  Tempo médio de espera ......: 56.0 min -> Atenção
  Maior tempo de espera ......: 95 min (UBS Parque Central - Sé)
  Menor tempo de espera ......: 25 min (UBS Vila Esperança - Penha)
  Total de atendimentos/dia ..: 740

  Quantidade e percentual por categoria:
   - Adequado :   1 UBS ( 33.3%) ######
   - Atenção  :   1 UBS ( 33.3%) ######
   - Crítico  :   1 UBS ( 33.3%) ######

  > Existe 1 UBS em nível CRÍTICO. Priorizar essa unidade na distribuição de profissionais.
  > A espera média está 26.0 min acima da meta de 30 min. Sugere-se ampliar o agendamento prévio (por app ou telefone).
  > Para o cidadão: quem for à 'UBS Parque Central' (95 min) pode considerar a 'UBS Vila Esperança' (Penha), com espera de apenas 25 min.
```

### 8.3 Descrição dos resultados

Com os dados de teste, cada UBS caiu em uma categoria diferente (33,3% cada). A média
da rede ficou em **56 minutos**, quase o dobro da meta de 30 minutos, então a rede
como um todo está em "Atenção". A **UBS Parque Central (Sé)**, com 95 minutos de
espera e o maior volume de atendimentos (320/dia), é a prioridade para receber mais
profissionais. O programa também orienta o cidadão: a **UBS Vila Esperança (Penha)**
atende em 25 minutos e serve de alternativa. Assim, o gestor sabe **onde agir
primeiro** e o cidadão sabe **para onde ir**.

O arquivo `exemplo_execucao.txt` mostra uma execução completa com cadastro manual
e entradas inválidas propositais ("quarenta" no tempo, 0 atendimentos, opção 9 no menu),
todas tratadas pelo programa.

---

## 9. Vídeo pitch

Link do vídeo: **https://youtu.be/a0WjoFRxdUY**

Apresentação feita por Felipe Arruda Calixto (RM574454), com os dois integrantes
identificados no vídeo (nome e RM falados e exibidos na tela).
O roteiro está em `roteiro_pitch.md`.

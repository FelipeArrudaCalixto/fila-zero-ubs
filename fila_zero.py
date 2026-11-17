"""
==============================================================================
 FILA ZERO - Monitor de Tempo de Espera nas Unidades Básicas de Saúde (UBS)
==============================================================================
 FIAP - 1º ano de Ciência da Computação - Turma 1CCPR
 Pensamento Computacional e Automação em Python
 Global Solution 2026.2 | CitizenTech
 Prof. Allan Roberto Molto

 Integrantes:
   - Felipe Arruda Calixto      - RM574454
   - Felipe Oliveira Barcelos   - RM576561

 Como executar:  python fila_zero.py
==============================================================================
"""

# ---------------------------------------------------------------------------
# CONSTANTES - critérios de classificação (definidos pelo grupo)
# ---------------------------------------------------------------------------
LIMITE_ADEQUADO = 30   # até 30 minutos de espera -> "Adequado"
LIMITE_ATENCAO = 60    # de 31 a 60 minutos       -> "Atenção"
                       # acima de 60 minutos      -> "Crítico"
TEMPO_MAXIMO = 600     # maior tempo aceito na digitação (10 horas)
ATENDIMENTOS_MAXIMO = 2000  # maior número de atendimentos/dia aceito

# ---------------------------------------------------------------------------
# ARMAZENAMENTO EM LISTAS
# Cada registro é uma lista: [nome_ubs, bairro, tempo_espera, atendimentos]
# Todos os registros ficam guardados na lista "registros".
# ---------------------------------------------------------------------------
registros = []


# ---------------------------------------------------------------------------
# FUNÇÕES DE ENTRADA DE DADOS (com tratamento de entradas inválidas)
# ---------------------------------------------------------------------------
def ler_texto(mensagem):
    """Lê um texto que não pode ficar vazio."""
    texto = input(mensagem).strip()
    while texto == "":
        print("   [!] Este campo não pode ficar vazio. Tente novamente.")
        texto = input(mensagem).strip()
    return texto


def ler_inteiro(mensagem, minimo, maximo):
    """Lê um número inteiro entre 'minimo' e 'maximo' (inclusive).
    Repete a pergunta enquanto o usuário digitar algo inválido."""
    while True:
        valor = input(mensagem).strip()
        if not valor.isdigit():
            print("   [!] Digite apenas números inteiros (ex.: 45).")
        elif int(valor) < minimo or int(valor) > maximo:
            print(f"   [!] O valor deve estar entre {minimo} e {maximo}.")
        else:
            return int(valor)


# ---------------------------------------------------------------------------
# FUNÇÕES DE CLASSIFICAÇÃO E CÁLCULO
# ---------------------------------------------------------------------------
def classificar_espera(tempo):
    """Classifica uma UBS a partir do tempo médio de espera (em minutos).

    Regras definidas pelo grupo:
      - até 30 min        -> "Adequado"  (espera aceitável)
      - de 31 a 60 min    -> "Atenção"   (precisa de acompanhamento)
      - acima de 60 min   -> "Crítico"   (precisa de ação imediata)
    """
    if tempo <= LIMITE_ADEQUADO:
        return "Adequado"
    elif tempo <= LIMITE_ATENCAO:
        return "Atenção"
    else:
        return "Crítico"


def calcular_media_espera(lista):
    """Calcula a média simples dos tempos de espera."""
    if len(lista) == 0:
        return 0
    soma = 0
    for registro in lista:
        soma = soma + registro[2]
    return soma / len(lista)


def calcular_total_atendimentos(lista):
    """Soma o número de atendimentos diários de todas as UBS."""
    total = 0
    for registro in lista:
        total = total + registro[3]
    return total


def encontrar_maior_espera(lista):
    """Retorna o registro (UBS) com o MAIOR tempo de espera."""
    maior = lista[0]
    for registro in lista:
        if registro[2] > maior[2]:
            maior = registro
    return maior


def encontrar_menor_espera(lista):
    """Retorna o registro (UBS) com o MENOR tempo de espera."""
    menor = lista[0]
    for registro in lista:
        if registro[2] < menor[2]:
            menor = registro
    return menor


def contar_por_categoria(lista):
    """Conta quantas UBS existem em cada categoria.
    Retorna uma lista: [qtd_adequado, qtd_atencao, qtd_critico]."""
    adequado = 0
    atencao = 0
    critico = 0
    for registro in lista:
        categoria = classificar_espera(registro[2])
        if categoria == "Adequado":
            adequado = adequado + 1
        elif categoria == "Atenção":
            atencao = atencao + 1
        else:
            critico = critico + 1
    return [adequado, atencao, critico]


def calcular_percentual(parte, total):
    """Calcula o percentual de 'parte' em relação ao 'total'."""
    if total == 0:
        return 0
    return parte / total * 100


def gerar_recomendacao(lista):
    """Gera uma conclusão automática com base nos indicadores calculados.
    Retorna uma lista de frases (strings) com as recomendações."""
    frases = []
    contagem = contar_por_categoria(lista)
    perc_critico = calcular_percentual(contagem[2], len(lista))
    media = calcular_media_espera(lista)
    maior = encontrar_maior_espera(lista)
    menor = encontrar_menor_espera(lista)

    # Situação geral da rede de UBS
    if perc_critico >= 50:
        frases.append("SITUAÇÃO GRAVE: metade ou mais das UBS estão em nível "
                      "CRÍTICO. Recomenda-se solicitar à Secretaria de Saúde "
                      "reforço emergencial de equipes.")
    elif contagem[2] > 0:
        if contagem[2] == 1:
            frases.append("Existe 1 UBS em nível CRÍTICO. Priorizar essa "
                          "unidade na distribuição de profissionais.")
        else:
            frases.append(f"Existem {contagem[2]} UBS em nível CRÍTICO. "
                          "Priorizar essas unidades na distribuição de "
                          "profissionais.")
    elif contagem[1] > 0:
        frases.append("Nenhuma UBS crítica, mas há unidades em ATENÇÃO. "
                      "Manter monitoramento semanal.")
    else:
        frases.append("Todas as UBS estão com espera ADEQUADA. Manter as "
                      "práticas atuais de atendimento.")

    # Comparação da média com o limite adequado
    if media > LIMITE_ADEQUADO:
        excesso = media - LIMITE_ADEQUADO
        frases.append(f"A espera média está {excesso:.1f} min acima da meta "
                      f"de {LIMITE_ADEQUADO} min. Sugere-se ampliar o "
                      "agendamento prévio (por app ou telefone).")
    else:
        frases.append(f"A espera média está dentro da meta de "
                      f"{LIMITE_ADEQUADO} min.")

    # Sugestão para o cidadão: unidade alternativa
    if maior[2] != menor[2]:
        frases.append(f"Para o cidadão: quem for à '{maior[0]}' "
                      f"({maior[2]} min) pode considerar a '{menor[0]}' "
                      f"({menor[1]}), com espera de apenas {menor[2]} min.")
    return frases


# ---------------------------------------------------------------------------
# FUNÇÕES DE TELA (exibição organizada)
# ---------------------------------------------------------------------------
def linha(caractere="-", tamanho=78):
    print(caractere * tamanho)


def mostrar_introducao():
    linha("=")
    print("  FILA ZERO - Monitor de Tempo de Espera nas UBS".center(78))
    linha("=")
    print(" Problema: longas filas nas Unidades Básicas de Saúde (UBS) fazem o")
    print(" cidadão perder horas e, muitas vezes, desistir do atendimento.")
    print(" Público beneficiado: usuários do SUS, agentes comunitários e gestores")
    print(" de saúde do bairro.")
    print(" Objetivo: registrar o tempo médio de espera de cada UBS, classificar")
    print(" as unidades e gerar indicadores e recomendações para a decisão.")
    print(" ODS 3 - Saúde e Bem-Estar | ODS 10 - Redução das Desigualdades |")
    print(" ODS 11 - Cidades e Comunidades Sustentáveis.")
    linha("=")


def mostrar_menu():
    print()
    print("+------------------------- MENU -------------------------+")
    print("|  1 - Cadastrar UBS                                     |")
    print("|  2 - Listar UBS cadastradas                            |")
    print("|  3 - Consultar relatório (indicadores e recomendação)  |")
    print("|  4 - Carregar dados de teste (3 UBS de exemplo)        |")
    print("|  5 - Ver regras de classificação                       |")
    print("|  0 - Encerrar o programa                               |")
    print("+--------------------------------------------------------+")


def mostrar_regras():
    print()
    linha()
    print(" REGRAS DE CLASSIFICAÇÃO (tempo médio de espera)")
    linha()
    print(f"  Adequado : até {LIMITE_ADEQUADO} minutos")
    print(f"  Atenção  : de {LIMITE_ADEQUADO + 1} a {LIMITE_ATENCAO} minutos")
    print(f"  Crítico  : acima de {LIMITE_ATENCAO} minutos")
    linha()


def mostrar_tabela(lista):
    """Percorre a lista de registros e exibe em formato de tabela."""
    print()
    linha()
    print(f" {'Nº':<3} {'UBS':<24} {'Bairro':<16} {'Espera':>7} "
          f"{'Atend./dia':>10}  {'Situação':<9}")
    linha()
    numero = 1
    for registro in lista:
        situacao = classificar_espera(registro[2])
        print(f" {numero:<3} {registro[0][:24]:<24} {registro[1][:16]:<16} "
              f"{registro[2]:>4} min {registro[3]:>10}  {situacao:<9}")
        numero = numero + 1
    linha()
    print(f" Total de UBS cadastradas: {len(lista)}")


# ---------------------------------------------------------------------------
# FUNÇÕES DAS OPÇÕES DO MENU
# ---------------------------------------------------------------------------
def cadastrar_ubs():
    """Cadastra uma ou mais UBS na lista de registros."""
    continuar = "S"
    while continuar == "S":
        print()
        print(f"--- Cadastro da UBS nº {len(registros) + 1} ---")
        nome = ler_texto("Nome da UBS: ")
        bairro = ler_texto("Bairro: ")
        tempo = ler_inteiro("Tempo médio de espera (minutos): ", 0, TEMPO_MAXIMO)
        atendimentos = ler_inteiro("Atendimentos por dia: ", 1,
                                   ATENDIMENTOS_MAXIMO)

        registros.append([nome, bairro, tempo, atendimentos])
        print(f"   [OK] UBS '{nome}' cadastrada -> situação: "
              f"{classificar_espera(tempo)}")

        continuar = input("Deseja cadastrar outra UBS? (S/N): ").strip().upper()
        while continuar != "S" and continuar != "N":
            continuar = input("   [!] Responda S ou N: ").strip().upper()

    if len(registros) < 3:
        print(f"\n   Dica: cadastre pelo menos 3 UBS para um relatório "
              f"mais completo (faltam {3 - len(registros)}).")


def listar_ubs():
    if len(registros) == 0:
        print("\n   [!] Nenhuma UBS cadastrada. Use a opção 1 ou 4.")
    else:
        mostrar_tabela(registros)


def mostrar_relatorio():
    """Processa os registros e apresenta indicadores e recomendações."""
    if len(registros) == 0:
        print("\n   [!] Nenhuma UBS cadastrada. Use a opção 1 ou 4.")
        return

    mostrar_tabela(registros)

    media = calcular_media_espera(registros)
    total_atend = calcular_total_atendimentos(registros)
    maior = encontrar_maior_espera(registros)
    menor = encontrar_menor_espera(registros)
    contagem = contar_por_categoria(registros)
    total = len(registros)

    print()
    linha("=")
    print("  RELATÓRIO - INDICADORES".center(78))
    linha("=")
    print(f"  Tempo médio de espera ......: {media:.1f} min "
          f"-> {classificar_espera(media)}")
    print(f"  Maior tempo de espera ......: {maior[2]} min ({maior[0]} - "
          f"{maior[1]})")
    print(f"  Menor tempo de espera ......: {menor[2]} min ({menor[0]} - "
          f"{menor[1]})")
    print(f"  Total de atendimentos/dia ..: {total_atend}")
    print()
    print("  Quantidade e percentual por categoria:")
    categorias = ["Adequado", "Atenção", "Crítico"]
    for i in range(len(categorias)):
        perc = calcular_percentual(contagem[i], total)
        barra = "#" * int(perc / 5)
        print(f"   - {categorias[i]:<9}: {contagem[i]:>3} UBS "
              f"({perc:5.1f}%) {barra}")

    print()
    linha("=")
    print("  CONCLUSÃO AUTOMÁTICA / RECOMENDAÇÕES".center(78))
    linha("=")
    for frase in gerar_recomendacao(registros):
        print(f"  > {frase}")
    linha("=")


def carregar_dados_teste():
    """Adiciona 3 registros de exemplo (um de cada categoria)."""
    for registro in registros:
        if registro[0] == "UBS Vila Esperança":
            print("\n   [!] Os dados de teste já foram carregados.")
            return
    registros.append(["UBS Vila Esperança", "Penha", 25, 180])
    registros.append(["UBS Jardim das Flores", "Itaquera", 48, 240])
    registros.append(["UBS Parque Central", "Sé", 95, 320])
    print("\n   [OK] 3 UBS de teste carregadas (Adequado, Atenção e Crítico).")


# ---------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------------
def main():
    mostrar_introducao()
    opcao = ""
    while opcao != "0":
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_ubs()
        elif opcao == "2":
            listar_ubs()
        elif opcao == "3":
            mostrar_relatorio()
        elif opcao == "4":
            carregar_dados_teste()
        elif opcao == "5":
            mostrar_regras()
        elif opcao == "0":
            print("\nEncerrando o Fila Zero. Obrigado por cuidar da saúde "
                  "da sua comunidade!")
        else:
            print("\n   [!] Opção inválida. Digite 0, 1, 2, 3, 4 ou 5.")


if __name__ == "__main__":
    main()

"""
Testes automáticos do projeto FILA ZERO
Integrantes: Felipe Arruda Calixto (RM574454) e Felipe Oliveira Barcelos (RM576561)
Turma 1CCPR - FIAP

Como executar:  python testes_fila_zero.py
Cada teste usa 'assert': se algum resultado estiver errado, o programa avisa.
"""

from fila_zero import (classificar_espera, calcular_media_espera,
                       calcular_total_atendimentos, encontrar_maior_espera,
                       encontrar_menor_espera, contar_por_categoria,
                       calcular_percentual, gerar_recomendacao)

# Três registros de teste: [nome, bairro, tempo_espera, atendimentos]
dados_teste = [
    ["UBS Vila Esperança", "Penha", 25, 180],
    ["UBS Jardim das Flores", "Itaquera", 48, 240],
    ["UBS Parque Central", "Sé", 95, 320],
]


def teste_classificacao():
    # Limites exatos de cada faixa
    assert classificar_espera(0) == "Adequado"
    assert classificar_espera(30) == "Adequado"
    assert classificar_espera(31) == "Atenção"
    assert classificar_espera(60) == "Atenção"
    assert classificar_espera(61) == "Crítico"
    assert classificar_espera(240) == "Crítico"
    print("[OK] classificar_espera")


def teste_indicadores():
    media = calcular_media_espera(dados_teste)
    assert round(media, 2) == 56.0          # (25 + 48 + 95) / 3
    assert calcular_total_atendimentos(dados_teste) == 740
    assert encontrar_maior_espera(dados_teste)[0] == "UBS Parque Central"
    assert encontrar_menor_espera(dados_teste)[0] == "UBS Vila Esperança"
    assert contar_por_categoria(dados_teste) == [1, 1, 1]
    assert round(calcular_percentual(1, 3), 1) == 33.3
    assert calcular_percentual(5, 0) == 0   # evita divisão por zero
    assert calcular_media_espera([]) == 0   # lista vazia
    print("[OK] indicadores (média, total, maior, menor, categorias, %)")


def teste_recomendacao():
    frases = gerar_recomendacao(dados_teste)
    assert "Existe 1 UBS em nível CRÍTICO" in frases[0]
    assert "acima da meta" in frases[1]
    assert "UBS Vila Esperança" in frases[2]

    tudo_bem = [["A", "X", 10, 50], ["B", "Y", 20, 60], ["C", "Z", 15, 70]]
    assert "ADEQUADA" in gerar_recomendacao(tudo_bem)[0]

    grave = [["A", "X", 90, 50], ["B", "Y", 120, 60], ["C", "Z", 20, 70]]
    assert "GRAVE" in gerar_recomendacao(grave)[0]
    print("[OK] gerar_recomendacao")


teste_classificacao()
teste_indicadores()
teste_recomendacao()
print("\nTodos os testes passaram com sucesso!")

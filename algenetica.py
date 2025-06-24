import numpy as np
import random
import matplotlib.pyplot as plt
import os
import sys
from typing import List, Tuple, Dict, Any

# =======================
# Parâmetros do Problema e do Algoritmo Genético
# =======================
# Parâmetros da instância da mochila
PESO_MAXIMO_MOCHILA: int = 1550  # Peso máximo que a mochila pode suportar
ARQUIVO_INSTANCIA: str = 'knapsack-instance.txt' # Arquivo com os valores e pesos dos itens

# Parâmetros do Algoritmo Genético
TAMANHO_POPULACAO: int = 200     # Número de indivíduos em cada geração
TAXA_MUTACAO: float = 0.05       # Probabilidade de um indivíduo sofrer mutação
NUMERO_GERACOES: int = 99        # Número de gerações por execução do AG
NUMERO_EXECUCOES: int = 20        # Quantas vezes o AG será executado independentemente
TAMANHO_TORNEIO: int = 5         # Número de indivíduos selecionados para o torneio

# Controle de Execução
VERBOSE: bool = False            # Se True, imprime estatísticas a cada geração
LOG_SAIDA: str = "saida_execucoes.txt" # Arquivo para registrar a saída detalhada

# =======================
# Leitura do Arquivo de Instância
# =======================
# Estas listas armazenarão os valores e pesos dos itens disponíveis
lista_valores_itens: List[int] = []
lista_pesos_itens: List[int] = []

try:
    with open(ARQUIVO_INSTANCIA, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
        if len(linhas) < 3:
            print(f"Erro: O arquivo '{ARQUIVO_INSTANCIA}' parece estar mal formatado ou vazio demais.")
            sys.exit(1)
        
        # Ignora as duas primeiras linhas de cabeçalho/comentário
        # A terceira linha geralmente contém o número de itens e a capacidade, que já definimos ou não usamos diretamente aqui.
        # As linhas subsequentes contêm valor e peso de cada item.
        for linha in linhas[2:]: # Ajuste o índice se o formato do seu arquivo for diferente
            partes = linha.split()
            if len(partes) == 2:
                try:
                    valor, peso = map(int, partes)
                    lista_valores_itens.append(valor)
                    lista_pesos_itens.append(peso)
                except ValueError:
                    print(f"Aviso: Ignorando linha mal formatada no arquivo de instância: {linha.strip()}")
            elif linha.strip(): # Se a linha não está vazia mas não tem 2 partes
                 print(f"Aviso: Ignorando linha com formato inesperado: {linha.strip()}")


except FileNotFoundError:
    print(f"Erro: Arquivo de instância '{ARQUIVO_INSTANCIA}' não encontrado.")
    sys.exit(1)
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo '{ARQUIVO_INSTANCIA}': {e}")
    sys.exit(1)

if not lista_valores_itens or not lista_pesos_itens:
    print("Erro: Não foram carregados itens do arquivo. Verifique o formato do arquivo e o caminho.")
    sys.exit(1)

TAMANHO_CROMOSSOMO: int = len(lista_valores_itens) # Cada gene representa um item

# ================================================================
# Configuração para Gravar Saída no Terminal e em Arquivo de Log
# ================================================================
try:
    log_file = open(LOG_SAIDA, "w", buffering=1, encoding="utf-8") # buffering=1 para flush automático
except IOError as e:
    print(f"Erro ao abrir o arquivo de log '{LOG_SAIDA}': {e}")
    sys.exit(1)

class Tee:
    """Classe para redirecionar sys.stdout para múltiplos streams (terminal e arquivo)."""
    def __init__(self, *streams):
        self.streams = streams

    def write(self, data: str):
        for s in self.streams:
            try:
                s.write(data)
            except Exception as e:
                # Em caso de erro de escrita em um stream, tenta continuar nos outros
                print(f"Erro ao escrever no stream: {e}", file=sys.__stderr__)


    def flush(self):
        for s in self.streams:
            try:
                s.flush()
            except Exception as e:
                print(f"Erro ao fazer flush no stream: {e}", file=sys.__stderr__)


orig_stdout = sys.stdout
sys.stdout = Tee(orig_stdout, log_file)

# =======================
# Funções Auxiliares do Algoritmo Genético
# =======================
# Um indivíduo (solução) é representado como uma lista de bits (0 ou 1),
# onde cada bit indica se o item correspondente está na mochila.

def calcular_valor_total(solucao: List[int]) -> int:
    """Calcula o valor total dos itens na mochila para uma dada solução."""
    valor_total = 0
    for i, item_selecionado in enumerate(solucao):
        if item_selecionado == 1:
            valor_total += lista_valores_itens[i]
    return valor_total

def calcular_peso_total(solucao: List[int]) -> int:
    """Calcula o peso total dos itens na mochila para uma dada solução."""
    peso_total = 0
    for i, item_selecionado in enumerate(solucao):
        if item_selecionado == 1:
            peso_total += lista_pesos_itens[i]
    return peso_total

def solucao_e_valida(solucao: List[int]) -> bool:
    """Verifica se uma solução é válida (não excede o peso máximo)."""
    return calcular_peso_total(solucao) <= PESO_MAXIMO_MOCHILA

def gerar_solucao_aleatoria_valida() -> List[int]:
    """Gera uma solução aleatória que seja válida."""
    # Tenta gerar uma solução válida. Para problemas densos, pode ser mais eficiente
    # começar com uma mochila vazia e adicionar itens aleatoriamente até que seja válida
    # ou encha. Para este caso, a abordagem original é mantida.
    while True:
        # Gera um cromossomo com bits aleatórios (0 ou 1)
        solucao = [random.randint(0, 1) for _ in range(TAMANHO_CROMOSSOMO)]
        if solucao_e_valida(solucao):
            return solucao

def selecao_por_torneio(populacao: List[List[int]]) -> Tuple[List[int], List[int]]:
    """Seleciona dois pais da população usando o método do torneio."""
    # Seleciona k indivíduos aleatoriamente da população
    candidatos_torneio = random.sample(populacao, TAMANHO_TORNEIO)
    
    # Ordena os candidatos pelo seu valor (fitness) em ordem decrescente
    # Nota: calcular_valor_total é chamado aqui. Para otimizar,
    # o fitness poderia ser calculado uma vez por geração e armazenado com o indivíduo.
    candidatos_torneio.sort(key=calcular_valor_total, reverse=True)
    
    # Retorna os dois melhores candidatos como pais
    return candidatos_torneio[0], candidatos_torneio[1]

def cruzamento_uniforme(pai1: List[int], pai2: List[int]) -> List[int]:
    """Realiza o cruzamento uniforme entre dois pais para gerar um filho."""
    filho = []
    for i in range(TAMANHO_CROMOSSOMO):
        # Para cada gene, escolhe aleatoriamente o gene de um dos pais
        if random.random() < 0.5:
            filho.append(pai1[i])
        else:
            filho.append(pai2[i])
    return filho

def mutacao_bit_flip(solucao: List[int]) -> List[int]:
    """Realiza a mutação em um filho, invertendo um bit aleatório."""
    filho_mutado = solucao[:] # Cria uma cópia para não alterar o original
    # Escolhe um índice aleatório no cromossomo
    idx_mutacao = random.randint(0, TAMANHO_CROMOSSOMO - 1)
    # Inverte o bit nesse índice (0 vira 1, 1 vira 0)
    filho_mutado[idx_mutacao] = 1 - filho_mutado[idx_mutacao]
    return filho_mutado

# =======================
# Algoritmo Genético Principal
# =======================
def executar_algoritmo_genetico() -> Dict[str, Any]:
    """Executa o algoritmo genético para o problema da mochila."""
    # Inicializa a população com soluções aleatórias válidas
    populacao_atual = [gerar_solucao_aleatoria_valida() for _ in range(TAMANHO_POPULACAO)]
    
    # Ordena a população inicial pelo valor (fitness)
    # Novamente, o fitness é calculado aqui.
    populacao_atual.sort(key=calcular_valor_total, reverse=True)

    historico_melhor_fitness_geracao: List[float] = []
    historico_media_fitness_geracao: List[float] = []

    print(f"\nIniciando Algoritmo Genético ({NUMERO_GERACOES} gerações, {TAMANHO_POPULACAO} indivíduos)")

    for geracao in range(NUMERO_GERACOES):
        nova_populacao: List[List[int]] = []

        # Elitismo: o melhor indivíduo da geração anterior passa para a próxima
        if populacao_atual: # Garante que a população não está vazia
             nova_populacao.append(populacao_atual[0])

        # Geração de novos indivíduos
        tentativas_geracao_filhos = 0
        max_tentativas = TAMANHO_POPULACAO * 10 # Limite para evitar loop infinito

        while len(nova_populacao) < TAMANHO_POPULACAO and tentativas_geracao_filhos < max_tentativas:
            pai1, pai2 = selecao_por_torneio(populacao_atual)
            filho = cruzamento_uniforme(pai1, pai2)

            if random.random() < TAXA_MUTACAO:
                filho = mutacao_bit_flip(filho)
            
            if solucao_e_valida(filho):
                nova_populacao.append(filho)
            
            tentativas_geracao_filhos += 1
        
        # Se não conseguiu preencher a população com filhos válidos,
        # completa com soluções aleatórias válidas.
        while len(nova_populacao) < TAMANHO_POPULACAO:
            nova_populacao.append(gerar_solucao_aleatoria_valida())

        populacao_atual = nova_populacao
        populacao_atual.sort(key=calcular_valor_total, reverse=True)

        # Coleta de estatísticas da geração
        valores_fitness_populacao = [calcular_valor_total(s) for s in populacao_atual]
        melhor_fitness_da_geracao = valores_fitness_populacao[0] if valores_fitness_populacao else 0
        media_fitness_da_geracao = np.mean(valores_fitness_populacao) if valores_fitness_populacao else 0
        
        historico_melhor_fitness_geracao.append(melhor_fitness_da_geracao)
        historico_media_fitness_geracao.append(media_fitness_da_geracao)

        if VERBOSE:
            print(f"Geração {geracao+1:3d}: Melhor Fitness = {melhor_fitness_da_geracao:5.0f} | Média Fitness = {media_fitness_da_geracao:7.2f}")

    melhor_solucao_final = populacao_atual[0] if populacao_atual else []
    
    return {
        'melhor_valor_encontrado': calcular_valor_total(melhor_solucao_final) if melhor_solucao_final else 0,
        'peso_da_melhor_solucao': calcular_peso_total(melhor_solucao_final) if melhor_solucao_final else 0,
        'melhor_solucao_cromossomo': melhor_solucao_final,
        'historico_melhor_fitness': historico_melhor_fitness_geracao,
        'historico_media_fitness': historico_media_fitness_geracao
    }

# =======================
# Execução Múltipla do AG e Coleta de Resultados
# =======================
todos_melhores_valores: List[float] = []
todos_historicos_melhor_fitness: List[List[float]] = []

print(f"Iniciando {NUMERO_EXECUCOES} execuções do Algoritmo Genético...")

for i_execucao in range(1, NUMERO_EXECUCOES + 1):
    print(f"\n========== Execução {i_execucao}/{NUMERO_EXECUCOES} ==========")
    resultado_execucao = executar_algoritmo_genetico()
    
    todos_melhores_valores.append(resultado_execucao['melhor_valor_encontrado'])
    todos_historicos_melhor_fitness.append(resultado_execucao['historico_melhor_fitness'])

    print(f">>> Melhor valor encontrado na execução: {resultado_execucao['melhor_valor_encontrado']}")
    print(f"    Peso da melhor solução: {resultado_execucao['peso_da_melhor_solucao']}")
    # print(f"    Cromossomo: {resultado_execucao['melhor_solucao_cromossomo']}") # Descomente se quiser ver o cromossomo

# =======================
# Cálculo e Exibição de Estatísticas Finais
# =======================
if todos_melhores_valores:
    media_dos_melhores_valores = np.mean(todos_melhores_valores)
    desvio_padrao_dos_valores = np.std(todos_melhores_valores)
    melhor_valor_geral = np.max(todos_melhores_valores)
    pior_valor_geral = np.min(todos_melhores_valores)

    print("\n========== Resumo das Execuções ==========")
    print(f"Número de execuções: {NUMERO_EXECUCOES}")
    print(f"Média dos melhores valores obtidos : {media_dos_melhores_valores:.2f}")
    print(f"Desvio padrão dos valores        : {desvio_padrao_dos_valores:.2f}")
    print(f"Melhor valor geral obtido        : {melhor_valor_geral:.0f}")
    print(f"Pior valor geral obtido          : {pior_valor_geral:.0f}")
    print("==========================================")
else:
    print("\nNenhuma execução completada com sucesso. Não há estatísticas para mostrar.")

# =======================
# Geração de Gráficos
# =======================
PASTA_FIGURAS = 'figs'
os.makedirs(PASTA_FIGURAS, exist_ok=True) # Cria o diretório se não existir

# 1. Boxplot da distribuição dos melhores valores
if todos_melhores_valores:
    plt.figure(figsize=(10, 6))
    plt.boxplot(todos_melhores_valores, vert=False, patch_artist=True,
                boxprops=dict(facecolor='lightblue', color='black'),
                medianprops=dict(color='red', linewidth=2))
    plt.title(f"Distribuição dos Melhores Valores ({NUMERO_EXECUCOES} Execuções)")
    plt.xlabel("Valor da Função Objetivo (Melhor Valor Encontrado)")
    plt.yticks([1], ['Resultados']) # Rótulo para o boxplot
    plt.grid(True, axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    try:
        plt.savefig(os.path.join(PASTA_FIGURAS, 'boxplot_melhores_valores.png'))
        print(f"\nGráfico 'boxplot_melhores_valores.png' salvo em '{PASTA_FIGURAS}/'")
    except Exception as e:
        print(f"Erro ao salvar o gráfico boxplot: {e}")
    plt.show()

# 2. Gráfico da evolução da média do melhor fitness por geração
if todos_historicos_melhor_fitness:
    # Calcula a média do melhor fitness em cada geração, através de todas as execuções
    try:
        media_do_melhor_fitness_por_geracao = np.mean(todos_historicos_melhor_fitness, axis=0)
        
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, NUMERO_GERACOES + 1), media_do_melhor_fitness_por_geracao, 
                 linewidth=2, color='dodgerblue', marker='o', markersize=4, linestyle='-')
        plt.title(f"Média da Melhor Aptidão por Geração ({NUMERO_EXECUCOES} Execuções)")
        plt.xlabel("Geração")
        plt.ylabel("Melhor Valor Médio (Fitness)")
        plt.xticks(range(0, NUMERO_GERACOES + 1, max(1, NUMERO_GERACOES // 10))) # Melhora a legibilidade dos ticks do eixo X
        plt.grid(True, linestyle=':', alpha=0.7)
        plt.tight_layout()
        try:
            plt.savefig(os.path.join(PASTA_FIGURAS, 'evolucao_media_melhor_fitness.png'))
            print(f"Gráfico 'evolucao_media_melhor_fitness.png' salvo em '{PASTA_FIGURAS}/'")
        except Exception as e:
            print(f"Erro ao salvar o gráfico de evolução: {e}")
        plt.show()
    except Exception as e:
        print(f"Erro ao processar dados para o gráfico de evolução: {e}")


# =======================
# Finalização
# =======================
print("\nExecução do Algoritmo Genético concluída.")
print(f"Resultados detalhados foram salvos em: {LOG_SAIDA}")

# Garante que tudo foi escrito no arquivo de log e fecha o arquivo
sys.stdout.flush() # sys.stdout é nosso objeto Tee
if log_file:
    try:
        log_file.close()
    except Exception as e:
        print(f"Erro ao fechar o arquivo de log: {e}", file=sys.__stderr__)

# Restaura a saída padrão original
sys.stdout = orig_stdout
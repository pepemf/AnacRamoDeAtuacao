import matplotlib.pyplot as plt
import pandas as pd

try:
    data = pd.read_csv('SISANT.csv', sep=';', low_memory=False)
except FileNotFoundError:
    exit('O arquivo "SISANT.csv" não foi encontrado no diretório do script')


def queryUser():
    answerTuple = ('1', '2', '3', 'sair', 'exit')
    answer = input('Por favor, digite o número do gráfico que deseja visualizar:\n'
                   '\t1 - Top 15\n'
                   '\t2 - Últimos\n'
                   '\t3 - Todos\n'
                   'Ou para sair, digite "sair" ou "exit"\nUser:> ')
    if answer.lower() not in answerTuple:
        print("Um erro ocorreu, por favor tente novamente")
        return queryUser()
    elif answer.lower() in (answerTuple[3], answerTuple[4]):
        exit('Good Bye!')
    else:
        genGraph(answer)


def genGraph(graphNumber):
    functions = {
        '1': top15Graph,
        '2': othersGraph,
        '3': allGraph
    }
    return functions[graphNumber]()


def top15Graph():
    # Calcula os dados para o gráfico "Top 15"
    atuacaoCounts = data['Unnamed: 9'].value_counts()
    top15Atuacao = atuacaoCounts.head(15)
    outrosCounts = atuacaoCounts[atuacaoCounts <= 241].sum() - 241
    top15Atuacao['Outros'] = outrosCounts

    # Cria o gráfico
    plt.figure(figsize=(12, 6))
    top15Atuacao.plot(kind='bar', width=0.7, color='darkred')

    font = {'family': 'serif',
            'color': 'darkred',
            'weight': 'normal',
            'size': 14,
            }

    plt.xlabel('Ramos de Atuação', fontdict=font)
    plt.ylabel('Número de drones', fontdict=font)
    plt.title('Top 15 Atuações', fontdict=font)

    plt.xticks(rotation=45, horizontalalignment='right', fontsize=8)

    plt.subplots_adjust(bottom=0.5)

    # Adiciona rótulos nas barras do gráfico
    for idx, value in enumerate(top15Atuacao, start=0):
        plt.annotate(f'{value}', (idx, value), ha='center', va='bottom')

    plt.show()

def othersGraph():
    # Calcula os dados para o gráfico "Ultimos"
    print("Atenção: este gráfico pode demorar a ser gerado, aguarde com paciência")
    atuacaoCounts = data['Unnamed: 9'].value_counts().tail(2188)
    plt.figure(figsize=(12, 6))

    # Cria o gráfico
    atuacaoCounts.plot(kind='bar', width=1, linewidth=0, color='darkred').set_xticklabels([])

    font = {'family': 'serif',
            'color': 'darkred',
            'weight': 'normal',
            'size': 14,
            }

    plt.xlabel('Ramos de Atuação', fontdict=font)
    plt.ylabel('Número de drones', fontdict=font)
    plt.title('Ultimas atuações', fontdict=font)

    plt.subplots_adjust(bottom=0.5)

    plt.show()

def allGraph():
    # Calcula os dados para o gráfico "Todos"
    print("Atenção: este gráfico pode demorar a ser gerado, aguarde com paciência")
    atuacaoCounts = data['Unnamed: 9'].value_counts()

    plt.figure(figsize=(12, 6))

    # Cria o gráfico
    atuacaoCounts.plot(kind='bar', width=1, linewidth=0, color='darkred').set_xticklabels([])

    font = {'family': 'serif',
            'color': 'darkred',
            'weight': 'normal',
            'size': 14,
            }

    plt.xlabel('Ramos de Atuação', fontdict=font)
    plt.ylabel('Número de drones', fontdict=font)
    plt.title('Todas as atuações', fontdict=font)

    plt.subplots_adjust(bottom=0.5)

    plt.show()
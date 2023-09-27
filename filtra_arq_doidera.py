with open('arq_doidera_teste.txt', 'r') as f:
    str_dados = f.read()

separador = 'termina isso aqui'
list_dados = str_dados.split(separador)

# não me interessa o último elemento da lista apos o separador
# vou retirar o último elemento da lista
n = len(list_dados)
list_dados = list_dados[:n-1]
#print(list_dados)

# Tenho que pegar informações importantes. As informações devem permanecer
# em seus respectivos blocos, portanto, acredito que devo indexar os blocos
# para manter suas posições. Para essa tarefa seria importante criar um
# dicionário cuja chave seria o indexador do bloco e o valor poderia ser
# os dados do bloco. Após essa tarefa seria importante pergar informaçoes no
# bloco que são importantes para serem comparadas, o dado3 e o dado4.
# Essas informações também devem estar indexar a chave do dicionário. Logo
# os valores do dicionário podem ser tuplas com três posições, exemplo
# (dados_do_bloco, smille_dado3, energia_dado4)


# Tarefa 1: indexar os blocos
# Tarefa 2: pegar informações sensíveis dado3 e dado4
# Tarefa 3: adicionar dado3, dado4 e informação do bloco em uma tupla no
# dicionário.
dict_dados = {}
for i, dados in enumerate(list_dados):
    smille_dado3 = dados.split('dado3:')[1].split('#######')[0].strip()
    energia_dado4 = dados.split('dado4:')[1].split('#######')[0].strip()
    dict_dados[i] = (dados, smille_dado3, energia_dado4)

#print(dict_dados)

# Agora que já tenho minha estrutura de dados pronta, eu posso tentar comparar
# as informações para tratar os dados.
# O que eu quero é comparar o dado3 do indice 0 com o dado3 de todos os
# outros indices, se dado3[0] = dado3[n] então eu quero comparar o dado4 do
# indice 0 com o dado4 do indice n. Essas comparações apresentam como objetivo
# identificar o bloco de dados que desejo remover do dicionário.

# Tarefa 1: Encontrar os indices que devem ser removidos do dicionário.
# Tarefa 2: Adicionar esse indices em um conjunto (set) para que sejam removidos
# posteriormente.

comp_dict = len(dict_dados.keys())
#print(comp_dict)
#copia_dados = dict_dados.copy()
indices_a_serem_apagados = set()
for i in dict_dados.keys():
    smille = dict_dados[i][1]
    energia = float(dict_dados[i][2])
    #print(i, smille)
    print()
    for j in range(i+1, comp_dict):
        if smille == dict_dados[j][1] and i != j:
            print(f'{smille} == {dict_dados[j][1]}')
            print(f'i={i} j={j}')
            if energia > float(dict_dados[j][2]):
                print(f'{energia} i={i}')
                indices_a_serem_apagados.add(i)

            else:
                print(f'{dict_dados[j][2]} j={j}')
                indices_a_serem_apagados.add(j)

print(indices_a_serem_apagados)

# Agora que já tenho os indices a serem removidos em um conjunto, devo tentar
# remove-los do dicionário de dados.

for i in indices_a_serem_apagados:
    if i in dict_dados.keys():
        del dict_dados[i]

novos_dados = dict_dados.copy()
print(novos_dados)

# Agora podemos escrever os dados desse novo dicionário em um arquivo.

with open('novos_dados_doidera.txt', 'w') as f:
    for dados in novos_dados.values():
        print(dados[0], end='\n', file=f)

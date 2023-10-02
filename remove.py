import sys
from rdkit import Chem
from rdkit.Chem import MACCSkeys

def MACCS(h):
    mols = [Chem.MolFromSmiles(i) for i in h]
    keys = [MACCSkeys.GenMACCSKeys(mol) for mol in mols]
    bits = [key.ToBitString() for key in keys]

    return bits

def change_name(mol_2, new_name):

    with open(mol_2, 'r') as f:
        str_dados = f.read()

    separador = '     1 <0>         1 TEMP              0 ****  ****    0 ROOT'
    list_dados = str_dados.split(separador)

    # não me interessa o último elemento da lista apos o separador
    # vou retirar o último elemento da lista
    n = len(list_dados)
    list_dados = list_dados[:n-1]

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
    h = []
    e = []
    dict_dados = {}
    for i, dados in enumerate(list_dados):
        smille_dado3 = dados.split('RD_SMILES:')[1].split('##########')[0].strip()
        h.append(smille_dado3)
        energia_dado4 = dados.split('desc_Grid_vdw_energy:')[1].split('##########')[0].strip()
        e.append(energia_dado4)

    maccs_descriptor = MACCS(h)

    for key_m, n in enumerate(maccs_descriptor):
        for key_e, energia in enumerate(e):
            for key_l, dados in enumerate(list_dados):
                if key_m == key_l and key_e == key_l and key_l == key_m:
                    dict_dados[key_l] = (dados, smille_dado3, energia, n)

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
    indices_a_serem_apagados = set()
    for i in dict_dados.keys():
        smille = dict_dados[i][3]
        energia = float(dict_dados[i][2])
        for j in range(i+1, comp_dict):
            if smille == dict_dados[j][3] and i != j:
                if energia < float(dict_dados[j][2]):
                    indices_a_serem_apagados.add(i)
                else:
                    indices_a_serem_apagados.add(j)


    print(indices_a_serem_apagados)

    # Agora que já tenho os indices a serem removidos em um conjunto, devo tentar
    # remove-los do dicionário de dados.

    for i in indices_a_serem_apagados:
        if i in dict_dados.keys():
            del dict_dados[i]

    novos_dados = dict_dados.copy()

    # Agora podemos escrever os dados desse novo dicionário em um arquivo.

    with open(new_name, 'w') as f:
        for dados in novos_dados.values():
            print(dados[0], end='\n', file=f)

if __name__ == '__main__':
   if len(sys.argv) < 3:
        print("Usage: python Change_Name.py <MOL_2>")
   else:
        mol_2 = sys.argv[1]
        new_name = sys.argv[2]
        change_name(mol_2, new_name)

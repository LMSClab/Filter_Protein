import subprocess
import sys

def sub_process(proteins):

     primeiro = []
     segundo = []
     terceiro = []

     # listas de input's
     for n in proteins:
          first = n[0:4] + ".rename." + n[5:]
          primeiro.append(first)
          second = n[0:4] + ".clean." + n[5:]
          segundo.append(second)
          third = n[0:4] + ".delete." + n[5:]
          terceiro.append(third)
     
     # Run rename
     for key_n, n in enumerate(proteins):
          for key_m, m in enumerate(primeiro):
               if key_m == key_n:
                    subprocess.run(["python3.10", "change_name.py", n, m])
          

     # Run smiles
     for key_m, m in enumerate(primeiro):
               for key_n, n in enumerate(segundo):
                         for key_w, w in enumerate(terceiro):
                              if key_m == key_n and key_w == key_m:
                                   subprocess.run(["python3.10", "smiles.py", m, n, w])

     t = []

     with open(segundo[0], 'r') as f:
           protein_1 = f.read()
           t.append(protein_1)
     with open(segundo[1], 'r') as f:
           protein_2 = f.read()
           t.append(protein_2)
     with open(segundo[2], 'r') as f:
           protein_3 = f.read()
           t.append(protein_3)

     with open("all_proteins.mol2", 'w') as f:
        for dados in t:
            print(dados, end='\n', file=f)

     # Run harvest_data_xrescore
     subprocess.run(["python3.10", "harvest_data_xrescore.py", "all_proteins.mol2"])

     subprocess.run(["cp", "all_proteins.csv", "../{}".format(proteins[1][0:4], proteins[1][0:4])])
     subprocess.run(["cp", "all_proteins.csv", "../{}".format(proteins[2][0:4], proteins[2][0:4])])

if __name__ == '__main__':
   if len(sys.argv) < 1:
        print("Usage: python Change_Name.py <MOL_2>")
   else:        
        proteins = sys.argv[1:4]
        sub_process(proteins)
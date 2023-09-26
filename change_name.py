import sys
import random
import string

def change_name(mol_2, new_mol_2):

  with open(mol_2, 'r') as f:
     lines = f.readlines()

     name = []
     l = []
     tamanho=15
     intermed = []
     
     for n in lines:
          a = n.split(":")
          intermed.append(a)

     reduc = []

     for n in intermed:
          for i in n:
               reduc.append(i)
     
     for key, n in enumerate(reduc):
          if n == '##########                                Name':
               o = key + 1
               l.append(o)      

     for n in l:
          caracteres = string.ascii_letters + string.digits 
          nome = ''.join(random.choice(caracteres) for _ in range(tamanho))
          name.append(nome)
     
     w = 0
     
     for key, n in enumerate(reduc):
          if n == '##########                                Name':
               o = key + 1
               reduc[o] = "{}_DN_{}\n".format(mol_2[0:4],name[w])
               w = w + 1
     
     with open(new_mol_2, 'w') as f:
          for key, n in enumerate(reduc):
               if n[0:9] == '#########':
                    f.write("{}:".format(reduc[key]))
               else:     
                    f.write(n)

if __name__ == '__main__':
   if len(sys.argv) < 3:
        print("Usage: python Change_Name.py <MOL_2>")
   else:
        mol_2 = sys.argv[1]
        new_mol_2 = sys.argv[2]
        change_name(mol_2, new_mol_2)

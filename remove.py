import sys

def change_name(mol_2):

  with open(mol_2, 'r') as f:
     lines = f.readlines()

     intermed = []
    
     #print(lines)

     for n in lines:
          a = n.split(":")
          intermed.append(a)     
     
     #print(intermed)

     reduc = []

     for n in intermed:
          for i in n:
               reduc.append(i)
     
     #print(reduc)

     l = []

     for key, n in enumerate(reduc):
          if n == '##########                           RD_SMILES':
               o = key + 1
               l.append(o)
     
     #print(l)
     
     h = []

     for n in l:
          for m in l:
              if reduc[n] == reduc[m] and n != m:
                    print(reduc[n])
                    print(n)
                    print(reduc[m])
                    print(m)
                    h.append(n)
     print(h)
     
     x = 0
     score_1 = []
     score_2 = []
     
     for key, n in enumerate(reduc):
        if h[x] == key:
            score_1.append(reduc[key + 2])
     
     y = x + 1

     for key, n in enumerate(reduc):
        if h[y] == key:
            score_2.append(reduc[key + 2])    
     
     l_1 = []
     l_2 = []

     for n in score_1:
        n = n[10:-1]
        n = float(n)
        l_1.append(n)

     for n in score_2:
        n = n[10:-1]
        n = float(n)
        l_2.append(n)

     l_test = []

     for key_1, n in enumerate(l_1):
        for key_2, m in enumerate(l_2):
            if key_1 == key_2:
                if n < m:
                    l_test.append("score_1")
                else:
                    l_test.append("score_2")
     ''' 
     for n in l_test:
        if n == "score_1":
            for key, n in enumerate(reduc):
                if h[0] == key:
                    
        else:
            print(reduc[h[1]])

    
     print(l_test)
     '''
            
                  


if __name__ == '__main__':
   if len(sys.argv) < 2:
        print("Usage: python Change_Name.py <MOL_2>")
   else:
        mol_2 = sys.argv[1]
#        new_mol_2 = sys.argv[2]
        change_name(mol_2)

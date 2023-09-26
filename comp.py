import pandas as pd
import sys

def comp(DN, X):

    df_1 = pd.read_csv(DN, sep=',', header=None)
    df_2 = pd.read_csv(X, sep=',', header=None)
    
    l = []

    for key_DN, valor1 in enumerate(zip(df_1.iloc[:, -1])):
        for key_X, valor2 in enumerate(zip(df_2.iloc[:, -1])):
            if valor1 == valor2:
                results = pd.concat([df_1.iloc[key_DN], df_2.iloc[key_X]], ignore_index=True)
                l.append(results)
                print(results)
   
    d = pd.DataFrame(l)
    d.to_csv('novo_df.csv', index=False, header=False)

if __name__ == '__main__':
   if len(sys.argv) < 3:
        print("Usage: python Change_Name.py <DN>, <X>")
   else:
        DN = sys.argv[1]
        X = sys.argv[2]
        comp(DN, X)

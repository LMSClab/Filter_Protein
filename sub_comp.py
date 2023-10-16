import subprocess
import sys

def comp(re_re_scored):
    subprocess.run(["python3.10", "harvest_data_xrescore.py", re_re_scored])
    # Run comp
    subprocess.run(["python3.10", "comp.py", "all_proteins.csv", re_re_scored[:-4] + "csv"])

if __name__ == '__main__':
   if len(sys.argv) < 1:
        print("Usage: python Change_Name.py <MOL_2>")
   else:        
        re_re_scored = sys.argv[1]
        comp(re_re_scored)
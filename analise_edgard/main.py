import analise as an
import pandas as pd

def main():
    analise = pd.DataFrame(an.analise_completa())

    return analise
    
 
if __name__ == "__main__":
    main()
import analise as an
import pandas as pd

def main():
    """Roda a função analise_completa do arquivo analise.py, e depois converte o dicionario para um DataFrame"""
    analise =  an.analise_completa()
    print(analise)

    return analise
     
 
if __name__ == "__main__":
    main()
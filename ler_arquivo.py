import pandas as pd
import doctest as dt

def ler_arquivo_csv (nome_arquivo):
    """
    Função para ler arquivos do tipo CSV e transformar em DataFrame Pandas.

    Parameters
    ----------
    nome_arquivo : string
        Nome do arquivo .csv, que deve estar na mesma pasta. Também é possível fornecer o caminho do arquivo, caso esteja em outra pasta.

    Returns
    -------
    df : DataFrame
        Retorna um DataFrame com os dados do arquivo.
        
    Exemplo
    -------
    >>> ler_arquivo_csv ("teste.csv")
      Teste  num
    0     a    1

    """
    df = pd.read_csv(nome_arquivo, sep = ";", encoding = "latin-1", on_bad_lines="skip", low_memory=False)
    
    return df

if __name__ == "__main__":
    dt.testmod()
    dt.testmod(verbose=True)
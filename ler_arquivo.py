import pandas as pd
import doctest as dt

def ler_arquivo_csv(nome_arquivo: str) -> pd.DataFrame:
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
    try:
        df = pd.read_csv(nome_arquivo, sep = ";", encoding = "latin-1", on_bad_lines="skip", low_memory=False)
    except FileNotFoundError: 
        print(f'Arquivo "{nome_arquivo}" não Encontrado! Veja se não errou o nome dele!')
    else:
        return df

if __name__ == "__main__":
    dt.testmod(verbose=True)
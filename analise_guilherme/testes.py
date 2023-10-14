import unittest
import doctest
import pandas as pd
import clean_columns as cc 

class TestFuncoes(unittest.TestCase):

    # Testa a função filter columns
    def test_filter_columns(self):
        # Gera um df exemplo
        df = pd.DataFrame({"Numero": [13, 22], "Nome": ["Lula", "Bolsonaro"]})
        colunas_selecionadas = ["Numero"]
        # Utiliza a função filter columns e obtém um resultado
        resultado = cc.filter_columns(df, colunas_selecionadas)
        esperado = pd.DataFrame({"Numero": [13, 22]})
        # Compara o resultado e o esperado, com assert equal
        self.assertEqual(resultado.to_dict(), esperado.to_dict())

    # Testa a função sum columns
    def test_sum_columns(self):
        # Gera um df exemplo
        df = pd.DataFrame({"Aluno": ["Gui", "Ale"], "Faltas": [7, 1]})
        # Utiliza a função sum columns e obtém um resultado
        resultado = cc.sum_columns(df)
        esperado = pd.Series({"Aluno": "GuiAle", "Faltas": 8})
        # Compara o resultado e o esperado, com assert equal
        self.assertEqual(resultado.to_dict(), esperado.to_dict())

if __name__ == '__main__':
    unittest.main()

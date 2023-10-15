import unittest
import pandas as pd
import funcoes_uteis as fu

class Testes(unittest.TestCase):
    df = pd.DataFrame({"Alunos": ["Alessandra", "Guilherme Ferrari", "Edgard", "Jeann"],
                       "Curso": ["Ciencia de Dados", "Matemática Aplicada", "Matemática Aplicada","Matemática Aplicada"],
                        "Dado1": [-5, 12, 3, 9],
                        "Dado2": [12, 0, 99, -18],
                        "Dado3": [100, 999, 13, -34],
                        "Dado4": [12, 12, 0, 45],
                        "Dado5": [1000, 0, 0, -102],
                        "Dado6": [-5, -4, -3, 2],
                        "Dado7": [10, 10, 10, 10]}) # dataframe base para os testes que serão feitos


    def test_escolhe_colunas(self):
        # teste para a função escolhe_colunas
        result = pd.DataFrame({"Alunos": ["Alessandra", "Guilherme Ferrari", "Edgard", "Jeann"],
                       "Curso": ["Ciencia de Dados", "Matemática Aplicada", "Matemática Aplicada","Matemática Aplicada"],
                        "Dado1": [-5, 12, 3, 9],
                        "Dado2": [12, 0, 99, -18],
                        "Dado3": [100, 999, 13, -34],
                        "Dado4": [12, 12, 0, 45],
                        "Dado5": [1000, 0, 0, -102]})
        value = fu.escolhe_colunas(self.df, ["Alunos", "Curso", "Dado1", "Dado2", "Dado3", "Dado4", "Dado5"])
        self.assertTrue(result.equals(value))
    
    def test_agrupa_por_sum(self):
        # teste para a função agrupa_por_sum
        result = pd.DataFrame({"Dado1": [-5, 24], "Dado2": [12, 81], "Dado3": [100, 978], "Dado4": [12, 57], "Dado5": [1000, -102]},
                              index=["Ciencia de Dados", "Matemática Aplicada"])
        result.index.name = "Curso"
        
        value = fu.agrupa_por_sum(self.df, "Curso", ["Dado1", "Dado2", "Dado3", "Dado4", "Dado5"])
        self.assertTrue(result.equals(value))

    def test_agrupa_por_cont(self):
        # teste para a função agrupa_por_cont
        result = pd.DataFrame({"Dado1": [1, 3], "Dado2": [1, 3], "Dado3": [1, 3], "Dado4": [1, 3], "Dado5": [1, 3]},
                              index=["Ciencia de Dados", "Matemática Aplicada"])
        result.index.name = "Curso"
        
        value = fu.agrupa_por_cont(self.df, "Curso", ["Dado1", "Dado2", "Dado3", "Dado4", "Dado5"])
        self.assertTrue(result.equals(value))

    def test_agrupa_por_proporcao(self):
        # teste para a função agrupa_por_proporcao
        result = pd.DataFrame({"Dado1": [-5., 8.], "Dado2": [12., 27.], "Dado3": [100., 326.], "Dado4": [12., 19.], "Dado5": [1000., -34.]},
                              index=["Ciencia de Dados", "Matemática Aplicada"])
        result.index.name = "Curso"
        
        value = fu.agrupa_por_proporcao(self.df, "Curso", ["Dado1", "Dado2", "Dado3", "Dado4", "Dado5"])
        self.assertTrue(result.equals(value))

    def test_dados_descritivos(self):
        # teste para a função dados_descritivos
        result = pd.DataFrame({"Dado1": [-5., 24., 9.5, 9.5, 20.506096654409877] , "Dado2": [12., 81., 46.5, 46.5, 48.79036790187178],
                               "Dado3": [100., 978., 539, 539, 620.8397538817887], "Dado4": [12., 57., 34.5, 34.5, 31.81980515339464],
                               "Dado5": [-102., 1000., 449., 449., 779.2316728675754]},
                              index=["MINIMO", "MAXIMO", "MEDIA", "MEDIANA", "DESVIO PADRAO"])
        
        value = fu.dados_descritivos(self.df, "Curso", ["Dado1", "Dado2", "Dado3", "Dado4", "Dado5"])
        self.assertTrue(result.equals(value))


if __name__ == '__main__':
    unittest.main()
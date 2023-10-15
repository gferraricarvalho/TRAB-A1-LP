import unittest
import pandas as pd
import visualizacao as vl

class MyTestOrganiza(unittest.TestCase):
    def teste_organiza_df(self):
        df = pd.DataFrame({'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],'Idade': [25, 30, 28, 35, 22],'Sexo':['F','M','F','M','F']})
        resultado = pd.DataFrame([['Alice', 25,'F'],['Bob', 30,'M'],['Carol', 28,'F'],['David', 35,'M'],['Eve', 22,'F']])

        # Converta os DataFrames em listas
        df_list = df.to_numpy().tolist()
        resultado_list = resultado.to_numpy().tolist()

        # Compare as listas
        self.assertEqual(df_list, resultado_list)
    
class MYtestCalculaEstatisticas(unittest.TestCase):
    def teste_estatisticas(self):
        #calculando as estatisticas 
        df = vl.calcular_estatisticas(pd.DataFrame({'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],'Poupança': [2500, 3000, 2800, 3500, 2200]}))
        resultado = [[5.0],[2800.0],[494.9747468305833],[2200.0],[2500.0],[2800.0],[3000.0],[3500.0]]
        df_list = df.to_numpy().tolist()

        self.assertEqual(df_list, resultado) # comparando os resultados

class MyTestEncontraValorMax(unittest.TestCase):
    def test_encontra_maximo(self):
        #Aqui a função encontra qual dos 5 possue mais dinheiro na poupança
        resultado = vl.encontrar_max(pd.DataFrame({'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],'Poupança': [2500, 3000, 2800, 3500, 2200]}),'Poupança','Nome')
        esperado = ['David']
        
        self.assertEqual(resultado, esperado)

class MyTestContagemFrequencia(unittest.TestCase):
    def test_conta_frequencia(self):
        #contando a frequência com que cada nome aparece
        df = vl.freq_contagem(pd.DataFrame({'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Alice']}), 'Nome')
        resultado = [2, 1, 1, 1, 1]

        # Converta os DataFrames em listas
        df_list = df.to_numpy().tolist()

        self.assertEqual(df_list, resultado)#comparando os resultados


if __name__ == "__main__":
    unittest.main()
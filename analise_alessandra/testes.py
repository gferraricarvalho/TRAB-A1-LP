import unittest
import funcoes_selecao as fs
import pandas as pd
import pandas.testing as pd_testing

#testando a função selecionar colunas
class MyTest_selecionar_colunas(unittest.TestCase):
    #usando o modulo assert_frame_equal para comparar DataFrames
    def assertDataframeEqual(self,atual,esperado, msg):
        try:
            pd_testing.assert_frame_equal(atual, esperado)
        except AssertionError as e:
            raise self.failureException(msg) from e

    #adicionando DataFrame no AssertEqual       
    def setUp(self):
        self.addTypeEqualityFunc(pd.DataFrame, self.assertDataframeEqual)
    
    #testando a função com um exemplo qualquer
    def test_allZero(self):
        df = pd.DataFrame({"nome":["Alessandra", "Guilherme", "Jeann", "Edgard"], "Idade": [20, 21, 18, 19]})
        atual = fs.selecionar_colunas(df, "Idade")
        esperado = pd.DataFrame({"Idade": [20, 21, 18, 19]})
        self.assertEqual(atual, esperado)
        
#testando a função trocar valor        
class MyTest_trocar_valor(unittest.TestCase):
    #usando o modulo assert_frame_equal para comparar DataFrames
    def assertDataframeEqual(self,atual,esperado, msg):
        try:
            pd_testing.assert_frame_equal(atual, esperado)
        except AssertionError as e:
            raise self.failureException(msg) from e
    
    #adicionando DataFrame no AssertEqual  
    def setUp(self):
        self.addTypeEqualityFunc(pd.DataFrame, self.assertDataframeEqual)
    
    #testando a função com um exemplo qualquer
    def test_allZero(self):
        df = pd.DataFrame({"nome":["Alessandra", "Guilherme", "Jeann", "Edgard"], "Idade": [20, 21, 18, 19]})
        atual = fs.trocar_valor(df, "Idade", {20: "Vinte", 21: "Vinte e Um", 18: "Dezoito", 19: "Dezenove"})
        esperado = pd.DataFrame({"nome":["Alessandra", "Guilherme", "Jeann", "Edgard"],"Idade": ["Vinte", "Vinte e Um", "Dezoito", "Dezenove"]})
        self.assertEqual(atual, esperado)
        
if __name__ == '__main__':
    unittest.main()
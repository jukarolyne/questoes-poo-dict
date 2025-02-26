class Televisao:
    '''A classe Televisao tem os metodos ligar e desligar a tv, mudar de canal e 
    tem os atributos tamanho e marca'''
    def __init__(self, canalMin=2, canalMax=14, canal=0, ligada=False):
        self.tamanho = None
        self.marca = None
        self.ligada = ligada
        self.canal = canal
        self.canalMin = canalMin
        self.canalMax = canalMax
    
    def cima(self):
        '''funcao seta em 1 para um canal mais acima'''
        if self.ligada == True:
            if self.canal + 1 <= self.canalMax:
                self.canal += 1
            else:
                self.canal = self.canalMin
            return print(self.canal)
        else:
            return print(self.ligada)

    def baixo(self):
        '''funcao seta em 1 para um canal mais abaixo'''
        if self.ligada == True:
            if self.canal - 1 >= self.canalMin:
                self.canal -= 1
            else:
                self.canal = self.canalMax
            return print(self.canal)
        else:
            return print(self.ligada)

class ControleRemoto:
    def __init__(self, televisao):
        self.televisao = televisao
    
    def liga(self):
        self.televisao.ligada = True
        return self.televisao.ligada
    
    def desliga(self):
        self.televisao.ligada = False
        return self.televisao.ligada
    
    def btn_mais(self):
        self.televisao.cima()
        return self.televisao.canal

    def btn_menos(self):
        self.televisao.baixo()
        return self.televisao.canal
    
tv = Televisao(2, 10, 2)
controle = ControleRemoto(tv)

print(tv.canal)
controle.liga()
print(tv.ligada)
controle.btn_mais()
controle.btn_mais()
controle.btn_mais()
controle.desliga()
controle.btn_menos()
print(tv.canal)
controle.liga()
controle.btn_menos()

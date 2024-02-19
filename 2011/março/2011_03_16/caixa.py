class ValorNaoPermitido(Exception):
    pass

class Caixa(object):
    notas = [100, 50, 20, 10]
    
    def valor_e_permitido(self, valor):
        return valor % 10 != 0 or valor < 1

    def sacar(self, valor):
        if self.valor_e_permitido(valor):
            raise ValorNaoPermitido
            
        saque = []
        
        for nota in self.notas:
            while valor >= nota:
                valor = valor - nota
                saque.append(nota)
                
        return saque
           
    def como_dicionario(self, notas_sacadas):
        notas_dict = {} 
        
        for nota in self.notas:
            if nota in notas_sacadas:
                notas_dict[nota] = notas_sacadas.count(nota)
               
        return notas_dict

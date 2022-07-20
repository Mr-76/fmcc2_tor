
class Cliente:
    def __init__(self, mensagem):
        self._mensagem = mensagem
        self._mensagem_encrypt = "" # por enquato
    def encrypt(self):
        chave1 = 1 #chave 1
        chave2 = 2 #chave 2
        chave3 = 3 #chave 3
        self._mensagem_encrypt = self._mensagem + str(chave1)#encripta 1 vez e armazena chave 
        self._mensagem_encrypt = self._mensagem_encrypt+ str(chave2)#encripta 2 vez e armazena chave 
        self._mensagem_encrypt = self._mensagem_encrypt + str(chave3)#encripta 3 vez e armazena chave 
        #print("debug encryptdador")

        #print(self_mensagem_encrypt)
        return (chave3,chave2,chave1)

    def send(self,nodo):#nodos tb tem esse metodo
        nodo.decrypt(self._mensagem_encrypt)
        

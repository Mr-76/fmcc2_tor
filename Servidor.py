class Servidor:
    def __init__(self):
        self._mensagem = "" # por enquato


    def receive(self,mensagem):#nodos tb tem esse metodo
        self._mensagem = mensagem

    def print_msg(self):
        print("mensagem recebida")
        print(self._mensagem)

from cryptography.fernet import Fernet

class Nodo:
    """Nodo."""

    def __init__(self,chave):
        """__init__.

        :param chave:
        """
        self._chave = chave
        self._mensagem = "" # por enquato

    def decrypt(self,mensagem):
        """decrypt.

        :param mensagem:
        """
        self._mensagem = self._chave.decrypt(mensagem) #decrypt a mensagem

    def send(self,nodo):#nodos tb tem esse metodo
        """send.

        :param nodo:
        """
        nodo.decrypt(self._mensagem)
 
    def print_msg(self):
        """print_msg."""
        return self._mensagem
    def send_server(self,server):
        """send_server.

        :param server:
        """
        print("mandando para servidor")
        server.receive(self._mensagem)

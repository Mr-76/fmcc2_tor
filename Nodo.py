from cryptography.fernet import Fernet


class Nodo:
    """Nodo."""

    def __init__(self, chave):
        """__init__.

        Construtor do objeto Nodo.

        :param chave:Chave para desencriptar uma
                      mensagem.
        """
        self._chave = chave
        self._mensagem = ""  # por enquato

    def decrypt(self, mensagem):
        """decrypt.

        Metodo desencripta a mensagem
        com uma chave.

        :param mensagem: Mensagem a desencriptar.
        """
        self._mensagem = self._chave.decrypt(mensagem)

    def send(self, nodo):
        """send 
        Metodo manda a mensagem para
        um objeto do tipo Nodo.

        :param nodo: Objeo nodo.
        """
        nodo.decrypt(self._mensagem)

    def print_msg(self):
        """print_msg.
        metodo retorna a mensagem do nodo
        :return: String com mensage de uma nodo.
        """
        return self._mensagem

    def send_server(self, server):
        """send_server.
        Metodo manda a mensagem que o
        nodo possui para um objeto
        servidor.

        :param server: Objeto servidor
        """
        print("mandando para servidor")
        server.receive(self._mensagem)

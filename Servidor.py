class Servidor:
    """Servidor.
    Objeto servidor que recebe mensagens.
    """

    def __init__(self):
        """__init__.
        Contrutor do objeto Servidor.
        """
        self._mensagem = ""

    def receive(self, mensagem):
        """receive.
        Metodo recebe uma mensagem e
        a armazenada.

        :param mensagem:
        """
        self._mensagem = mensagem

    def print_msg(self):
        """print_msg.
        Metodo retorna para o usuario
        a mensagem armazenada no Objeto
        Servidor.

        """
        print("mensagem recebida")
        print(self._mensagem.decode())

class Servidor:
    """Servidor."""

    def __init__(self):
        """__init__."""
        self._mensagem = "" # por enquato


    def receive(self,mensagem):#nodos tb tem esse metodo
        """receive.

        :param mensagem:
        """
        self._mensagem = mensagem

    def print_msg(self):
        """print_msg."""
        print("mensagem recebida")
        print(self._mensagem.decode())

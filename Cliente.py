from cryptography.fernet import Fernet

class Cliente:
    """Cliente."""

    def __init__(self, mensagem):
        """__init__.

        :param mensagem:
        """
        self._mensagem = mensagem
        self._mensagem_encrypt = ""  
    def encrypt(self):
        """encrypt."""

        chave1 = Fernet.generate_key()
        chave1 = Fernet(chave1)

        chave2 = Fernet.generate_key()
        chave2 = Fernet(chave2)

        chave3 = Fernet.generate_key()
        chave3 = Fernet(chave3)

        self._mensagem_encrypt = chave1.encrypt(self._mensagem.encode()) 

        self._mensagem_encrypt = chave2.encrypt(self._mensagem_encrypt) 

        self._mensagem_encrypt = chave3.encrypt(self._mensagem_encrypt)

        return (chave3,chave2,chave1)

    def send(self,nodo):
        """send.

        :param nodo:
        """
        nodo.decrypt(self._mensagem_encrypt)
        

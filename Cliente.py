from cryptography.fernet import Fernet


class Cliente:
    """Cliente.
    Objeto Cliente que tem uma mensagem
    encripta essa mensagem,pode retornar
    as chaves de encriptacao,e mandar a
    mensagem encriptada para um objeto do
    tipo Nodo.

    """

    def __init__(self, mensagem):
        """__init__.

        Construtor do objeto Cliente,
        que recebe uma mensagem inicial
        nao encriptada.

        :param mensagem: String mensagem que
                         um cliente possui.
        """
        self._mensagem = mensagem
        self._mensagem_encrypt = ""

    def encrypt(self):
        """encrypt.
        Metodo enripta uma mensagem tres vezes
        e retorna as chaves de cada encriptacao.

        """

        chave1 = Fernet.generate_key()
        chave1 = Fernet(chave1)

        chave2 = Fernet.generate_key()
        chave2 = Fernet(chave2)

        chave3 = Fernet.generate_key()
        chave3 = Fernet(chave3)

        self._mensagem_encrypt = chave1.encrypt(self._mensagem.encode())

        self._mensagem_encrypt = chave2.encrypt(self._mensagem_encrypt)

        self._mensagem_encrypt = chave3.encrypt(self._mensagem_encrypt)

        return (chave3, chave2, chave1)

    def send(self, nodo):
        """send.

        Metodo manda uma mensagem ja encriptada,
        para um nodo.

        :param nodo: Objeto tipo nodo.
        """
        nodo.decrypt(self._mensagem_encrypt)

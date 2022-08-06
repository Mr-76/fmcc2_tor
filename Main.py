from Cliente import Cliente
from Nodo import Nodo
from Servidor import Servidor


def main():
    mensagem = input("Digite a mensagem que quer mandar ")
    servidor = Servidor()
    cliente = Cliente(mensagem)

    chaves = tuple(cliente.encrypt())  #Armazenando chaves de encriptacao

    #Associando as chaves de encriptacao aos nodos.
    nodo1 = Nodo(chaves[0])
    nodo2 = Nodo(chaves[1])
    nodo3 = Nodo(chaves[2])

    print("Chave 3", chaves[0])
    print("Chave 2", chaves[1])
    print("Chave 1", chaves[2])

    #Mandando a mensagem do cliente ate o servidor.
    cliente.send(nodo1)  #mensagem para nodo1.
    nodo1.send(nodo2)  #mensagem para nodo2.
    nodo2.send(nodo3)  #mensagem para nodo3.
    nodo3.send_server(servidor)  # mensagem para servidor.
    servidor.print_msg()


main()

from Cliente import Cliente
from Nodo import Nodo
from Servidor import Servidor


def main():
    servidor = Servidor()
    cliente = Cliente("Hello world")
    chaves = tuple(cliente.encrypt())
    nodo1 = Nodo(chaves[0])  
    nodo2 = Nodo(chaves[1])  
    nodo3 = Nodo(chaves[2])

    cliente.send(nodo1)#1 cahve
    nodo1.send(nodo2)#2 chave
    nodo2.send(nodo3)#3 chave
    nodo3.send_server(servidor)
    servidor.print_msg()
main()

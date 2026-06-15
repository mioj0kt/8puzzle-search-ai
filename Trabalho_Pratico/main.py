from puzzle.estados import Estado
from algorithms.bfs import BFS

def montar_tabuleiro():
    print("Digite os números do tabuleiro separados por espaço:")
    entrada = input("Tabuleiro: ")

    numeros = list(map(int, entrada.split()))

    if len(numeros) != 9:
        raise ValueError("O tabuleiro deve possuir exatamente 9 números.")
    
    return Estado(numeros)

def menu():
    print("\n===== 8 PUZZLE =====\n")

    print("Escolha o algoritmo:")

    print("1 - BFS")
    print("2 - DFS")
    print("3 - Busca Uniforme")
    print("4 - Busca Gulosa")
    print("5 - A*")
    print("\n0 - Sair")

    return int(input("\nOpcao: "))

def mostrar_caminho(caminho):
    for i, no in enumerate(caminho):
        print(f"Passo {i}")
        if no.movimento:
            print("Movimento:", no.movimento)

        print(no.estado)

def main():
    estado_inicial = montar_tabuleiro()
    opcao = menu()

    if opcao == 1:

        solucao, nos_visitados = BFS.buscar(estado_inicial)

        if solucao:

            caminho = BFS.reconstruir_caminho(solucao)

            mostrar_caminho(caminho)

            print("\n===== ESTATÍSTICAS =====")

            print("Nós visitados:", nos_visitados)
            print("Profundidade:", solucao.profundidade)

        else:

            print("Solução não encontrada.")

    elif opcao == 2:
        print("DFS ainda não implementado.")

    elif opcao == 3:
        print("Busca Uniforme ainda não implementada.")

    elif opcao == 4:
        print("Busca Gulosa ainda não implementada.")

    elif opcao == 5:
        print("A* ainda não implementado.")

    elif opcao == 0:
        print("Saindo do programa...")
        return

    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
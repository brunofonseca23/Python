print("Questão 1 \n")

def menu():
    print(35 * "=")
    print("Menu de opções")
    print("0 - Encerrar o programa")
    print("1 - Buscar aluno no sistema")
    print(35 * "=")

def ler_arquivo():
    lista = []
    with open("relatorio.csv","r",encoding="utf-") as bd:
        bd.readline()
        for linhas in bd:
            linha = linhas.strip().split(";")
            lista.append(linha)
    return lista



def ler_num(inteiro):
    while True:
        try:
            inte = int(input(inteiro))
            return inte
        except ValueError:
            print("Digite um valor válido!")


def mostrar_aluno(result):
    print(35 * "=")
    print("Nome do aluno: ",result[4])
    print("Matrícula: ",result[7])
    print("Curso: ",result[6])
    print("Situação: ",result[3])
    print(35 * "=")
     
        


def main():
    banco_de_dados = ler_arquivo()
    while True:
        menu()
        opcao = ler_num("O que deseja fazer? ")
        if opcao == 0:
            for c in banco_de_dados:
                mostrar_aluno(c)
        elif opcao == 1:
            mat = input("Digite o número da matrícula: ")
            result = None
            
            for c in banco_de_dados:
                
                if mat == c[7]:
                    result = c
                    break

                if result is None:
                    print("Matrícula não encontrada...")
                else:
                    mostrar_aluno(result)           
            
        else:
            print("Digite uma opção válida!")




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Usuário encerrou o programa...")
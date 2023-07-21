def menu():
    print(35 * "=")
    print("Menu principal: ")
    print("0 - Sair do programa")
    print("1 - Buscar personalizada")
    print(35 * "=")

def abrir_arq():
    banco_de_dados = []
    with open("servidores.csv","r",encoding="utf-8") as arq:
        arq.readline()
        for c in arq:
            linha = c.strip().split(";")
            banco_de_dados.append(linha)
    return banco_de_dados

def ler_num(inteiro):
    while True:
        try:
            inte = int(input(inteiro))
            return inte
        except ValueError:
            print("Digite um valor válido!")


def mostrar_resultado(info):
    print(35 * "=")
    print("Disciplina:", info[3])
    print("Campus:", info[11])
    print("Servidor:", info[5])
    print("Matrícula:", info[9])
    print(35 * "=")
    

def main():
    bd = abrir_arq()
    while True:
        menu()
        opcao = ler_num("Digite uma opção: ")
        
        if opcao == 0:
            print("Encerrando o programa...")
            break
        elif opcao == 1:
            result = None
            nome = str(input("Digite o nome da disciplina: ")).capitalize()
            campi = str(input("Digite o nome do campus: ")).capitalize()
            
            for linhas in bd:
                if nome == linhas[3].capitalize() and campi == linhas[11].capitalize():
                    result = linhas 
            
            if result is None:
                print("Registro não encontrado!") 
    
            else:
                mostrar_resultado(result)   
        else:
            print("Opção inválida, tente novamente...")

try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("Usuário preferiu encerrar o programa... ")
    
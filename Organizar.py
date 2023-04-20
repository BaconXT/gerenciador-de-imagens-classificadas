import os
import shutil

PastaOrigem = "C:\\Users\\AN1\\Downloads"

PastaDestino = "C:\\Users\\AN1\\Python\\Aula102\\Arquivos"

ListarArquivos = os.listdir(PastaOrigem)

# print(ListarArquivos)

for nome_arquivo in ListarArquivos:
    nome, extensao = os.path.splitext(nome_arquivo)
    #print(nome)
    #print(extensao)

    if extensao == '':
        continue

    if extensao in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        caminho1 = PastaOrigem + '/' + nome_arquivo
        caminho2 = PastaDestino + '/' + "arquivos_imagem"
        caminho3 = PastaDestino + '/' + "arquivos_imagem" + '/' + nome_arquivo


        print("caminho1 " , caminho1)
        print("caminho3 ", caminho3)


        if os.path.exists(caminho2):
            print("Movendo " + nome_arquivo + "...")

            shutil.move(caminho1, caminho3)

        else:
            os.makedirs(caminho2)
            print("Movendo " + nome_arquivo + "...")

            shutil.move(caminho1, caminho3)
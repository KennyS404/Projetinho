import os
import time
flag = []
vagas = []
for i in range (3):
    vagas.append([0] * 3)
while (True):
    operacao = input('''Selecione abaixo\n [1] Mostrar vagas \n [2] Mostrar vagas livres \n [3] ocupar vagas \n [4] Liberar vagas \n [5] resumo das vagas \n [6] Mostrar as somas das vagas ocupadas por linha \n [7] Mostrar as somas das vagas ocupadas por coluna \n [8] sair \n ''')
    os.system('clear')
    
    if operacao == '1':
        armario = 0 
        for linha in range (3):
           for coluna in range (3):
               armario = armario + 1
               if vagas[linha][coluna] == 0:
                   print("Armario %d livre."%(armario))
               else:
                   print("Armario %d ocupado"%(armario))
            
        
    elif operacao == '2':   
        armario = 0
        for linha in range (3):
           for coluna in range (3):
               armario = armario + 1
               if vagas[linha][coluna] == 0:
                   print("Armario %d livre."%(armario))
                   
    elif operacao == '3':
        vaga_a_ocupar = int(input("Informe o armário a ocupar: "))
        armario = 0
        for linha in range (3):
            for coluna in range (3):
                armario = armario + 1 
                
                if armario == vaga_a_ocupar:
                    if vagas[linha][coluna] == 0:
                        vagas[linha][coluna] = 1
                        print("Vaga ocupada com sucesso")
                    else:
                        print("Esse armário já está ocupado, escolha outro pls")
   

    elif operacao == '4':
        vaga_a_desocupar = int(input("Informe o armário a desocupar: "))
        armario = 0
        for linha in range (3):
            for coluna in range (3):
                armario = armario + 1 
                
                if armario == vaga_a_desocupar:
                    if vagas[linha][coluna] == 1:
                        vagas[linha][coluna] = 0
                        print("Vaga desocupada com sucesso")
                    else:
                        print("Esse armário já está desocupado, escolha outro pls")
   
        
    elif operacao == '5':
        soma_vagas_livres = 0
        soma_vagas_ocupadas = 0
        for linha in range (3):
            for coluna in range (3):
                if vagas[linha][coluna] == 0:
                    soma_vagas_livres = soma_vagas_livres + 1
                else:
                    soma_vagas_ocupadas = soma_vagas_ocupadas + 1
        print("Existem %d armários livres e existem %d armários ocupados"%(soma_vagas_livres,soma_vagas_ocupadas))    
        
        
    elif operacao == '6':
        linha1 = 0
        for linha in range (3):
            linha1 = linha1 + 1
            vagas_ocupadas_por_linha = 0
            for coluna in range (3):
                if vagas[linha][coluna] == 1:
                    vagas_ocupadas_por_linha = vagas_ocupadas_por_linha + 1 
            print("A linha %d possui %d armários ocupados"%(linha1,vagas_ocupadas_por_linha))
            
    elif operacao == '7':
        
        vagas_colunas1 = 0
        vagas_colunas2 = 0
        vagas_colunas3 = 0
        for linha in range (3):
            colunai = 0
            for coluna in range (3):
                colunai = colunai + 1
                if vagas[linha][coluna] == 1:
                    if colunai == 1:
                        vagas_colunas1 = vagas_colunas1 + 1
                    elif colunai == 2:
                        vagas_colunas2 = vagas_colunas2 + 1 
                    else:
                        vagas_colunas3 = vagas_colunas3 + 1 
        
                        
        print("A coluna 1 possui %d armários ocupados \nA coluna 2 possui %d armários ocupado \nA coluna 3 possui %d armários ocupados  "%(vagas_colunas1,vagas_colunas2,vagas_colunas3))            
    elif operacao == '8':
        break
    else:
        print("Opcão inválida, digite novamente")
# Criando arrays para usar nas funcoes. 

mediana_array = []
amplitude_array = []
variancia_array = []

#importando as bibliotecas calculos.
import os
from statistics import *
import numpy as np

# exibindo o menu de escolhas das funcionalidades.

print("       Unimetrocamp | Wyden             ")
print("										   ")
print('           000000000000                 ')
print('          00        00                  ')
print('          00       00                   ')
print('          00        00                  ')
print('          00         00                 ')
print('          00          00                ')
print(' 									   ')
print(' 00000000     00000000     00000000	   ')
print('  00    00     00    00     00    00	   ')
print('   00    00     00    00     00    00   ')		
print('    00    00     00    00     00    00  ')
print('     00    00     00    00     00    00 ')
print('      00    00     00    00     00 00   ')
print('       00    00     00    00     00     ')
print('        00    00     00    00           ')
print('         00    00     00    00          ')
print('          00 00        00 00            ')
print('           00           00              ') 
   
print("\n Nome do sistema: Projeto de Estudo Dirigido\n")

print("\n")
print("MENU (Escolha das funcionalidades)\n\n")

print("1 - Estatistica \n")
print("2 - Historia da universidade \n")   
print("3 - Desenvolvedores do Sistema \n")    
print("4 - sair \n")   

opcao_funcionalidades = input("Digite a opcao:")

menu = menu()
estatistica = estatistica()
desenvolvedoresSistema = desenvolvedoresSistema()
historiaUniversidade = historiaUniversidade()

# Criando menu de opcoes para a chamada da funcionalidade. 
def menu(opcao_funcionalidades): 
	if(opcao_funcionalidades == 1 ):
	    estatistica()

	if(opcao_funcionalidades == 2 ):
	    historiaUniversidade()
	    
	if(opcao_funcionalidades == 3 ):
	    desenvolvedoresSistema()

	if(opcao_funcionalidades == 4 ):
	    print("\n Ate logo!")  

	else:
		print("Opção invalida")

	#os.system("pause")

#Criando funcao de estatisticas para os calculos dentro as opcoes. 
def estatistica():
	print("MENU \n")
	print("Escolha a funcao:\n\n")  
	print("1 - Media Aritmetica \n") 
	print("2 - Media Ponderada \n")
	print("3 - Mediana \n")
	print("4 - Amplitude \n")
	print("5 - Variancia \n")
	print("6 - Voltar para o menu principal \n")    

	opcao_estatistica = input("Digite a opcao do menu acima: ")

	#fazendo as chamadas das funcoes

	if int(opcao_estatistica) > 0 or int(opcao_estatistica) < 7:
		if(opcao_estatistica == 1):
			mediaAritmetica =  mediaAritmetica()
     
		if(opcao_estatistica == 2):
			mediaPonderada = mediaPonderada()

		if(opcao_estatistica == 3):
			mediana = mediana()

		if(opcao_estatistica == 4):
			amplitude = amplitude()

		if(opcao_estatistica == 5):
			variancia = variancia()

		if(opcao_estatistica == 6):
			return()
	else:
		print("Opção invalida")

	#os.system("pause")

#criando funcao para mostrar os desenvolvedores
def desenvolvedoresSistema():
    print(" Desenvolvedores do sistema: \n")            
    print(" Copyright Erro #404 Brasil©. Todos os direitos reservados. ") 
    #os.system("pause")

#criando funcao para mostrar a historia da universidade
def historiaUniversidade():
	print(" Historia da Universidade \n")    
	print("A Wyden é uma instituição de ensino superior parte de um dos maiores grupos educacionais do mundo, a Adtalem Global Education, que oferece, qualidade internacional e experiência em transformar realidades por meio da educação no mundo inteiro. Oferecemos cursos de Graduação e Pós-Graduação nas modalidades presencial, semipresencial e à distância. \n O UniMetrocamp | Wyden, em Campinas, oferece a você mais de 60 cursos, entre Graduação e Pós-Graduação. Em 2017, foi apontada, pelo IGC, como a melhor de Campinas, além de ter 7 cursos avaliados, pelo Enade, como os melhores da cidade. \n História no Brasil \n Um dos maiores grupos educacionais do mundo, a Adtalem Global Education chegou ao Brasil em 2009 para trazer uma educação de qualidade internacional e junto com o talento brasileiro empoderar seus alunos a conquistar seus objetivos profissionais. \n Atualmente, a Adtalem Educacional do Brasil tem 13 instituições de ensino superior distribuídas pelo território nacional. Sendo, ao todo, 16 campi em todo o País, ofertando cursos de graduação e pós-graduação a mais de 124 mil alunos. \n")
	#os.system("pause")

#criando funcao para calcular a media aritmetica.
def mediaAritmetica():
    print("\n  Calculo da Media Artimetia  \n ")
    print("Obs: permite a entrada de apenas 10 valores")
    quant_Pesos = 0
    soma = 0

    while (opcao_mediaAritmetica == 's'):
	    if quant_Pesos < 10:
	     
	    	peso = input("Digite o peso: \n")
	         
	    	soma = soma + peso
	    	quant_Pesos = quant_Pesos + 1
	    	
	    	opcao_mediaAritmetica = input("Deseja incluir outro peso? Digite 's' para sim e 'n' para nao. \n")

	    else:
	    	print("A quantidade e entrada de pesos foi atingida.")
	    	esccolha_mediaAritmetica = input
    else: 
    	media = soma/quantidadeDePesos

    	print("\n Valor da media de peso dos " + quantidadeDePesos + " aluno(s) é: " + media)

	#os.system("pause")

#criando funcao para calcular a media ponderada.
def mediaPonderada():
    print("\n Calculo da Media Ponderada \n ")
     
    ap1 = intput("Digite a nota da AP1: \n")
      
    ap2 = intput("Digite a nota da AP2: \n")
     
    ap3 = intput("Digite a nota da AP3: \n")
         
    media = (notaAP1*0.2) + (notaAP2*0.3) + (notaAP3*0.5)
     
    print("\n\nMedia ponderada: %.2f", media)       
   
    #os.system("pause")

#criando funcao para calcular a mediana
def mediana():
    print("\n Calculo da Mediana \n")
    print("OBS: Será aceito somente 10 valores. \n")

    decisao_valor = 0

    while(decisao_valor < 10): 
    	valor = input("Digite o valor: \n")
    	mediana_array.append(valor)

    	decisao = input("Deseja incluir outro valor? Digite 's' para sim e 'n' para nao. \n")

    	if decisao == 's':
    		decisao_valor = decisao_valor + 1

    	else:
    		decisao_valor3 = decisao_valor
    		decisao_valor2 = 10 - len(mediana_array)
    		decisao_valor = decisao_valor2 + decisao_valor3

    result = median(mediana_array)

    print("O valor da mediana é: "+result)

	#os.system("pause")

#criando funcao para calcular a amplitude
def amplitude():
    print("\n Calculo da Amplitude \n")
    print("OBS: Será aceito somente 10 valores. \n")

    decisao_valor = 0
    i = 0

    while(decisao_valor < 10): 
    	valor = input("Digite o valor: \n")
    	amplitude_array.append(valor)

    	decisao = input("Deseja incluir outro valor? Digite 's' para sim e 'n' para nao. \n")

    	if decisao == 's':
    		decisao_valor = decisao_valor + 1

    	else:
    		decisao_valor3 = decisao_valor
    		decisao_valor2 = 10 - len(mediana_array)
    		decisao_valor = decisao_valor2 + decisao_valor3

    valor_unico = list(i for i in amplitude_array if amplitude_array.count(i) <2 )
    
    maximo = print("\n Maior valor: " + max(valor_unico))
    minimo = print("\n Menor valor: " + min(valor_unico))
    
    amplitude = maximo - minimo

    print("\n O Valor da Amplitude é: " + amplitude)

	#os.system("pause")

#criando funcao para calcular a variancia
def variancia():

	print("\n Calculo da Variancia \n")

	decisao_valor = 0
	i = 0

	while(decisao_valor < 10):

		valor = input("Digite o valor: \n")

		variancia_array.append(valor)

		decisao = input("Deseja incluir outro valor? Digite 's' para sim e 'n' para nao. \n")

		if decisao == 's':

			decisao_valor = decisao_valor + 1

		else:
			decisao_valor3 = decisao_valor
			decisao_valor2 = 10 - len(mediana_array)
			decisao_valor = decisao_valor2 + decisao_valor3

	media = mean(variancia_array)

	variancia = np.var(valores)
    
	printf("\n O Valor da Variancia é: \n" + variancia)

	#os.system("pause")
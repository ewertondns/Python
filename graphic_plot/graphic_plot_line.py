import numpy as np
import matplotlib.pyplot as plt

#---------------------Funções----------------------#

#--------------Função Plota Gráfico----------------#
def GrafPlot(array, name):
	#Salva o array, caso precise fazer modificações
	data = array
	
	print("Data:", data)#Printa o array

	#Gera as linhas vermelhas tracejadas
	for point in data:
		plt.plot((0, point), (point, point), linestyle='--', color='blue')#Linha Horizontal
		plt.plot((point, point), (0, point), linestyle='--', color='blue')#Linha Vertical

	plt.title(name)#Coloca o título no gráfico 
	plt.plot(data, data, 'go', color='red')#Plota os ponto verdes no gráfico
	plt.plot(data, data, color='red')#Gera a linha azul interligando os pontos
	plt.xlabel("X")#Define o nome do eixo X
	plt.ylabel("Y")#Define o nome do eixo Y
	plt.axhline(linewidth=0.9, color='black')#Cria a linha do eixo X
	plt.axvline(linewidth=0.9, color='black')#Cria linha do eixo Y
	plt.show()
#--------------Fim da Plota Gráfico---------------#

#-----------------Fim das Funções-----------------#

arr = [0,2,4,6,8]#Gráfico a ser gerado
nome = "Gráfico"#Nome do gráfico

GrafPlot(arr, nome)#Chama função plota gráfico
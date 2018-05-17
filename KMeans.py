import time  
from numpy import *  
import matplotlib.pyplot as plt  
import matplotlib.patheffects as path_effects
 
class KMeans():
	def __init__(self):
		print("Classe KMeans")
	  
	'''
	Método inicializa os centróides com valores
	aleatórios, dado um conjunto de dados.
	'''  
	def inicializarCentroides(self, dados, k):  
		amostra, colunas = dados.shape
		centroides = zeros((k, colunas))  		
		for i in range(k):  
			index = int(random.uniform(0, amostra))
			centroides[i, :] = dados[index, :]  
		return centroides  
	  
	'''
 	Calcula a Distância Euclidiana
 	'''
	def distanciaEuclidiana(self, vetor1, vetor2):  
		return sqrt(sum(power(vetor2 - vetor1, 2)))


	'''
	Executa os passos necessários para obter a
	clusterização(agrupamento) dos dados
	'''
	def executar(self, dados, k):  
		amostra = dados.shape[0]

		avaliacao = mat(zeros((amostra, 2)))
		mudanca = True  
	  
  
		centroides = self.inicializarCentroides(dados, k)
	  
		'''
		Executa até não ter mudanças nas avaliações
		'''
		while mudanca:  
			mudanca = False  
			for i in range(amostra):
				menorDistancia  = 100000.0  
				indice = 0  
				'''
				Encontra centróide mais próximo
				'''
				for j in range(k):  
					distance = self.distanciaEuclidiana(centroides[j, :], dados[i, :])  
					if distance < menorDistancia:  
						menorDistancia  = distance  
						indice = j  
	              
				'''
				Atualiza o Cluster
	            ''' 
				if avaliacao[i, 0] != indice:  
					mudanca = True  
					avaliacao[i, :] = indice, menorDistancia**2
	  
			'''
			Atualiza os Centróide
	       '''  
			for i in range(k):  
				pontos = dados[nonzero(avaliacao[:, 0].A == i)[0]] 
				centroides[i, :] = mean(pontos, axis = 0) #tira a média de cada coluna
	  
		print(avaliacao)
		return centroides, avaliacao  
	  
	
	'''
	Método Imprime o resultado, utilizando a biblioteca
	matplotlib
	'''
	def imprimir(self, dados, k, centroides, avaliacao):  
		amostra, colunas = dados.shape  
		if colunas != 2:  
			print ("É necessário ter duas colunas!!!")  
			return 1  
	  
		mark = ['or', 'ob', 'og', 'ok']  
		if k > len(mark):  
			print ("\nErro: Quantidade suportada de cores: %s, clusters solicitados: %s\n" %( len(mark), k ) )  
			return 1 
	     

		#Imprime todos os pontos
		for i in range(amostra):  
			pos = int(avaliacao[i, 0])
			plt.plot(dados[i, 0], dados[i, 1], mark[pos], markersize = 8)  

	    #Imprime os centróides  
		for i in range(k):  
			plt.plot(centroides[i, 0], centroides[i, 1], mark[i], markersize = 12,  path_effects=[path_effects.Stroke(linewidth=3, foreground='cyan'), path_effects.Normal()])  
	  
		plt.show() 

		#Makers
		# o - círculo 

		#Colors
		# b - blue
		# g - green
		# k - black
		# r - red
		# c - cyan
		# m - magento
		# y - yellow

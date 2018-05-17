from numpy import *  
import time  
import matplotlib.pyplot as plt 
from KMeans import KMeans
import sys

filename = "./"+sys.argv[1] #nome do arquivo	
dados = []
arquivo = open(filename)

for l in arquivo.readlines(): 
	linha = l.strip().split(' ')
	dados.append([float(linha[0]), float(linha[1])])  
arquivo.close()  

 
dados = mat(dados) #interpreta a entrada como matriz
k = int(sys.argv[2]) #quantidade de Clusters

kmeans = KMeans()
centroids, avaliacao = kmeans.executar(dados, k) #kmeans
  

kmeans.imprimir(dados, k, centroids, avaliacao)
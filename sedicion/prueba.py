#!/usr/bin/env python
# -*- coding: utf-8 -*-
#con los comentarios puedo utilizar ñ y tildes
import nltk
import csv
import sys 
from time import time

reload(sys) 
sys.setdefaultencoding("utf-8")
from nltk.tokenize import sent_tokenize, word_tokenize  #Para tokenizar las palabras
from nltk.corpus import stopwords  						#Para las palabras vacias
import unicodedata 										#Para eliminar tildes


def elimina_tildes(input_str):
	nkfd_form = unicodedata.normalize('NFKD', unicode(input_str))
	return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

class Sedicion:
	cant_textos 		  = 0
	list_words_sedicion   = []
	list_monografias      = []
	diccionario_words_sed = dict()
	# La libreria ofrece palabras en español
	spanish_words         = set(stopwords.words('spanish'))

	def __init__(self,cant_textos):
		self.cant_textos = cant_textos
	
	#Guado en una lista las palabras de sedicion.
	def open_words_sedicion(self):
		#linea    = ""
		archivo_sed  = open("words.txt","r")
		archivo_sed1 = open("words_sed.txt","r")
		for line in archivo_sed1:
			self.list_words_sedicion.append(line)
		for line in archivo_sed:
			#print line
			linea = line.split(' ')
			palabra1 = linea[0]
			palabra2 = linea[1]
			self.diccionario_words_sed[palabra1] = [int(palabra2)]
	# Textos a evaluar 
	def open_textos(self):
		cont = 0
		id_  = "0" 
		#Itero por todos los archivos 
		while cont < self.cant_textos:
			texto   = ""
			archivo = open( (id_+".txt"),"r")
 			cont    = cont+1
 			id_     = str(cont) # Cast para string
			# En el string texto, tengo toda una monografia entera
			texto   = archivo.read()
			self.list_monografias.append(texto)
		
	def tokenize(self):
		cont   = 0
		result = 0
		posible_sedicion = []
		list_prioridades = [] 
		while cont < self.cant_textos:
			#En list_monografias tengo cada texto 
			#Lista de contextos, [ ****** ]
			string_temp =  sent_tokenize(self.list_monografias[cont])
			print "\n NUEVO DOCUMENTO \n\n", string_temp,"\n\n"
			for line in string_temp:
				linea    = line.split(',')
				# En palabra 1 tengo cada contexto que al tokenizar se dividio en comas
				palabra1 = linea[0]
				#palabra1 = elimina_tildes(palabra1)
				palabra1 = word_tokenize(palabra1)
				# Ahora quito las palabras vacias como (del,el,los) 
				palabra1 = self.quitar_palabras_vacias(palabra1)
				#PRIMER FILTRO 
				# Mando a verificar sedicion en cada contexto
				posible_sed  = self.verificar_Sedicion(palabra1)
				# En posible sed tengo las las palabras q encontre en un contexto sospechosas
				if len(posible_sed)>=1:
					for line in posible_sed:
						# Busco en mi diccionario esa palabra que es comun en sedicion y extraigo su prioridad
						if self.diccionario_words_sed.has_key(line):
							x = self.diccionario_words_sed[line]
							list_prioridades.append(x[0])
						posible_sedicion.append(line)
				if(self.analizando_resultado(list_prioridades)):
					result = result + 1
					print "\n******Se encontro sedicion, se encontraron las siguientes palabras***\n"
					print posible_sedicion
				#Reseteo la lista posbile_sed para cada contexto
				self.remove_list(posible_sed)
				self.remove_list(list_prioridades)
			#Reseteo las variables
			string_temp = ""
			self.remove_list(posible_sedicion)
			self.remove_list(list_prioridades)
			cont = cont + 1

	def quitar_palabras_vacias(self,string_tokenizado):
		string_temp = []
		for w in string_tokenizado:
			# si la palabra no esta dentro de la lista de spanish_words qiere decir q no es vacia y la agrego
			if w not in self.spanish_words:
				string_temp.append(w)
		return string_temp

	#En esta funcion le paso el texto donde qiero encontrar palabras mas frecuentes y la cantidad de palabras que quiero que encuentre
	def palabras_frecuentes(self,string_tokenizado,cant_palabras):
		frec        = nltk.FreqDist(string_tokenizado) 
		vocabulary1 = frec.keys() 
		vocabulary1[:cant_palabras] 
		return vocabulary1

	#Esta funcion recibe el string tokenizada por palabras, para analizar palabra a palabra
	def verificar_Sedicion(self,string_tokenizado):
		match       = 0
		encontrados = [] 
		size  = len(self.list_words_sedicion)
		for line in string_tokenizado:
			for line2 in self.list_words_sedicion:
				if line in line2 and len(line)==len(line2)-1:
					#print line
					match  = match + 1
					encontrados.append(line)
		return encontrados
	def analizando_resultado(self,list_result):
		rpta  = False
		size  = len(list_result)
		cont  = 0
		cont1 = 0
		cont2 = 0
		cont3 = 0
		while cont < size:
			if list_result[cont] == 1:
				cont1 = cont1 + 1
			if list_result[cont] == 2:
				cont2 = cont2 + 1
			if list_result[cont] == 3:
				cont3 = cont3 + 1
			cont = cont + 1
		#Resultado
		if (cont1 >=3 and cont2 >= 1 and cont3>=1 ):
			rpta = True
		return rpta
	def remove_list(self,lista_):
		for x in lista_[:]:
			lista_.remove(x)
		return lista_
		
def main():
	start_time = time()
	Obj = Sedicion(1)
	Obj.open_words_sedicion()
	Obj.open_textos()
	Obj.tokenize()
	elapsed_time = time() - start_time
        print(" time: %0.10f seconds." % elapsed_time)
main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#con los comentarios puedo utilizar ñ y tildes
import nltk
import csv
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")
from nltk.tokenize import sent_tokenize, word_tokenize  #Para tokenizar las palabras
from nltk.corpus import stopwords  						#Para las palabras vacias
import unicodedata 										#Para eliminar tildes


EXAMPLE_TEXT = "Hi Mr james I am Joel I want to lear this library"

#EXAMPLE_TEXT = "Hola Joel que tal yo soy joel y tu mi amigo me encantaria salir yo me fui a otro lado"
example_sent = "yo estoy subiendo feliz a reirme y saltar por las escaleras muajajajaja"
print(sent_tokenize(EXAMPLE_TEXT))
print(word_tokenize(EXAMPLE_TEXT))


stop_words = set(stopwords.words('spanish'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)

def elimina_tildes(input_str):
	nkfd_form = unicodedata.normalize('NFKD', unicode(input_str))
	return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])
#read = csv.reader(prueba)
string = 'eñes'+'\n'+'\n'+'\n'+'\n'+'\n'+'héroe'
print elimina_tildes(string)
# que se puede usar asi:



class Sedicion:
	cant_textos 		= 0
	list_words_sedicion = []
	list_monografias    = []
	matriz_contextos    = []
	def __init__(self,cant_textos):
		self.cant_textos = cant_textos
	
	#Guado en una lista las palabras de sedicion.
	def open_words_sedicion(self):
		linea    = ""
		espacios = '\n'
		archivo_sed = open("words_sed.txt","r")
		for line in archivo_sed:
			linea    = line.split('	')
			palabra1 = linea[0]
			self.list_words_sedicion.append(palabra1)
		archivo_sed.close()

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
			#Primero quito ñ y tildes de los textos para tokenizarlos
			#texto   = elimina_tildes(texto)
			self.list_monografias.append(texto)
		#print self.list_monografias[2]
		#self.words  = archivo_sed.read()
		#tokens      = nltk.word_tokenize(linea)
		#tokens      = nltk.sent_tokenize(linea) 
		#archivo.close()
		#print linea[1]
		#text        = nltk.Text(tokens)
		#text.concordance("l")
	def tokenize(self):
		cont = 0
		while cont < self.cant_textos:
			print sent_tokenize(self.list_monografias[cont])
			#print word_tokenize(self.list_monografias[cont])
			cont = cont + 1
		#print self.list_monografias[0]
		
	


def main():
	Obj = Sedicion(1)
	Obj.open_words_sedicion()
	Obj.open_textos()
	Obj.tokenize()
main()

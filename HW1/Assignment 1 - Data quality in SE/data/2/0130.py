#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Creado 26/04/2016

@author: Cinthya Ramos. 09-11237
@author: Patricia Valencia. 10-10916

'''

import sys
from lexer import tokens, find_column, lexer_error, lexer_tokenList, analyzeNeo

if __name__ == '__main__':
    
	#Comprobacion de los parametros de entrada. 
	if len(sys.argv) < 2:
		print ("Error: Parametros de entrada incorrectos.")
		print ("Debe hacerlo de la siguiente manera: ")
		print ('\n''\t'+ "./LexNeo archivo.neo" +'\n')
		exit()

	#Abrimos el archivo del codigo Neo
	codeFile = open(sys.argv[1], 'r')
	code = codeFile.read()

	analyzeNeo(code)

#!C:\cygwin\bin\python
# -*- coding: utf-8 -*-
import individuo
import random

class Poblacion:
	evaluaciones = 0
	porcentajeDeCruza = 0
	porcentajeDeMutacion = 0
	
	def __init__(self, tamanio):
		self.individuos = []
		for i in range( tamanio ):
			self.individuos.append(individuo.Individuo())
		
		
			
	def getPadres(self):
		""" Selección de padres por torneo binario determinístico"""
		#hacemos una copia de los individuos
		individuos = list( self.individuos )
		#Aqui se guardarán los nuevos padres
		padres = []
		
		for i in range( len( self.individuos ) ):
			random.shuffle( individuos ) 
			padres.append( min( individuos[0:2] ) )
		
		return padres
	
	def cruzar(self, individuos ):
		hijos = []
		for i in  range(0, len(self.individuos), 2 ):
			if random.random() < Poblacion.porcentajeDeCruza:
				hijos += individuos[i].cruzar( individuos[ i+1 ] )
			else:
				hijos += [ individuos[i], individuos[ i + 1] ]
		return hijos
			 	
	
	def mutar(self, individuos):
		pass
	
	
	def __str__(self):
		return str( self.individuos )
					
					
				
				 
			
			
			 
				
			
			
		
		
		
		
		
		

		
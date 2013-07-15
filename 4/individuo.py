#!C:\cygwin\bin\python
# -*- coding: utf-8 -*- 
import random
import math
from poblacion import *

class Individuo:
	limiteSuperior = 5.12
	limiteInferior = -5.12
	
	def __init__(self, values=""):
		""" Se le podrán pasar los values con los que inicializará, o dejarlo vació, y se crearán 
		values aleatorios, si se pasa values se generá la aptitud, si no se pasa, no se generará
		para poderlo generar hasta después de la cruza"""
		self.values = []
		self.aptitud = 0
		
		if values:
			for i in values:
				self.values.append( i )
		else:
			for i in range(10):
				self.values.append( random.uniform( Individuo.limiteInferior, Individuo.limiteSuperior) )
			self.updAptitud() # Obtenemos la aptitud sólo si se genera con valores aleatorios	
		
		
	def setValues(self):
		pass

	def updAptitud(self):
		"""Actualiza la aptitud en base a los values, vuelve a calcular la aptitud """
		Poblacion.evaluaciones += 1;
		D = 10
		suma = 0.0
		for x in self.values:
			suma += ( x**2 - 10 * math.cos( 2 * math.pi * x ) )
		res = 10 * D + suma
		self.aptitud = res
		
	
	def getAptitud(self):
		return self.aptitud
	
	def __repr__(self):
		return str( self.aptitud )
	
	def __str__(self):
		return "[" + ", ".join( str( round(n, 3) ) for n in self.values ) + "] f(x): " + str( round( self.aptitud, 3 ) )

	
	def __cmp__(self, other):
		return self.aptitud - other.aptitud
	
	
	def cruzar(self, other):
		#Los valores de los padres
		p1 = self.values
		p2 = other.values
		#para guardar  los valores de los hijos formados
		h1 = []
		h2 = []

		
		for i in range( len(self.values) ):
			v = p1[i]
			w = p2[i]
			a = calcular_a( v, w, Individuo.limiteSuperior, Individuo.limiteInferior )
			
			x_h1 = w * a + v * ( 1 - a )
			x_h2 = v * a + w * ( 1 - a )
			
			h1.append(x_h1)
			h2.append(x_h2)
			
		return [ Individuo( h1 ), Individuo( h2 ) ]
			
			
	
	def mutar(self):
		r = random.randint(0, len(self.values) -1 )
		self.values[ r ] = random.uniform( Individuo.limiteInferior, Individuo.limiteSuperior )
		
	
	
def calcular_a(v, w, ls, li):
	""" Calcula a en base a su w, v y límites inferiores y superiores"""
	if v != w:
		alfa = ( li - w ) / ( v - w )
		beta = ( ls - v ) / ( w - v )
		gama = ( li - v ) / ( w - v )
		delta = ( ls - w ) / ( v - w)
		
		if v > w:
			return random.uniform( max( alfa, beta ), min( gama, delta )  )
		elif v < w:
			return random.uniform( max( gama, delta ), min( alfa, beta ) )
	else:
		return 0
				

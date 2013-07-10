#!C:\cygwin\bin\python
import random
from poblacion import *

class Individuo:
	#p_cruza = 0;
	
	def __init__(self, cad_binary=""):
		self.values = []
		self.cadenaBits = ""
		self.aptitud = 0
		
		if cad_binary:
			self.cadenaBits = cad_binary
			self.setValues()
		else:
			for i in range( 10):
				self.values.append( round ( random.uniform( -10, 10), 3 ) )
			self.setAptitud()
			self.makeBinary()
		
		
	def setValues(self):
		"""Establecera los valores de las diez x (self.values) en base a su binario (de 150 bits)"""
		self.values = []
		for i in range(0, len(self.cadenaBits), 15 ):
			cadena_bit = self.cadenaBits[ i : i + 15 ]
			self.values.append( binary_to_real( cadena_bit ) )

	def setAptitud(self):
		Poblacion.evaluaciones += 1;
		self.aptitud = sum ( [ n*n for n in self.values] )
	
	def getAptitud(self):
		return self.aptitud
	
	def __repr__(self):
		return str( self.aptitud )
	
	def __str__(self):
		a_mostrar = []
		for i in self.values:
			a_mostrar.append( round( i, 3) )
		
		return str( a_mostrar  ) + " f(x) = " +  str( self.aptitud )
	
	def __cmp__(self, other):
		return self.aptitud - other.aptitud
	
	def makeBinary(self):
		""" Crea la representacion binaria, son 15 espacios por 10 individuos"""
		ls = 10 #limite superior
		li = -10 #limite inferior
		t = 15 # total de binarios
		
		cadena_bits = ""
		for i in self.values:
			entero = (int) ( ( i - li ) * ( 2 ** t ) ) / ( ls - li )
			cadena_bits += "{0:b}".format(entero).zfill(15)
			
		self.cadenaBits = cadena_bits
		return cadena_bits
	
	def getBinary(self):
		if self.cadenaBits:
			return self.cadenaBits
		else:
			return makeBinary() 
	
			
	
	def cruzar(self, other):
		binary1 = self.getBinary()
		binary2 = other.getBinary()
		hijo1 = ""
		hijo2 = ""
		
		for i in range( len( binary1 ) ):
			if( random.random() <= 0.5 ): #Escogemos al padre 1
				hijo1 += binary1[i]
				hijo2 += binary2[i]
			else:
				hijo1 += binary2[i]
				hijo2 += binary1[i]
				
		return [ Individuo( hijo1 ), Individuo( hijo2 ) ]
		
				
				

def binary_to_real( cadbin ):
	ls = 10 #limite superior
	li = -10 #limite inferior
	entero = int( cadbin, 2 )
	t = 15
	
	real = li + ( ( entero * ( ls-li ) * 1.0 ) / ( 2 ** t - 1 ) ) 
	return real
	
	
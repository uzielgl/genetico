#!C:\cygwin\bin\python
import individuo
import random

class Poblacion:
	evaluaciones = 0
	porcentajeDeCruza = 0
	porcentajeDeMutacion = 0
	
	def __init__(self, tamanio_poblacion):
		self.tamanioPoblacion = tamanio_poblacion
		self.individuos = []
		for i in range( tamanio_poblacion ):
			self.individuos.append( individuo.Individuo() )
			
	def getPadres(self):
		"""Seleccionara en base a la ruleta, se hace el cambio 
		para poder usar minimos en vez de maximos """
		
		negativos = [ n.getAptitud() * -1 for n in self.individuos]
		minimo = min( negativos )
		sumador = abs( minimo ) * 2 #valor a sumar
		
		nuevas_aptitudes = [ n + sumador for n in negativos ]
		
		promedio_aptitudes = sum( nuevas_aptitudes) / len( nuevas_aptitudes ) * 1.0
		
		#Obtenemos los valores esperados
		valores_esperados = [ n / promedio_aptitudes for n in nuevas_aptitudes ]
		
		t = sum( valores_esperados )
		
		padres = []
		for  i in range( self.tamanioPoblacion):
			r = random.uniform( 0, t)
			suma = 0;
			while suma < r:
				for idx, val in enumerate( valores_esperados ):
					suma += val
					if suma >= r:
						padres.append( self.individuos[ idx] )
						break
			#print "random %s, suma %s, index %s" %( r, suma, idx)
		return padres
	
	def cruzar(self, individuos ):
		hijos = [];
		for i in range(0, len(individuos), 2 ):
			if( random.random() <= Poblacion.porcentajeDeCruza ):
				resultado = individuos[ i ].cruzar( individuos[i+1] )
				hijos.append( resultado[0] )
				hijos.append( resultado[1] )
			else:
				hijos.append( individuos[ i ] )
				hijos.append( individuos[ i + 1 ] )
		return hijos
	
	
	def mutar(self, individuos):
		hijos_mutados = []
		for i in individuos:
			if random.random() <= Poblacion.porcentajeDeMutacion:
				cadena_bit = i.getBinary()
				rand = random.randint(0, len(cadena_bit) - 1 )
				
				lst_cadena_bit = list( cadena_bit )
				
				lst_cadena_bit[rand] = "0" if lst_cadena_bit[rand] == "1" else "1"
				cadena_bit_mutada = "".join( lst_cadena_bit )
				hijos_mutados.append( individuo.Individuo( cadena_bit_mutada ) )
			else:
				 hijos_mutados.append( i )
		return hijos_mutados
	
					
					
				
				 
			
			
			 
				
			
			
		
		
		
		
		
		

		
#!C:\cygwin\bin\python
# -*- coding: utf-8 -*-

from individuo import *
from poblacion import *
import sys


tamanio_poblacion = 40
generaciones = 10000
p_cruza = 1
p_mutacion = .5

# tamanio_poblacion = 40
# generaciones = 1000
# p_cruza = 1
# p_mutacion = .5  
#.188


#si viene con argumentos sobre escribimos los de default
if len( sys.argv ) > 1:
	tamanio_poblacion = int( sys.argv[1] )
	generaciones =  int( sys.argv[2] )
	p_cruza =  float( sys.argv[3] )
	p_mutacion =  float( sys.argv[4] ) 
	





#Individuo.p_cruza = 0.5

import random
#random.seed(123123123)

Poblacion.porcentajeDeMutacion = p_mutacion
Poblacion.porcentajeDeCruza = p_cruza



f = open("corridas.txt", "w")
f.close()

mejores_soluciones = []

for j in range(1, 31):
	f = open("corridas.txt", "a")
	
	
	print "============================================="
	print "Problema 1 en binario"
	print "Tamanio de la poblacion: " + str( tamanio_poblacion )
	print "Generaciones: " + str( generaciones )
	print "P. Cruza: " + str( p_cruza )
	print "P. Mutacion: " + str(p_mutacion) 
	print "============================================="
	print ""

	f.write("Corrida " + str( j ) + "\n")
	
	p = Poblacion( tamanio_poblacion )
	
	for i in range( generaciones ):
		print "generacion: " + str( i )
		f.write("Generacion: " + str( i ) + "\n")
		
		padres = p.getPadres()
		
		
		hijos = p.cruzar( padres ) # Todos los hijos que tenga una aptitud de cero, es que no se les ha evaluado
		 
		hijos_mutados = p.mutar( hijos )
		
		for j in hijos_mutados:
			j.setValues()
			j.setAptitud()
		
		mejor = min( p.individuos ) #Obtenemos el mejor individuo
		
		hijos_mutados.remove( max( hijos_mutados ) ) # Eliminamos la peor solucion
		
		hijos_mutados.insert( 0, mejor ) # Juntamos en hijos_mutados las soluciones
		
		mejor_de_mejores = min( hijos_mutados ) # Obtenemos el mejor de los mejores
		
		p.individuos = hijos_mutados
		
		print mejor_de_mejores
		f.write( mejor_de_mejores.__str__() + "\n")
		
		if  i == generaciones - 1 :
			mejores_soluciones.append( mejor_de_mejores )
			
	f.close()
	

f = open("corridas.txt", "a")
f.write( "============= Mejores corridas ============== \n")
for inx, i in enumerate( mejores_soluciones ):
	f.write( "Corrida " + str( inx + 1 ) + ":" + i.__str__() + "\n" ) 

print Poblacion.evaluaciones


#print hijos

#print hijos

#hijos = p.mutar( hijos )

#print Poblacion.evaluaciones



#print len ( p.getPadres() )

#print Poblacion.evaluaciones

#print p.individuos[0].cruzar( p.individuos[1] )



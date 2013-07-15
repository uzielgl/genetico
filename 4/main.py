#!C:\cygwin\bin\python
# -*- coding: utf-8 -*-
from individuo import *
from poblacion import *
import random
import sys
import copy

#Ponemos semilla
random.seed(123456789)

#Obtenemos los argumentos
if len( sys.argv ) > 1:
	tamanio_poblacion = int( sys.argv[1] )
	generaciones =  int( sys.argv[2] )
	p_cruza =  float( sys.argv[3] )
	p_mutacion =  float( sys.argv[4] ) 
else:
	tamanio_poblacion = 2
	generaciones = 100000
	p_cruza = .5
	p_mutacion = 1
	
# 	tamanio_poblacion = 2
# 	generaciones = 100000
# 	p_cruza = .5
# 	p_mutacion = 1
#	0.588
	
# 	tamanio_poblacion = 2
# 	generaciones = 100000
# 	p_cruza = .5
# 	p_mutacion = .5
# 	1.268
	
# 	tamanio_poblacion = 2
# 	generaciones = 100000
# 	p_cruza = .8
# 	p_mutacion = .5
# 	1.536


Poblacion.porcentajeDeCruza = p_cruza
Poblacion.porcentajeDeMutacion = p_mutacion
	
f = open("corridas.txt", "w")
f.close()

mejores_soluciones = []

for j in range(1, 3):
	f = open("corridas.txt", "a")
	f.write("Corrida " + str(j) + "\n")
	
	#Imprimimos información 
	print "============================================="
	print "Problema 1"
	print "Tamanio de la poblacion: " + str( tamanio_poblacion )
	print "Generaciones: " + str( generaciones )
	print "P. Cruza: " + str( p_cruza )
	print "P. Mutacion: " + str(p_mutacion) 
	print "============================================="
	print ""
	
	
	#Generamos la población inicial
	p = Poblacion( tamanio_poblacion )
	
	for i in range( generaciones ):
		print "Generación " + str( i )
		f.write( "generacion: " + str( i ) + "\n" )
		
		#De la población actual, obtenemos la mejor solución, que se usará en el reemplazo con elitismo
		mejor_de_poblacion_actual = copy.deepcopy( min( p.individuos ) )
		
		
		#obtenemos los padres
		padres = p.getPadres()
		
		#cruzamos esos padres
		hijos = p.cruzar( padres )
		#Los mutamos de acuerdo al porcentaje de mutación
		for k in hijos:
			if random.random() < p_mutacion:
				k.mutar()
		#actualizamos las aptitudes
		for h in hijos: h.updAptitud()
		
		#Ordenamos los hijos
		random.shuffle( hijos )
		
		#hacemos la nueva población con el mejor de la población, y con los mejores de los hijos
		p.individuos = [ mejor_de_poblacion_actual ] + hijos[: len(hijos)-1 ]
		
		#obtenemos el mejor y lo mostramos
		mejor = min( p.individuos )
		print mejor
		f.write( mejor.__str__() + "\n" )
		
		if  i == generaciones - 1 :
			mejores_soluciones.append( mejor )
	f.close()
	
	
f = open("corridas.txt", "a")
f.write( "============= Mejores corridas ============== \n")
for inx, i in enumerate( mejores_soluciones ):
	f.write( "Corrida " + str( inx + 1 ) + ":" + i.__str__() + "\n" ) 



print Poblacion.evaluaciones
		







""" 
tamanio_poblacion = 100
generaciones = 10000
p_cruza = 0.8
p_mutacion = 0.8



#si viene con argumentos sobre escribimos los de default
if len( sys.argv ) > 1:
	tamanio_poblacion = int( sys.argv[1] )
	generaciones =  int( sys.argv[2] )
	p_cruza =  float( sys.argv[3] )
	p_mutacion =  float( sys.argv[4] ) 
	


print "============================================="
print "Problema 1"
print "Tamanio de la poblacion: " + str( tamanio_poblacion )
print "Generaciones: " + str( generaciones )
print "P. Cruza: " + str( p_cruza )
print "P. Mutacion: " + str(p_mutacion) 
print "============================================="
print ""


#Individuo.p_cruza = 0.5

import random
#random.seed(123123123)

Poblacion.porcentajeDeMutacion = p_mutacion
Poblacion.porcentajeDeCruza = p_cruza

p = Poblacion( tamanio_poblacion )

#print p.individuos
for i in range( generaciones ):
	print "generacion: " + str( i )
	padres = p.getPadres()
	
	
	hijos = p.cruzar( padres ) # Todos los hijos que tenga una aptitud de cero, es que no se les ha evaluado
	 
	hijos_mutados = p.mutar( hijos )
	
	for i in hijos_mutados:
		i.setValues()
		i.setAptitud()
	
	mejor = min( p.individuos ) #Obtenemos el mejor individuo
	
	hijos_mutados.remove( max( hijos_mutados ) ) # Eliminamos la peor solucion
	
	hijos_mutados.insert( 0, mejor ) # Juntamos en hijos_mutados las soluciones
	
	mejor_de_mejores = min( hijos_mutados ) # Obtenemos el mejor de los mejores
	
	p.individuos = hijos_mutados
	
	print mejor_de_mejores



 

print Poblacion.evaluaciones


#print hijos

#print hijos

#hijos = p.mutar( hijos )

#print Poblacion.evaluaciones



#print len ( p.getPadres() )

#print Poblacion.evaluaciones

#print p.individuos[0].cruzar( p.individuos[1] )
"""


#!C:\cygwin\bin\python
# -*- coding: utf-8 -*-
from individuo import *
from poblacion import *
import random
import sys

#Ponemos semilla
#random.seed(123456789)

#Obtenemos los argumentos
if len( sys.argv ) > 1:
	tamanio_poblacion = int( sys.argv[1] )
	generaciones =  int( sys.argv[2] )
	p_cruza =  float( sys.argv[3] )
	p_mutacion =  float( sys.argv[4] ) 
else:
	tamanio_poblacion = 100
	generaciones = 100000
	p_cruza = 0.8
	p_mutacion = 0.8


Poblacion.porcentajeDeCruza = p_cruza
Poblacion.porcentajeDeMutacion = p_mutacion
	
	
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
	
	#De la población actual, obtenemos la mejor solución, que se usará en el reemplazo con elitismo
	mejor_de_poblacion_actual = min( p.individuos )
	
	
	#obtenemos los padres
	padres = p.getPadres()
	
	#cruzamos esos padres
	hijos = p.cruzar( padres )
	#Los mutamos de acuerdo al porcentaje de mutación
	for i in hijos:
		if random.random < p_mutacion:
			i.mutar()
	#actualizamos las aptitudes
	for i in hijos: i.updAptitud()
	
	#Ordenamos los hijos
	hijos.sort()
	
	#hacemos la nueva población con el mejor de la población, y con los mejores de los hijos
	p.individuos = [ mejor_de_poblacion_actual ] + hijos[: len(hijos)-1 ]
	
	#obtenemos el mejor y lo mostramos
	mejor = min( p.individuos )
	print mejor
	








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


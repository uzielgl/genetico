#!C:\cygwin\bin\python
from individuo import *
from poblacion import *
import sys


tamanio_poblacion = 40
generaciones = 1000
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



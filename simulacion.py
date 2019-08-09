tiempoGlobal = 0

tiempoSemaforosRojo = 55
tiempoSemaforo1Verde = 70
tiempoSemaforo2Verde = 90

tiempoSemaforo1 = [tiempoSemaforo1Verde, True]
tiempoSemaforo2 = [tiempoSemaforo2Verde, False]
tiempoLiberarFlujo = [tiempoSemaforosRojo, False]

ciclo = 2

retrasoArranque = 2

cola1 = [] 
cola2 = []

while tiempoGlobal < 200 :
	tiempoGlobal += 1

	if(tiempoSemaforo1[1]):
		tiempoSemaforo1[0] -= 1
		print("1 Semaforo Verde")
		if(tiempoSemaforo1[0] == 0):
			tiempoSemaforo1 = [tiempoSemaforo1Verde, False]
			tiempoSemaforo2 = [tiempoSemaforo2Verde, False]
			tiempoLiberarFlujo = [tiempoSemaforosRojo, True]

	if(tiempoSemaforo2[1]):
		print("2 Semaforo Verde")
		tiempoSemaforo2[0] -= 1
		if(tiempoSemaforo2[0] == 0):
			tiempoSemaforo2 = [tiempoSemaforo2Verde, False]
			tiempoSemaforo1 = [tiempoSemaforo1Verde, False]
			tiempoLiberarFlujo = [tiempoSemaforosRojo, True]

	if(tiempoLiberarFlujo[1]):
		print("ROJO")
		tiempoLiberarFlujo[0] -= 1
		if(tiempoLiberarFlujo[0] == 0 and ciclo == 1 ):
			tiempoLiberarFlujo = [tiempoSemaforosRojo, False]
			tiempoSemaforo2 = [tiempoSemaforo2Verde, False]
			tiempoSemaforo1 = [tiempoSemaforo1Verde, True]
			ciclo = 2
		if(tiempoLiberarFlujo[0] == 0 and ciclo == 2):
			tiempoLiberarFlujo = [tiempoSemaforosRojo, False]
			tiempoSemaforo1 = [tiempoSemaforo1Verde, False]
			tiempoSemaforo2 = [tiempoSemaforo2Verde, True]
			ciclo = 1



'''
if(tiempoGlobal%tiempoSemaforosRojo == 0):

if(contadorCola1%12 == 0):
	cola1.insert( 0 , 1 )

if (contadorCola2%9 == 0):
	cola2.insert( 0 , 1 )

if(tiempoSemaforo1Verde==70):
	tiempoSemaforo1Verde = 0
	cola1.pop(0) 
'''





import numpy as np
import math

tiempoGlobal = 0

tiempoSemaforosRojo = 55
tiempoSemaforo1Verde = 70
tiempoSemaforo2Verde = 90

tiempoSemaforo1 = [tiempoSemaforo1Verde, True]
tiempoSemaforo2 = [tiempoSemaforo2Verde, False]
tiempoLiberarFlujo = [tiempoSemaforosRojo, False]

tiempoLlegadaCola1 = math.ceil(np.random.exponential(scale=9, size=1))
tiempoLlegadaCola2 = math.ceil(np.random.exponential(scale=12, size=1))

ciclo = 2

retrasoArranque1 = 2
retrasoArranque2 = 2

cola1 = []
cola2 = []

esperaCola1 = []
esperaCola2 = []

while tiempoGlobal < 10000 :
	cola1 = [x + 1 for x in cola1]
	cola2 = [x + 1 for x in cola2]
	tiempoGlobal += 1
	print(cola1, " - ", cola2)

	if(tiempoLlegadaCola1 != 0):
		tiempoLlegadaCola1 -= 1
	else:
		tiempoLlegadaCola1 = math.ceil(np.random.exponential(scale=9, size=1))
		if(tiempoSemaforo1[1] == False):
			cola1.append(1)

	if(tiempoLlegadaCola2 != 0):
		tiempoLlegadaCola2 -= 1
	else:
		tiempoLlegadaCola2 = math.ceil(np.random.exponential(scale=12, size=1))
		if(tiempoSemaforo2[1] == False):
			cola2.append(1)

	if(tiempoSemaforo1[1]):
		tiempoSemaforo1[0] -= 1
		print("1 Semaforo Verde")
		if(tiempoSemaforo1[0] == 0):
			tiempoSemaforo1 = [tiempoSemaforo1Verde, False]
			tiempoSemaforo2 = [tiempoSemaforo2Verde, False]
			tiempoLiberarFlujo = [tiempoSemaforosRojo, True]
			retrasoArranque1 = 2
		else:
			if(retrasoArranque1 != 0):
				retrasoArranque1 -= 1
			else:
				try:
					tiempoEsperando = cola1.pop(0)
					esperaCola2.append(tiempoEsperando)
				except:
					0
				retrasoArranque1 = 2

	if(tiempoSemaforo2[1]):
		print("2 Semaforo Verde")
		tiempoSemaforo2[0] -= 1
		if(tiempoSemaforo2[0] == 0):
			tiempoSemaforo2 = [tiempoSemaforo2Verde, False]
			tiempoSemaforo1 = [tiempoSemaforo1Verde, False]
			tiempoLiberarFlujo = [tiempoSemaforosRojo, True]
			retrasoArranque2 = 2
		else:
			if(retrasoArranque2 != 0):
				retrasoArranque2 -= 1
			else:
				try:
					tiempoEsperando = cola2.pop(0)
					esperaCola2.append(tiempoEsperando)
				except:
					0
				retrasoArranque2 = 2

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

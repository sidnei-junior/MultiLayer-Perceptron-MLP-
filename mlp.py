import camada as camada

class mlp:

    def __init__(self, entradas, pesos, n_camadas, saidas, limiares, epocas, t_aprendizado):
        self.entradas = entradas
        self.pesos = pesos
        self.n_camadas = n_camadas
        self.saidas = saidas
        self.limiares = limiares
        self.epocas = epocas
        self.t_aprendizado = t_aprendizado

    def backpropagtion(self):
        # chamar o forward para todas as camadas da primeira até a última e depois o backward voltando.
        entradas_camadas_seguinte = self.entradas
        for i in range(self.n_camadas):
            cam = camada(entradas_camadas_seguinte, ) # analisar a questão dos pesos já que são diferenes para todas as camadas e já são armazenados em uma matriz
            entradas_camadas_seguinte = cam.forward()
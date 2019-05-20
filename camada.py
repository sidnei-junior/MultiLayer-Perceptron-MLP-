from neuronio import neuronio

class camada:

    def __init__(self, entradas, pesos, n_neuronios, saidas, limiares):
        self.entradas = entradas
        self.pesos = pesos
        self.n_neuronios = n_neuronios
        self.saidas = saidas
        self.limiares = limiares

    def forward(self):
        # Chamar o forward da classe neurônio
        for i in range(self.n_neuronios):
            neu = neuronio(entradas, pesos[i],limiares[i])
            saidas[i] = neu.forward()

        return saidas


    def backward(self):
        # Chamar o backward da classe neurônio

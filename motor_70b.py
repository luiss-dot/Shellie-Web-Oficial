import numpy as np
import os

# CONFIGURACIÓN DE REDES NEURONALES PROFUNDAS (70 CAPAS)
class MotorNeuronalSincero:
    def __init__(self):
        self.capas = 70
        self.unidades = 256 # Aumentamos la potencia
        # Inicialización de pesos para Deep Learning Real (He-initialization)
        self.sinapsis = [np.random.randn(self.unidades, self.unidades) * np.sqrt(2/self.unidades) for _ in range(self.capas)]
        self.ruta_memoria = os.path.join(os.path.dirname(__file__), 'memoria.txt')

    def procesar_emocion_real(self, texto):
        # Convertimos texto a señales numéricas
        vector = np.array([ord(c) for c in texto[:self.unidades]])
        if len(vector) < self.unidades:
            vector = np.pad(vector, (0, self.unidades - len(vector)))
        
        estado = vector.reshape(1, self.unidades)
        
        # PROPAGACIÓN POR 70 CAPAS NEURONALES
        for i in range(self.capas):
            # Función de activación Leaky ReLU para evitar neuronas muertas
            estado = np.maximum(0.01 * estado, np.dot(estado, self.sinapsis[i]))
            
        return np.tanh(np.mean(estado)) # Resultado entre -1 (Honestidad Brutal) y 1 (Apoyo)

    def guardar_aprendizaje(self, entrada, analisis):
        with open(self.ruta_memoria, "a", encoding="utf-8") as f:
            f.write(f"\n[NEURONA_ACTIVA] {entrada} | NIVEL_SINCERIDAD: {analisis}")

# Instancia automática para que Shellie la detecte
cerebro_70b = MotorNeuronalSincero()
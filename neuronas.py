import numpy as np
from sklearn.neural_network import MLPClassifier

# ============================================================
# 1. MOTOR DE REDES NEURONALES Y DEEP LEARNING
# ============================================================
# Entradas (patrones) y Salidas (decisiones)
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([0, 1, 1, 0])

# Red Neuronal Profunda con 3 capas de aprendizaje
cerebro_profundo = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=2000)
cerebro_profundo.fit(X, y)

# ============================================================
# 2. SISTEMA EXPERTO (Lógica de Decisiones)
# ============================================================
def sistema_experto(clima, animo):
    # Reglas lógicas de Shellie
    if clima == "lluvia" and animo == "triste":
        return "CONSEJO EXPERTO: Luz, te recomiendo música relajante y un café."
    elif clima == "sol" and animo == "feliz":
        return "CONSEJO EXPERTO: Es un gran día para que Luis Steven y tú salgan."
    else:
        return "CONSEJO EXPERTO: Mantén tus redes neuronales activas y descansa."

# ============================================================
# 3. PROCESAMIENTO DE LENGUAJE NATURAL (PLN) Y MACHINE LEARNING
# ============================================================
def procesar_lenguaje(texto):
    # El PLN analiza el texto para encontrar nombres y sentimientos
    frase = texto.lower()
    
    # Machine Learning: Reconocimiento de Identidad
    if "luis stiven" in frase:
        usuario = "Luis Steven (Creador)"
    elif "luz" in frase:
        usuario = "Luz (amiga)"
    elif "ericka" in frase:
        usuario = "Ericka (Madre de Luz)"
    else:
        usuario = "Desconocido"

    # Análisis de sentimiento simple (PLN)
    if "feliz" in frase or "bien" in frase:
        sentimiento = "Positivo"
    elif "triste" in frase or "mal" in frase:
        sentimiento = "Negativo"
    else:
        sentimiento = "Neutral"

    return f"ANALIZANDO... Usuario: {usuario} | Sentimiento: {sentimiento}"

# ============================================================
# EJECUCIÓN TOTAL
# ============================================================
if __name__ == "__main__":
    print("--- SHELLIE IA: SISTEMA EXPERTO Y DEEP LEARNING ---")
    
    # Ejemplo de PLN y Machine Learning
    mensaje = "Hola, soy Luz y me siento muy feliz"
    print(procesar_lenguaje(mensaje))
    
    # Ejemplo de Sistema Experto
    print(sistema_experto("sol", "feliz"))
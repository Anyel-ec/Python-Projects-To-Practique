import tensorflow as tf
import numpy as np

# Generar datos de entrenamiento
num_samples = 1000
x_train = np.random.rand(num_samples, 2)   # Dos números aleatorios
y_train = np.sum(x_train, axis=1)           # Suma de los dos números

# Construir el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),
    tf.keras.layers.Dense(1)
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mse')

# Entrenar el modelo
model.fit(x_train, y_train, epochs=50, batch_size=32)

# Evaluar el modelo
x_test = np.array([[0.3, 0.7], [0.5, 0.9]])
predictions = model.predict(x_test)
print("Predicciones:", predictions.flatten())

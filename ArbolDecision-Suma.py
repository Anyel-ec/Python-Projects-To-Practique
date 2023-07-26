from sklearn.tree import DecisionTreeRegressor
import random

# Generar 20 ejemplos aleatorios para aprender a sumar
X_train = [[random.randint(1, 100), random.randint(1, 100)] for _ in range(10000)]
y_train = [sum(numbers) for numbers in X_train]

# Crear el modelo de árbol de decisiones
model = DecisionTreeRegressor()

# Entrenar el modelo
model.fit(X_train, y_train)

# Datos de prueba
X_test = [[5, 4], [6, 8], [4, 6], [5, 6]]
# Realizar predicciones
predictions = model.predict(X_test)

print("Predicciones:")
for i in range(len(X_test)):
    print(f"{X_test[i][0]} + {X_test[i][1]} = {round(predictions[i])}")

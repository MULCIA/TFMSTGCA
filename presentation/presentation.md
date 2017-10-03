Análisis de las transiciones de comportamiento en crecimiento de tumores usando una simulación con autómata celular
===

###### Sergio Rodríguez Calvo, Diciembre 2017.
###### Trabajo fin de máster (MULCIA), Universidad de Sevilla.

---

# Índice

1. Objetivos
2. Breve introducción a la enfermedad del cáncer.
3. Simulación con autómata celular.
4. Modelización.
5. Modelo de eventos.
6. Pruebas previas a la mitósis.
7. Mitosis.
8. Experimentos.
9. Resultados.

---

# Objetivos

* Encontrar artículos cientificos de calidad sobre esta temática.
* Extraer información del artículo (o los artículos).
* Elegir un artículo y hacer un modelado e implementación propia.
* Reproducir los resultados del artículo.
* Comparar los resultados obtenidos con los del artículo.

---

# Breve introducción a la enfermedad del cáncer

* Nombre genérico para agrupar más de 200 enfermedades que causan proliferación descontrolada de células.
* Se conoce como neoplasia a toda masa anormal, y puede ser invasiva (carcinoma) o benigna (adenoma). Los diferenciadores son la invasividad y el factor de crecimiento.
* Presenta diferentes fases: crecimiento, angiogénesis y metástasis.

---

# Simulación con autómata celular

* Un autómata celular es un modelo matemático para sistemas dinámicos.
* Apropiado para sistemas ecológicos y de comportamiento emergente, en el cual los elementos interactúan localmente.
* Apropiado para realizar simulación en este tipo de problemas.

---

# Modelización

* Rejilla o matriz en tres dimensiones con una única célula sana en su centro.
* No se considera el tamaño de la célula.
* Cada célula presenta:
    * Un genoma formado por cinco elementos binarios (marcadores).
    * Dos propiedades: tamaño del telómero; y tasa de mutación base.
* Existe un límite espacial replicativo (concentración de factor de crecimiento).

--- 

# Modelo de Eventos

* Hay una serie de atributos globales a la simulación:
    * Factor de muerte aleatoria de la célula.
    * Factor de reemplazo de un vecino.
    * Factor de incremento de la tasa base de mutación.
    * Factor de evasión de apoptosis.
* Cada célula recibe programación de evento mitótico en el futuro de forma aleatoria.
* Cada iteración suponen aproximadamente entre 15 y 24 horas.

---

# Pruebas previas a la mitósis

* Prueba de muerte aleatoria.
* Prueba de muerte por daño genético.
* Prueba de mitosis:
    * Comprobación del factor de crecimiento.
    * Comprobación de inhibición de parada de crecimiento.
    * Comprobación de potencial replicativo sin límites.
* Si supera todas las pruebas se ejecuta la mitosis.

---

# Mitosis

* Consiste en una serie de pasos:
    1. Incrementar la tasa de mutación base si el marcador de inestabilidad genética está presente.
    2. Añadir mutaciones a la célula hija de acuerdo a su tasa de mutación base.
    3. Decrementar el telómero en una unidad en ambas células.
* Tras la mitosis se debe programar nuevo evento mitotico como se ha explicado previamente en ambas células.
* Si no aplica mitosis, y la célula no ha muerto, se le programa nuevo evento mitótico.

---

# Experimentos



---

# Resultados



---

# ¿Alguna pregunta?

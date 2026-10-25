# Práctica 5: La Ruleta Francesa Cuántica con PyQuil

Implementación de un simulador cuántico para el juego de la Ruleta Francesa utilizando registros de múltiples cúbits con **pyQuil** y el entorno de Rigetti Forest SDK[cite: 20].

## Descripción

El proyecto traslada la lógica y aleatoriedad de la ruleta francesa (37 casillas: 0 neutro, rojos y negros) a circuitos cuánticos, modelando un sistema con 4 apostadores independientes y 1 croupier con balance de monedas dinámico por rondas[cite: 20, 21].

## Estructura del Repositorio

- **`ruleta_cuantica.py` (Modo Estándar):**
  - Generación cuántica de las tiradas del croupier (número y color) y de las decisiones aleatorias de los jugadores (apuesta a número, par/impar, falta/pasa [1-18 / 19-36] o color)[cite: 20, 21].
  - Evaluación independiente de aciertos y liquidación de apuestas ronda a ronda[cite: 21].
- **`ruleta_trampas.py` (Intervención Cuántica):**
  - El croupier espía la apuesta de un jugador y, en caso de coincidencia, perturba el sistema aplicando una compuerta cuántica para invertir aleatoriamente el estado de uno de sus cúbits antes de la lectura final[cite: 21].
- **`ruleta_clasica.py` (Implementación Clásica):**
  - Simulación comparativa del juego utilizando generación pseudoaleatoria clásica en Python (sin librerías cuánticas)[cite: 21].

## Tecnologías Utilizadas

- Python 3
- pyQuil
- Rigetti Forest SDK (`quilc` & `QVM`)[cite: 20]
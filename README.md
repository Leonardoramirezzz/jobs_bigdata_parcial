En jobs dejo mi job de hadoop y de hive.

 - El job de hadoop es un simple Contar cuántas reseñas fueron positivas y cuántas negativas según el campo recommended.
Así que el job responde a la pregunta:

“¿Cuántas reseñas totales recomiendan el juego y cuántas no lo recomiendan?”

⚙️ 2️⃣ El Mapper (mapper.py)

Cada línea del CSV (una reseña) pasa por el mapper.

Se separan las columnas con el módulo csv de Python.

Se toma la columna número 7 (fields[7]), que corresponde a recommended.

Si ese valor es "true" o "false", el mapper emite una clave–valor así:

true    1
false   1


👉 En otras palabras, cada reseña genera una línea con su valor de “recomendado” y el número 1.

⚙️ 3️⃣ El Reducer (reducer.py)

El reducer recibe las salidas del mapper agrupadas por clave (true o false) y suma todos los valores.

Así calcula cuántas veces apareció cada clave.

Por ejemplo, si el mapper produjo:

true    1
true    1
false   1
true    1
false   1


El reducer sumará y emitirá:

false   2
true    3

📊 4️⃣ Tu salida final
false   187
true    1357


💡 Esto significa:

187 reseñas negativas (no recomendaron el juego)

1357 reseñas positivas (sí recomendaron el juego)

Total = 1544 reseñas procesadas.



 - El job de hive crea una tabla games con los juegos únicos (con las columnas app_id, y app_name), crea una tabla game_recommendation que resume para cada juego sus reseñas, y sus respectivas recommended, voted_helpful y voted_funny

'''
jobs
-> hadoop
  -> mapper.py
  -> reducer.py
  -> output
    -> success
    -> parte-00000
    -> parte-00001
    -> parte-00002

->hive
  -> success
  -> dsfnjdsfafsda // defrente los output


 '''

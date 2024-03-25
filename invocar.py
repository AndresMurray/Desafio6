import desafio
peliculas= desafio.input_movies()
promedio = desafio.average_calculation(peliculas)
cant=desafio.max_average(peliculas,promedio)
print(f"el promedio es {promedio}")
print(f"la cantidad de peliculas con mayor duracion al promedio son: {cant}")
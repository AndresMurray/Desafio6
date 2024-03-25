
def input_movies():
    """ This function returns a list with the duration in minutes of the movies """

    minutes = int(input("Ingresá la duración de una película de Dragon Ball (0 para finalizar)"))
    movies_duration  = []
    while minutes != 0:
        movies_duration .append(minutes)
        minutes = int(input("Ingresá la duración de una película de Dragon Ball (0 para finalizar)"))

    return movies_duration

def average_calculation(movies_duration):
    """ This function calculates the average of the lengths of the movies received by parameter.
    movies_duration: is a list with the duration in minutes of the movies
    """
    len_movies = len(movies_duration)
    average = 0 if len_movies == 0 else sum(movies_duration) / len_movies
    return average

def max_average(movies, duracion):
    """ This function returns how many movies are more long than the average """
    cant=0
    for i in movies:
        if i>duracion:
            cant=cant+1
    return cant
if __name__ == "__main__":
  movies = input_movies()
  duracion = average_calculation(movies)
  cant= max_average(movies, duracion)

  print (f"la duracion promedio de las peliculas es: {duracion}")
  print (f"la cantidad que supera el promedio es: {cant}")


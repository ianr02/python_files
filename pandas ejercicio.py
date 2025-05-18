# Ian Aaron Renderos Garcia
# Carne 24604
# Algoritmos y Programación Basica Universidad del Valle de Guatemala

import pandas as p

# si no corre, cambiar el path
doc = p.read_csv(open('TemarioA.csv'), index_col=0)

while True:
    print(f'\n1. ¿Qué género poblacional tiene un mejor rendimiento en promedio en las pruebas de matemáticas, lectura y escritura?\n'
          f'2. ¿Qué etnia tiene un mejor rendimiento en promedio en las pruebas de matemáticas, lectura y escritura?\n'
          f'3. ¿Qué prueba es en la que mejores resultados obtuvieron los estudiantes en promedio?\n'
          f'4. ¿Los estudiantes que se preparan para la prueba suelen tener un mejor rendimiento en las pruebas de matemáticas?\n'
          f'5. ¿Cuál es el promedio del puntaje en las pruebas de lectura según el nivel de educación escolar de los padres?\n'
          f'6. ¿Cuántos estudiantes tuvieron una comida "standard" antes de tomar alguna prueba.\n'
          f'7. Salir del programa\n')
    opcion = input("¿Qué deseas saber? (escoga la opcion numerica): ")
    print()
    if opcion == "1":
        # promedio general
        doc["Promedio en general"] = (doc["math_score"] + doc["writing_score"] + doc["reading_score"]) / 3
        promedios = doc.groupby('gender')['Promedio en general'].mean().sort_values(ascending=False).head(1)
        print(f'Promedio General:\n{promedios}\n'
              f'Analizando el promedio general entre hombres y mujeres, las mujeres poseen un mejor rendimiento basandose en el promedio de las pruebas respecto a los hombres\n')
        # promedio por prueba
        mate = doc.groupby('gender')['math_score'].mean().sort_values(ascending=False)
        lec = doc.groupby('gender')['reading_score'].mean().sort_values(ascending=False)
        scrib = doc.groupby('gender')['writing_score'].mean().sort_values(ascending=False)
        print(f'Promedio de Matematicas entre hombre y mujeres:\n{mate}\n'
              f'Basandose en el promedio del examen de matematicas, se concluye que los hombres tuvieron un mejor rendimiento\n'
              f'\nPromedio de Lectura entre hombre y mujeres:\n {lec}\n'
              f'Basandose en el promedio del examen de lectura, se concluye que las mujeres tuvieron un mejor rendimiento\n'
              f'\nPromedio Escritura entre hombre y mujeres:\n{scrib}\n'
              f'Basandose en el promedio del examen de escritura, se concluye que las mujeres tuvieron un mejor rendimiento')
    elif opcion == "2":
        # promedio general
        doc["Promedio en general"] = (doc["math_score"] + doc["writing_score"] + doc["reading_score"]) / 3
        promedios = doc.groupby('race_ethnicity')['Promedio en general'].mean().sort_values(ascending=False).head(1)
        print(f'Promedio General:\n{promedios}\n'
              f'Analizando el promedio general entre grupos etnicos, el grupo E posee un mejor rendimiento basandose en el promedio de las pruebas respecto al resto de grupos\n')
        # promedio por prueba
        mate = doc.groupby('race_ethnicity')['math_score'].mean().sort_values(ascending=False).head(1)
        lec = doc.groupby('race_ethnicity')['reading_score'].mean().sort_values(ascending=False).head(1)
        scrib = doc.groupby('race_ethnicity')['writing_score'].mean().sort_values(ascending=False).head(1)
        print(f'Promedio de Matematicas entre hombre y mujeres:\n{mate}\n'
              f'Analizando el promedio del examen de matematicas entre grupos etnicos, el grupo E posee un mejor rendimiento basandose en el promedio de las pruebas respecto al resto de grupos'
              f'\nPromedio de Lectura entre hombre y mujeres:\n {lec}\n'
              f'Analizando el promedio del examen de lectura entre grupos etnicos, el grupo E posee un mejor rendimiento basandose en el promedio de las pruebas respecto al resto de grupos'
              f'\nPromedio Escritura entre hombre y mujeres:\n{scrib}\n'
              f'Analizando el promedio del examen de escritura entre grupos etnicos, el grupo E posee un mejor rendimiento basandose en el promedio de las pruebas respecto al resto de grupos')
    elif opcion == "3":
        Matematicas = doc['math_score'].mean()
        Lectura = doc['reading_score'].mean()
        Escritura = doc['writing_score'].mean()
        print(f'Promedio de Matematicas = {Matematicas}\n'
              f'Promedio de Lectura = {Lectura}\n'
              f'Promedio Escritura = {Escritura}\n'
              f'Se concluyen que en la prueba de lectura se obtuvieron los mejores resultados')
    elif opcion == "4":
        mate2 = doc.groupby('test_preparation_course')['math_score'].mean().sort_values(ascending=False).head(1)
        print(mate2)
        print(f'\nSe puede concluir que las personas que hacen un test de preparacion previamente tienden a tener un mejor rendimiento que los que no lo hacen')
    elif opcion == "5":
        papas = doc.groupby('parental_level_of_education')['reading_score'].mean().sort_values(ascending=False).head(1)
        print(papas)
        print(f'\nSe puede concluir que las personas cuyos padres tienen una maestria tienen un mejor rendimiento')
    elif opcion == "6":
        comida = doc[doc['lunch'] == 'standard']
        comida = comida.count()['lunch']
        print(f'{comida} estudiantes tuvieron una comida standard antes de cada prueba\n')
    elif opcion == "7":
        print('Adios')
        break
    else:
        print('Esa opcion no existe\n')

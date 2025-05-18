# Ian Aaron Renderos Garcia
# Carne 24604
# Algoritmos y Programación Basica Universidad del Valle de Guatemala

import pandas as pd
import matplotlib.pyplot as plt

# Utilice encoding latin1 debido a que mi computadora no leia el archivo con utf8 y no sirve pues perdi el archivo csv

doc = pd.read_csv('/Users/ianrenderos/PycharmProjects/pythonProject1/vgsales.csv', encoding='Latin-1', index_col=0)


def genero(generoi):
    generoreview = doc[doc['Genre'] == generoi][['Game Title','Review']].sort_values(by=['Review'],ascending=False).head(3)
    print(f'Aqui estan los mejores 3 juegos de este genero segun Metacritic: \n{generoreview}\n\n')


while True:
    print('1. Mostrar un listado de las 5 plataformas, 5 publicadores y los 5 géneros más populares de juegos.\n'
          '2. Mostrar la media y la desviación estándar de las ventas de cada región.\n'
          '3. Ingrese el nombre de un juego mostrara el género, publicador y ventas globales en millones\n'
          '4. Escoje un género de videojuegos, y sugerirle los 3 mejores juegos de ese género\n'
          '5. Mostrar en una gráfica de barras, clasificado por género, la media de unidades vendidas por cada región\n'
          '6. Ingrese el nombre de un videojuego y mostrar en una gráfica de; porcentaje de unidades vendidas por región\n')
    opcion = input('Ingrese la opción que desea numericamente: ')
    if opcion == '1':
        compania = doc.groupby('Platform')['Platform'].count().sort_values(ascending=False).head(5)
        publicador = doc.groupby('Publisher')['Publisher'].count().sort_values(ascending=False).head(5)
        genero = doc.groupby('Genre')['Genre'].count().sort_values(ascending=False).head(5)
        print(f'Aqui esta un listado de las top 5 plataformas más populares: \n{compania}'
              f'\nAqui esta un listado de los top 5 publicadores más populares: \n{publicador}'
              f'\nAqui esta un listado de los top 5 generos más populares: \n{genero}\n')
    elif opcion == '2':
        japon = doc['Japan'].mean().round(2)
        japan1 = doc['Japan'].std().round(2)
        resto_mundo = doc['Rest of World'].mean().round(2)
        resto_mundo1 = doc['Rest of World'].std().round(2)
        america = doc['North America'].mean().round(2)
        america1 = doc['North America'].std().round(2)
        europa = doc['Europe'].mean().round(2)
        europa1 = doc['Europe'].std().round(2)
        print(f'Aqui esta la media y desviación estandar de ventas en Japon:\nMedia: {japon}\nDesviación Estandar: {japan1}\n'
              f'Aqui esta la media y desviación estandar de ventas en Europa:\nMedia: {europa}\nDesviación Estandar: {europa1}\n'
              f'Aqui esta la media y desviación estandar de ventas en Norte America:\nMedia: {america}\nDesviación Estandar: {america1}\n'
              f'Aqui esta la media y desviación estandar de ventas en el Resto del Mundo:\nMedia: {resto_mundo}\nDesviación Estandar: {resto_mundo1}\n')
    elif opcion == '3':
        juego = input('Ingrese el nombre del videojuego que desea saber su información: ')
        juego = juego.title()
        check = doc['Game Title'].tolist()
        doc['Ventas Globales'] = doc['North America'] + doc['Europe'] + doc['Japan'] + doc['Rest of World']
        if juego in check:
            ijuego = doc[doc['Game Title'] == juego][['Genre', 'Publisher', 'Ventas Globales']]
            print(f'Aqui esta la informaciond de tu juego:\n {ijuego}\n\n')
        else:
            print('El juego no existe en la base de datos\n')
    elif opcion == '4':
        print(f'1. Action\n'
              f'2. Adventure\n'
              f'3. Fighting\n'
              f'4. Misc\n'
              f'5. Platform\n'
              f'6. Puzzle\n'
              f'7. Racing\n'
              f'8. Role-Playing\n'
              f'9. Shooter\n'
              f'10. Simulation\n'
              f'11. Sports\n'
              f'12. Strategy\n')
        generoi = input('Ingrese el nombre del genero que desee saber: ')
        if generoi == '1':
            generoi = 'Action'
            genero(generoi)
        elif generoi == '2':
            generoi = 'Adventure'
            genero(generoi)
        elif generoi == '3':
            generoi = 'Fighting'
            genero(generoi)
        elif generoi == '4':
            generoi = 'Misc'
            genero(generoi)
        elif generoi == '5':
            generoi = 'Platform'
            genero(generoi)
        elif generoi == '6':
            generoi = 'Puzzle'
            genero(generoi)
        elif generoi == '7':
            generoi = 'Racing'
            genero(generoi)
        elif generoi == '8':
            generoi = 'Role-Playing'
            genero(generoi)
        elif generoi == '9':
            generoi = 'Shooter'
            genero(generoi)
        elif generoi == '10':
            generoi = 'Simulation'
            genero(generoi)
        elif generoi == '11':
            generoi = 'Sports '
            genero(generoi)
        elif generoi == '12':
            generoi = 'Strategy'
            genero(generoi)
        else:
            print('Ese genero no existe\n')
    elif opcion == '5':
        porgenero = doc.groupby('Genre')[['Japan', 'Europe', 'North America', 'Rest of World']].mean().round(2)
        porgenero.plot(kind='bar', xlabel='Genero', ylabel='Unidades en millones', title='Media de videojuegos vendidos por región ')
        plt.show()
    elif opcion == '6':
        check = doc['Game Title'].tolist()
        juego2 = input('Ingrese el nombre del videojuego que se desea saber su información: ')
        juego2 = juego2.title()
        if juego2 in check:
            labels = ['Japan', 'Europe', 'North America', 'Rest of World']
            wea = doc[doc['Game Title'] == juego2][['Japan', 'Europe', 'North America', 'Rest of World']]
            size = [wea['Japan'].mean(), wea['Europe'].mean(), wea['North America'].mean(), wea['Rest of World'].mean()]
            fig, ax = plt.subplots()
            ax.pie(size, labels=labels, autopct='%1.1f%%')
            plt.title(f'Ventas de {juego2} en las regiones de ventas (en millones)')
            plt.show()
        else:
            print('El juego no existe en la base de datos')
    elif opcion == '7':
        print('Saliendo del programa')
        break
    else:
        print('Opcion no existente, ingrese otra opcion de nuevo\n')

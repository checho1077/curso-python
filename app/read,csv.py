import csv 
import matplotlib.pyplot as plt 

def read_csv(ruta):
    with open(ruta, 'r') as file:
        read = csv.reader(file, delimiter=',')
        header = next(read)
        datainf = []
        for row in read:
            iterable = (zip(header, row))
            country_dict = {key: value for key, value in iterable}
            datainf.append(country_dict)
        return datainf

def bar_chart(claves, valores):
    fig, ax = plt.subplots()
    ax.bar(claves, valores)
    plt.savefig('chart.png')
    plt.show()
    plt.close()

if __name__ == '__main__':
    datainf = read_csv('data.csv')
    omitir = ["Rank", "CCA3", "Capital", "Continent", "Area (km²)", 'Density (per km²)', 'Growth Rate', 'World Population Percentage']
    nuevo_dict = [{clave: valor for clave, valor in c.items() if clave not in omitir} for c in datainf]
    pais_a_buscar = input("Ingrese un país: ")

    paises_encontrados = [country for country in datainf if country['Country/Territory'].lower() == pais_a_buscar.lower()]

    if paises_encontrados:
        for pais_encontrado in paises_encontrados:
            print(f"Información para {pais_a_buscar}:")
            claves = []
            valores = []
            for clave, valor in pais_encontrado.items():
                if clave not in omitir:
                    print(f"{clave}: {valor}")
                    claves.append(clave)
                    valores.append(valor)  # Asumiendo que los valores son números, ajusta según tus datos

            # Crear y mostrar el gráfico de barras
            bar_chart(claves, valores)
    else:
        print(f"No se encontró información para {pais_a_buscar}.")

  
  
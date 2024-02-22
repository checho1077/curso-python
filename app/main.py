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
    
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels= labels)
    ax.axis('equal')
    plt.savefig('bar_chart.png')
    plt.show()
    plt.close()
    
if __name__ == '__main__':
    datainf = read_csv('data.csv')
    world = [row['World Population Percentage'] for row in datainf]
    country = [row['Country/Territory'] for row in datainf]
    generate_pie_chart(country, world)

  
import matplotlib.pyplot as plt
 
def bar_chart():
 labels = ['a', ' b ', 'c' ]
 values= [100, 200, 80 ]
          
 fig, ax = plt.subplots()
 ax.pie(values, labels= labels)
 plt.savefig("pie.png")
 plt.close()

if __name__ == '__main__':
  bar_chart()
  
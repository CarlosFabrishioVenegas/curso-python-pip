
import read_csv
import charts

def run():
  data = read_csv.read_csv('./app/data.csv')
  #data = list(filter(lambda item : item['Continent'] == 'South America',data))
  print(list(filter(lambda item : item['Continent'],data)))
  '''
  ejex=input('Deberas colocar el eje que desees graficar')
  ejey=input('Deberas colocar el valor del eje que desees graficar')
  countries = list(map(lambda x: x[ejex], data))
  percentages = list(map(lambda x: x[ejey], data))
  charts.generate_pie_chart(countries, percentages)
  '''
  
if __name__ == '__main__':
  run()
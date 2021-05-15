import matplotlib.pyplot as plt
import pandas
import scipy

experiment = [388.2 , 387.5, 388, 387.1, 388.8 , 387.5, 387.1, 388.3, 388.1, 388.5, 387.7, 388.9,
388.2, 388.3, 387.7, 388.7, 389, 388, 388.5, 388.2, 387, 388, 388.4,
388.4, 387.1, 388.3, 388.4, 388.5, 387, 388.7, 387.1, 388.8, 388.9, 387.8, 387.9, 387.6, 388.9, 387.9, 388.2, 389.4]

df = pandas.DataFrame(data={
    'experiment': experiment
})

df.to_csv("experiment.csv")

df1 = pandas.read_csv("experiment.csv")

df12 = pandas.DataFrame(data={
    'df1': df1['experiment'],
})

# Плотность распределения
df12.plot.kde()
plt.title('Плотность распределения')
d1 = df12['df1']
print()
print('Из теста Колмагорова - Смирнова:')
print(scipy.stats.kstest(d1, 'norm', (d1.mean(), d1.std()), N=len(d1)))

plt.show()

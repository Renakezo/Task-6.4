import pandas as pd

data = pd.read_csv('data.csv')
average = data['salary'].mean()
filtered_data = data[data['age'] > 30]

print(f'Средняя зарплата сотрудников: {average}')
print(f'Сотрудники старше 30 лет:')
print(filtered_data)
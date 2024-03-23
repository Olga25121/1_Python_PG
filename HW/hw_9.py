# # Pandas

# # 1. Дан файл california_housing_train.csv. 
# # Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
# # Используйте модуль pandas.

# import pandas as pd
# data = pd.read_csv('california_housing_train.csv')
# avg = data[(data['population'] < 500) & (data['population'] > 0)]['median_house_value'].mean()

#      # Автотест
# import pandas as pd

# df = pd.read_csv('california_housing_train.csv')
# avg = df[(df['population'] > 0) & (df['population'] < 500)]['median_house_value'].mean()  # Средняя стоимость дома, где количество людей от 0 до 500


# # 2. Дан файл california_housing_train.csv.
# # Найти максимальное значение переменной "households" в зоне минимального значения переменной min_population и 
# # сохраните это значение в переменную max_households_in_min_population.
# # Используйте модуль pandas.

# import pandas as pd
# data = pd.read_csv('california_housing_train.csv')
# min_population = data['population'].min()
# max_households_in_min_population = data[data['population'] == min_population]['households'].max()

#        # Автотест
# import pandas as pd

# df = pd.read_csv('california_housing_train.csv')
# # Найти минимальное значение 'population'
# min_population = df['population'].min()

# # Отфильтровать строки с минимальным значением 'population' и найти максимальное значение 'households'
# max_households_in_min_population = df[df['population'] == min_population]['households'].max()


import json

import pandas as pd

from constants import ITEMS_AMOUNT_FOR_DISTRIBUTION

data = []

with open('os_and_version.json', 'r') as file:
    lines = []
    for i, line in enumerate(file):
        if line.strip():
            try:
                json_data = json.loads(line)
                if ('os' in json_data and 'version' in json_data):
                    data.append(json_data)
                    if i + 1 == ITEMS_AMOUNT_FOR_DISTRIBUTION:
                        break
                else:
                    print("Отсутствует ключ 'os' или 'version' "
                          "или их значение пусто: ", json_data)
            except json.JSONDecodeError:
                print("Ошибка декодирования JSON: ", line)

print('Количество записей, которые использованы для '
      'построения распределения:', len(data))

df = pd.DataFrame(data)

distribution = df.groupby(['os', 'version']).size().reset_index(name='count')
distribution = distribution.sort_values(by='count', ascending=False)

print(distribution.drop('os', axis=1).to_string(index=False))

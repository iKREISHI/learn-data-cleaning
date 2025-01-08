import pandas as pd
import numpy as np
import re


if __name__ == "__main__":
    # Загрузка датасета
    dataset = pd.read_csv('movies.csv')

    # Вывод Series ['runtime'] для детального просмотра данных
    print(dataset['runtime'])

    # Вывод уникальных значений по Series ['runtime']
    print(dataset['runtime'].unique())


    # Написание функции для очистки runtime от нецифровых символов
    def clear_runtime(runtime):
        match = re.search(r'\d+', str(runtime))  # Ищем цифровое значение
        return int(match.group()) if match else ''  # Возвращаем число или пустую строку


    # Применение функции к Series ['runtime']
    dataset['runtime_clear'] = dataset['runtime'].apply(clear_runtime)

    # Вывод Series ['runtime_clear'] для оценки результата
    print(dataset['runtime_clear'])

    # Проверка поля по индексу 4997
    print(dataset['runtime_clear'][4997])
    print(type(dataset['runtime_clear'][4997]))

    # Фильтрация датасета, исключающая строки с пустыми значениями в runtime_clear
    dataset = dataset[dataset['runtime_clear'] != '']

    # Приведение признака runtime_clear к формату int
    dataset['runtime_clear'] = dataset['runtime_clear'].astype(int)

    # Оценка размеров датасета
    print(dataset.shape)


    # Проверка типов данных
    def clear_gross_earn(gross_earn):
        if pd.isna(gross_earn):
            return np.nan
        else:
            return re.sub(r'[^\d\.]', '', gross_earn)


    # Применение функции к Series ['gross_earn']
    dataset['gross_earn_clear'] = dataset['gross_earn'].apply(clear_gross_earn)

    # Приведение признака gross_earn_clear к формату float
    dataset['gross_earn_clear'] = dataset['gross_earn_clear'].astype(float)

    # Исключаем строки, где gross_earn_clear содержит NaN
    dataset = dataset[dataset['gross_earn_clear'].notna()]

    # Проверка преобразований gross_earn
    print(dataset['gross_earn_clear'])

    # Проверка итогового размера датасета
    print(dataset.shape)

    # Сортировка датасета по убыванию рейтинга
    sorted_dataset = dataset.sort_values(by='rating', ascending=False)

    # Переопределение индексов
    sorted_dataset.reset_index(drop=True, inplace=True)

    # Сохранение итогового датасета
    sorted_dataset.to_csv('movies_clean.csv', index=False)
    print("Финальный датасет сохранён как 'movies_clean.csv'")


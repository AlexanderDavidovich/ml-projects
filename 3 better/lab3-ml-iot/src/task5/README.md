# Задание 5: Создание приложений Panel App и Voila

## 📋 Описание

Создание интерактивных дашбордов и веб-приложений из Jupyter Notebooks.

## 🎯 Две части задания

### Часть 1: Panel App
Создание приложения с использованием библиотеки Panel.

### Часть 2: Voila App
Преобразование Jupyter Notebook в веб-приложение с помощью Voila.

## 📚 Необходимые статьи

Согласно методичке, нужно изучить:

1. **"Publish a Notebook as a Dashboard Using the Layout Builder"**
   - Поиск в Google: "Panel publish notebook as dashboard layout builder"
   - Или: https://panel.holoviz.org/

2. **"Build Dashboard"**
   - Документация Panel по созданию дашбордов
   - https://panel.holoviz.org/tutorials/

3. **"How to Deploy a Panel Visualization Dashboard to GitHub Pages"**
   - Публикация приложения
   - Поиск: "deploy panel dashboard github pages"

4. **"And Voilà!"**
   - Статья о Voila
   - https://voila.readthedocs.io/

## 🚀 Быстрый старт

### Установка библиотек

```bash
# Panel
pip install panel hvplot

# Voila
pip install voila

# Дополнительные библиотеки для визуализации
pip install plotly bokeh holoviews
```

### Пример 1: Простой Panel Dashboard

Создайте файл `panel_example.ipynb`:

```python
import panel as pn
import numpy as np
import matplotlib.pyplot as plt

pn.extension()

# Создание интерактивного слайдера
freq_slider = pn.widgets.FloatSlider(
    name='Частота', 
    start=1, 
    end=10, 
    step=0.1, 
    value=5
)

# Функция для построения графика
def plot_sine(freq):
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(freq * x)
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y)
    ax.set_title(f'Синусоида с частотой {freq}')
    ax.set_xlabel('x')
    ax.set_ylabel('sin(x)')
    plt.close(fig)
    return fig

# Создание дашборда
dashboard = pn.Column(
    '# Интерактивный график синусоиды',
    freq_slider,
    pn.bind(plot_sine, freq_slider)
)

dashboard.servable()
```

**Запуск Panel App:**
```bash
panel serve panel_example.ipynb --show
```

### Пример 2: Voila App

Создайте файл `voila_example.ipynb`:

```python
import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np

# Интерактивный виджет
slider = widgets.FloatSlider(
    value=5,
    min=1,
    max=10,
    step=0.1,
    description='Частота:',
)

output = widgets.Output()

def update_plot(change):
    with output:
        output.clear_output(wait=True)
        x = np.linspace(0, 2*np.pi, 100)
        y = np.sin(change['new'] * x)
        
        plt.figure(figsize=(8, 4))
        plt.plot(x, y)
        plt.title(f'Синусоида с частотой {change["new"]}')
        plt.xlabel('x')
        plt.ylabel('sin(x)')
        plt.show()

slider.observe(update_plot, names='value')

# Инициализация
update_plot({'new': slider.value})

display(slider, output)
```

**Запуск Voila:**
```bash
voila voila_example.ipynb
```

## 📝 Что нужно сделать

### Задание 5.1: Panel App

1. Изучите статью "Publish a Notebook as a Dashboard"
2. Создайте блокнот с интерактивными виджетами
3. Настройте Layout Builder
4. Добавьте вкладки и компоненты
5. Предоставьте совместный доступ через Share
6. Опубликуйте на GitHub Pages (опционально)

### Задание 5.2: Voila App

1. Изучите статью "And Voilà!"
2. Создайте блокнот с виджетами ipywidgets
3. Запустите через Voila
4. Сравните с Panel App

## 🎨 Идеи для дашборда

- Анализ данных из предыдущих заданий
- Визуализация списка студентов
- Интерактивные графики
- Фильтрация и поиск данных
- Статистические показатели

## 📊 Минимальные требования

Ваш дашборд должен содержать:
- Как минимум 2 интерактивных виджета
- Визуализацию данных (график/таблица)
- Текстовое описание
- Структурированный Layout

## 🔗 Полезные ссылки

- Panel Documentation: https://panel.holoviz.org/
- Voila Documentation: https://voila.readthedocs.io/
- Panel Gallery: https://panel.holoviz.org/gallery/
- Voila Gallery: https://voila-gallery.org/

## ⏱️ Время выполнения

- Изучение документации: 30-40 минут
- Создание Panel App: 20-30 минут
- Создание Voila App: 15-20 минут
- **Итого: 1.5-2 часа**

## 💡 Совет

Начните с простого примера, потом добавляйте функционал постепенно.

## 📤 Экспорт

После завершения:
1. Сохраните блокноты (.ipynb)
2. Экспортируйте в HTML
3. Сделайте скриншоты работающих приложений
4. Загрузите на GitHub

## 🎯 Критерии оценки

- ✅ Работающее Panel приложение
- ✅ Работающее Voila приложение
- ✅ Интерактивность
- ✅ Качество визуализации
- ✅ Код документирован
- ✅ Экспортировано в HTML/PDF

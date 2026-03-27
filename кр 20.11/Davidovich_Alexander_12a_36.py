# Фамилия_Имя_группа_6.ipynb

# Импорт необходимых библиотек
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import warnings
warnings.filterwarnings('ignore')

# Определяем путь к папке с данными
current_script_path = os.path.abspath(__file__)
current_script_dir = os.path.dirname(current_script_path)

print(f"Скрипт запущен из: {current_script_dir}")

# Загрузка данных с правильными путями
try:
    train_df = pd.read_csv(os.path.join(current_script_dir, 'train.csv'))
    test_df = pd.read_csv(os.path.join(current_script_dir, 'test.csv'))
    print("Файлы успешно загружены!")
except Exception as e:
    print(f"Ошибка загрузки файлов: {e}")
    # Альтернативный способ - попробовать загрузить из подпапки
    try:
        train_df = pd.read_csv('train.csv')
        test_df = pd.read_csv('test.csv')
        print("Файлы загружены из текущей директории!")
    except:
        print("Не удалось загрузить файлы. Проверьте пути.")
        exit()

# Просмотр структуры данных
print("\nРазмер тренировочных данных:", train_df.shape)
print("Размер тестовых данных:", test_df.shape)
print("\nПервые 5 строк тренировочных данных:")
print(train_df.head())
print("\nИнформация о тренировочных данных:")
print(train_df.info())

# Выбор необходимых признаков
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
target = 'Survived'

# Создание X и y
X = train_df[features]
y = train_df[target]

# Разделение на тренировочную и тестовую выборки (80%/20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nРазмеры выборок:")
print(f"X_train: {X_train.shape}")
print(f"X_test: {X_test.shape}")
print(f"y_train: {y_train.shape}")
print(f"y_test: {y_test.shape}")

# Проверка пропущенных значений
print("\nПропущенные значения в тренировочных данных:")
print(X_train.isnull().sum())

# Определение числовых и категориальных признаков
numeric_features = ['Age', 'Fare']
categorical_features = ['Sex', 'Embarked', 'Pclass']

# Создание трансформеров для числовых и категориальных признаков
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Объединение трансформеров в ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Создание полного пайплаина с моделью kNN
knn_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', KNeighborsClassifier(n_neighbors=5))
])

# Обучение модели
print("\nОбучение модели kNN...")
knn_pipeline.fit(X_train, y_train)

# Предсказание на тестовых данных
y_pred = knn_pipeline.predict(X_test)

# Вычисление метрик
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Вывод метрик
print("\n" + "="*50)
print("МЕТРИКИ КАЧЕСТВА МОДЕЛИ")
print("="*50)
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")

print("\n" + "="*50)
print("ОТЧЕТ ПО КЛАССИФИКАЦИИ")
print("="*50)
print(classification_report(y_test, y_pred, target_names=['Not Survived', 'Survived']))

# Ответ на вопрос о качестве модели
print("\n" + "="*50)
print("АНАЛИЗ РЕЗУЛЬТАТОВ")
print("="*50)
print("Почему результат kNN может быть хуже, чем у других моделей?")
print("1. Чувствительность к шуму: kNN чувствителен к выбросам и шуму в данных")
print("2. Проклятие размерности: при большом количестве признаков расстояние между точками становится менее информативным")
print("3. Необходимость масштабирования: kNN требует масштабирования признаков")
print("4. Выбор параметра k: фиксированное значение k=5 может быть неоптимальным для данной задачи")
print("5. Вычислительная сложность: kNN требует хранения всех тренировочных данных для предсказания")
print("6. Чувствительность к несбалансированным данным")

# Дополнительный анализ
print(f"\nБаланс классов в целевой переменной:")
print(y_train.value_counts(normalize=True))

# Пример предсказания для нескольких пассажиров
print("\n" + "="*50)
print("ПРИМЕР ПРЕДСКАЗАНИЯ")
print("="*50)
sample_passengers = X_test.head(3)
sample_predictions = knn_pipeline.predict(sample_passengers)
sample_probabilities = knn_pipeline.predict_proba(sample_passengers)

for i, (idx, passenger) in enumerate(sample_passengers.iterrows()):
    actual = y_test.loc[idx]
    predicted = sample_predictions[i]
    probability = sample_probabilities[i][1]
    
    print(f"\nПассажир {i+1}:")
    print(f"  Класс: {passenger['Pclass']}, Пол: {passenger['Sex']}, Возраст: {passenger['Age']}")
    print(f"  Фактический результат: {'Выжил' if actual == 1 else 'Не выжил'}")
    print(f"  Предсказанный результат: {'Выжил' if predicted == 1 else 'Не выжил'}")
    print(f"  Вероятность выживания: {probability:.2f}")
    print(f"  Совпадение: {'✓' if actual == predicted else '✗'}")
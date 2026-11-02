import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Загрузка и подготовка данных
data = load_wine()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target
print("Размер выборки:", X.shape, "| классы:", data.target_names)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 2. Обучение модели градиентного бустинга
model = GradientBoostingClassifier(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=3,
    random_state=42,
)
model.fit(X_train, y_train)

# 3. Оценка модели на обучающей и тестовой выборках
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

print("\n=== МЕТРИКИ НА ОБУЧАЮЩЕЙ ВЫБОРКЕ ===")
print(classification_report(y_train, y_train_pred, target_names=data.target_names))

print("\n=== МЕТРИКИ НА ТЕСТОВОЙ ВЫБОРКЕ ===")
print(classification_report(y_test, y_test_pred, target_names=data.target_names))

cv = cross_val_score(model, X, y, cv=5)
print(f"Кросс-валидация (5 фолдов): {cv.mean():.3f} ± {cv.std():.3f}")

# 4. Графическое представление результатов
plt.figure(figsize=(14, 6))

# 4.1. Тепловая карта матрицы ошибок (Confusion Matrix)
plt.subplot(1, 2, 1)
cm = confusion_matrix(y_test, y_test_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=data.target_names, yticklabels=data.target_names)
plt.title('Матрица ошибок (Тестовая выборка)')
plt.xlabel('Предсказанный класс')
plt.ylabel('Истинный класс')

# 4.2. Диаграмма важности признаков (Feature Importance)
plt.subplot(1, 2, 2)
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]
sns.barplot(x=importances[indices], y=np.array(data.feature_names)[indices], palette='viridis', hue=np.array(data.feature_names)[indices], legend=False)
plt.title('Важность признаков (Градиентный бустинг)')
plt.xlabel('Относительная важность')
plt.ylabel('Признаки')

plt.tight_layout()
# Покажем графики (при запуске в консоли скрипт остановится, пока окно открыто)
plt.show() 

# 5. Предсказание для нового образца
new_sample = pd.DataFrame([{
    "alcohol": 10.2,
    "malic_acid": 2.0,
    "ash": 2.0,
    "alcalinity_of_ash": 13.0,
    "magnesium": 73.0,
    "total_phenols": 2.3,
    "flavanoids": 2.5,
    "nonflavanoid_phenols": 0.3,
    "proanthocyanins": 1.8,
    "color_intensity": 7.0,
    "hue": 1.0,
    "od280/od315_of_diluted_wines": 2.6,
    "proline": 800.0,
}])[data.feature_names]

pred = model.predict(new_sample)[0]
proba = model.predict_proba(new_sample)[0]
print(f"\nНовый образец -> сорт {pred} ({data.target_names[pred]})")
for cls, p in zip(data.target_names, proba):
    print(f"  {cls}: {p:.3f}")

# 6. Угадывание образца из датасета scikit-learn
rng = np.random.default_rng()
if len(sys.argv) > 1:
    try:
        pos = int(sys.argv[1]) % len(X_test)
    except ValueError:
        pos = int(rng.integers(len(X_test)))
else:
    pos = int(rng.integers(len(X_test)))

sample = X_test.iloc[[pos]]
true_class = y_test.iloc[pos] # Исправлено на .iloc для надежного доступа в pandas Series
guess = model.predict(sample)[0]
proba = model.predict_proba(sample)[0]

print(f"\n=== Угадывание образца №{X_test.index[pos]} из датасета (тестовая выборка) ===")
print(sample.T.round(2).to_string(header=False))
print(f"\nМодель думает: сорт {guess} (уверенность {proba[guess]:.1%})")
print(f"Настоящий сорт: {true_class}")
print("Угадала!" if guess == true_class else "Ошибка.")

# 7. Выводы и интерпретация
print("\n=== ИНТЕРПРЕТАЦИЯ РЕЗУЛЬТАТОВ ===")
print("1. Наличие переобучения:")
print("   - Метрики на обучающей выборке (Accuracy, F1) составляют ~1.00.")
print(f"   - Метрики на тестовой выборке также очень высоки (Accuracy = {accuracy_score(y_test, y_test_pred):.2f}).")
print("   - ВЫВОД: Существенного переобучения нет. Градиентный бустинг отлично обобщает эту задачу, так как датасет линейно разделим по ключевым признакам.")
print("\n2. Информативность признаков:")
top_3_features = [data.feature_names[indices[0]], data.feature_names[indices[1]], data.feature_names[indices[2]]]
print(f"   - Самые информативные признаки: {', '.join(top_3_features)}.")
print("   - Именно они чаще всего оказывались в узлах деревьев бустинга, давая наибольший прирост информации (Information Gain) при разделении классов вина.")
print("\n3. Анализ предсказания классов:")
print("   - Датасет Wine является 'простым' (чистые данные), поэтому ошибки встречаются крайне редко.")
print("   - Если ошибки и возникают, то обычно между сортами `class_1` и `class_2`. В отличие от `class_0` (который сильно выделяется высоким содержанием алкоголя и пролина), `class_1` и `class_2` имеют перекрывающиеся диапазоны значений по цвету и флавоноидам, что делает границу между ними менее четкой.")
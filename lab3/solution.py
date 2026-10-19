import pandas as pd
import matplotlib.pyplot as plt

# 1. Чтение данных (tr_mcc_codes и tr_types разделены символом ';')
tr_mcc_codes = pd.read_csv('data/tr_mcc_codes.csv', sep=';')
tr_types = pd.read_csv('data/tr_types.csv', sep=';')
transactions = pd.read_csv('data/transactions.csv', nrows=1000000)
customers_gender_train = pd.read_csv('data/gender_train.csv')

# 2. Соединение таблиц
df = transactions.merge(tr_mcc_codes, on='mcc_code', how='inner')
df = df.merge(tr_types, on='tr_type', how='inner')
df = df.merge(customers_gender_train, on='customer_id', how='left')
print('Строк после соединения:', len(df))  # ожидается 999584

# 3. Новый столбец: конкатенация mcc_code и tr_type
df['mcc_code+tr_type'] = df['mcc_code'].astype(str) + df['tr_type'].astype(str)

# 4. Только положительные amount
df = df[df['amount'] > 0]

# 5. Средние значения amount по категориям, где 5 <= число наблюдений <= 25
stats = df.groupby('mcc_code+tr_type')['amount'].agg(['mean', 'count'])
selected = stats[(stats['count'] >= 5) & (stats['count'] <= 25)]
answer = round(selected['mean'].mean(), 2)
print('Ответ:', answer)

# 6. Гистограмма по полученной таблице (значения amount)
plt.figure(figsize=(10, 6))
plt.hist(df['amount'], bins=50, color='steelblue', edgecolor='black')
plt.yscale('log')
plt.xlabel('amount')
plt.ylabel('Количество наблюдений (log)')
plt.title('Гистограмма amount (положительные значения)')
plt.tight_layout()
plt.show()

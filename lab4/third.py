import csv
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Шлях до файлу CSV
output_dir = r'd:\Project\lab4'
os.makedirs(output_dir, exist_ok=True)  # Переконайтеся, що директорія існує
csv_file = os.path.join(output_dir, 'employees.csv')

def calculate_age(birthdate):
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Завантаження даних з CSV
try:
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        print("Файл успішно завантажено.")
except FileNotFoundError:
    print("Файл CSV не знайдено.")
    exit()

# Лічильники статі
male_count = 0
female_count = 0

# Категорії віку
age_categories = {
    "younger_18": 0,
    "18-45": 0,
    "45-70": 0,
    "older_70": 0
}

# Статеві категорії по віку
gender_age_categories = {
    "younger_18": {"чоловік": 0, "жінка": 0},
    "18-45": {"чоловік": 0, "жінка": 0},
    "45-70": {"чоловік": 0, "жінка": 0},
    "older_70": {"чоловік": 0, "жінка": 0}
}

# Обробка рядків з даними
for row in data[1:]:
    gender = row[3]
    birthdate = datetime.strptime(row[4], '%Y-%m-%d')
    age = calculate_age(birthdate)

    # Лічильник статі
    if gender == 'чоловік':
        male_count += 1
    else:
        female_count += 1

    # Лічильник вікових категорій та розподіл за статтю
    if age < 18:
        age_categories["younger_18"] += 1
        gender_age_categories["younger_18"][gender] += 1
    elif 18 <= age <= 45:
        age_categories["18-45"] += 1
        gender_age_categories["18-45"][gender] += 1
    elif 45 < age <= 70:
        age_categories["45-70"] += 1
        gender_age_categories["45-70"][gender] += 1
    else:
        age_categories["older_70"] += 1
        gender_age_categories["older_70"][gender] += 1

# Виведення результатівф
print(f"Кількість чоловіків: {male_count}")
print(f"Кількість жінок: {female_count}")

# Створення графіків
plt.figure(figsize=(10, 5))

# Графік статі
plt.subplot(1, 2, 1)
plt.pie([male_count, female_count], labels=['чоловік', 'жінка'], autopct='%1.1f%%')
plt.title('Стать')

# Графік вікових категорій
plt.subplot(1, 2, 2)
age_category_labels = ['<18', '18-45', '45-70', '>70']
age_category_values = [age_categories[key] for key in age_categories]
plt.bar(age_category_labels, age_category_values)
plt.title('Категорії віку')

plt.show()

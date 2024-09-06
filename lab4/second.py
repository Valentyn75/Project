import csv
from openpyxl import Workbook
from datetime import datetime
import os

def calculate_age(birthdate):
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Встановлення шляху для файлу
output_dir = r'd:\Project\lab4'
os.makedirs(output_dir, exist_ok=True)  # Переконайтеся, що директорія існує
csv_file = os.path.join(output_dir, 'employees.csv')
xlsx_file = os.path.join(output_dir, 'employees.xlsx')

# Завантаження даних з CSV
try:
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
except FileNotFoundError:
    print("Файл CSV не знайдено.")
    exit()

wb = Workbook()

age_categories = {
    "all": [],
    "younger_18": [],
    "18-45": [],
    "45-70": [],
    "older_70": []
}

header = ['№', 'Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік']

# Заповнення категорій
for i, row in enumerate(data[1:], start=1):
    birthdate = datetime.strptime(row[4], '%Y-%m-%d')
    age = calculate_age(birthdate)
    record = [i] + row[:4] + [row[4], age]

    age_categories['all'].append(record)
    if age < 18:
        age_categories['younger_18'].append(record)
    elif 18 <= age <= 45:
        age_categories['18-45'].append(record)
    elif 45 < age <= 70:
        age_categories['45-70'].append(record)
    else:
        age_categories['older_70'].append(record)

# Запис до XLSX
try:
    for category, records in age_categories.items():
        ws = wb.create_sheet(title=category)
        ws.append(header)
        for record in records:
            ws.append(record)

    wb.save(xlsx_file)
    print(f"XLSX файл успішно створено за шляхом {xlsx_file}")
except Exception as e:
    print(f"Помилка при створенні XLSX файлу: {e}")

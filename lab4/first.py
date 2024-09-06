import csv
import random
import pandas as pd
from faker import Faker
from datetime import datetime
import os

# Налаштування для генерації даних
fake = Faker('uk_UA')  # Ukrainian locale for realistic names and addresses
total_records = 2000
male_percentage = 0.6
female_percentage = 0.4
male_count = int(total_records * male_percentage)
female_count = total_records - male_count

# Поля для CSV файлу
fields = ['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 
          'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email']

# Функція для генерації даних людини
def generate_person(gender):
    last_name = fake.last_name_male() if gender == 'чоловік' else fake.last_name_female()
    first_name = fake.first_name_male() if gender == 'чоловік' else fake.first_name_female()
    middle_name = fake.middle_name_male() if gender == 'чоловік' else fake.middle_name_female()
    dob = fake.date_of_birth(minimum_age=16, maximum_age=85)
    position = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()
    
    return [last_name, first_name, middle_name, gender, dob.strftime('%Y-%m-%d'), 
            position, city, address, phone, email]

# Встановлення шляху для файлу
output_dir = r'd:\Project\lab4'
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'employees.csv')

# Створення CSV файлу
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    
    for _ in range(male_count):
        writer.writerow(generate_person('чоловік'))
        
    for _ in range(female_count):
        writer.writerow(generate_person('жінка'))

print(f"CSV file with 2000 employees has been created at {output_file}.")

# Використання pandas для читання CSV файлу та обробки даних
try:
    # Читання даних за допомогою pandas
    df = pd.read_csv(output_file, encoding='utf-8')
    
    # Виведення перших 5 записів для перевірки
    print("Перші 5 записів з файлу:")
    print(df.head())
    
    # Приклад маніпуляції з даними: групування за статтю і підрахунок
    gender_counts = df['Стать'].value_counts()
    print("\nКількість чоловіків та жінок:")
    print(gender_counts)
    
except FileNotFoundError:
    print("Файл CSV не знайдено.")
except Exception as e:
    print(f"Помилка при читанні CSV файлу: {e}")

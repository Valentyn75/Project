import os
import re
from testModul.gtrans import TransLate, LangDetect
from testModul.gtrans import LanguageList as gtransLanguageList
from testModul.deeptr import LanguageList as deeptrLanguageList


def read_config(config_file):
    """Зчитує конфігураційний файл і повертає параметри у вигляді словника."""
    config = {}
    try:
        with open(config_file, 'r', encoding='utf-8') as file:
            for line in file:
                name, value = line.strip().split('=')
                config[name.strip()] = value.strip()
        return config
    except FileNotFoundError:
        print("Конфігураційний файл не знайдено.")
        exit(1)
    except Exception as e:
        print(f"Помилка читання конфігураційного файлу: {e}")
        exit(1)

def analyze_text(text):
    """Аналізує текст і повертає кількість символів, слів та речень."""
    num_chars = len(text)
    num_words = len(re.findall(r'\b\w+\b', text))
    num_sentences = len(re.findall(r'[.!?]', text))
    return num_chars, num_words, num_sentences

def main():
    config = read_config('D:\\Project\\lab3\\config.txt')
    
 # Використання функцій з gtrans.py
    print("=== Використання googletrans ===")
    print(gtransLanguageList("screen", "Добрий день"))
    
    # Використання функцій з deeptr.py
    print("=== Використання deep_translator ===")
    print(deeptrLanguageList("screen", "Добрий день"))

    # Зчитування параметрів з конфігураційного файлу
    text_file = config.get('text_file')
    dest_lang = config.get('dest_lang')
    output = config.get('output')
    max_chars = int(config.get('max_chars', 600))
    max_words = int(config.get('max_words', 100))
    max_sentences = int(config.get('max_sentences', 10))
    
    if not os.path.exists(text_file):
        print(f"Файл {text_file} не знайдено.")
        return
    
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Аналіз тексту
    num_chars, num_words, num_sentences = analyze_text(text)
    print(f"Назва файлу: {text_file}")
    print(f"Розмір файлу: {num_chars} символів")
    print(f"Кількість символів: {num_chars}")
    print(f"Кількість слів: {num_words}")
    print(f"Кількість речень: {num_sentences}")
    
    # Визначення мови тексту
    language = LangDetect(text, "lang")
    print(f"Мова тексту: {language}")
    
    # Читання тексту з файлу до виконання однієї з умов
    limited_text = ''
    current_chars, current_words, current_sentences = 0, 0, 0
    
    for line in text.splitlines():
        for sentence in re.split(r'(?<=[.!?]) +', line):
            limited_text += sentence + ' '
            current_chars += len(sentence)
            current_words += len(re.findall(r'\b\w+\b', sentence))
            current_sentences += 1
            
            if current_chars >= max_chars or current_words >= max_words or current_sentences >= max_sentences:
                break
        if current_chars >= max_chars or current_words >= max_words or current_sentences >= max_sentences:
            break
    
    # Переклад тексту
    translated_text = TransLate(limited_text.strip(), 'auto', dest_lang)
    
    # Вивід результатів
    if output == 'screen':
        print(f"Переклад на мову {dest_lang}:")
        print(translated_text)
    elif output == 'file':
        output_file = f"{os.path.splitext(text_file)[0]}_{dest_lang}.txt"
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(translated_text)
            print("Ok")
        except Exception as e:
            print(f"Помилка запису у файл: {e}")

if __name__ == "__main__":
    main()
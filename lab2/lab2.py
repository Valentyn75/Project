from langdetect import detect, DetectorFactory
from langdetect import detect_langs
from googletrans import Translator
import pycountry

# Фіксуємо результат для детермінованості
DetectorFactory.seed = 0

# Функція для визначення коду мови за текстом
def LangDetect(txt):
    lang_code = detect(txt)
    detected_langs = detect_langs(txt)  # Отримуємо список мов із впевненістюw
    return lang_code, detected_langs

# Функція для отримання назви мови за її кодом
def CodeLang(lang):
    language = pycountry.languages.get(alpha_2=lang)
    return language.name if language else "Unknown"

# Функція для перекладу тексту
def translate_text(text, dest_language='de'):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

# Основна частина
if __name__ == "__main__":
    text = "Доброго дня. Як справи?"  # Приклад введеного тексту

    # Визначаємо код мови та впевненість за текстом
    lang_code, detected_langs = LangDetect(text)
    
    # Отримуємо назву мови за її кодом
    detected_lang = CodeLang(lang_code)
    
    # Виводимо результат визначення мови з впевненістю
    print(f"Detected(lang={lang_code}, confidence={detected_langs[0].prob})")
    
    # Переклад тексту 
    translated_text = translate_text(text, dest_language='de')
    print(f"Перекладений текст: {translated_text}")
    
    # Отримуємо назву мови перекладу 
    translated_lang = CodeLang('de')
    print(f"Назва мови перекладу: {translated_lang}")

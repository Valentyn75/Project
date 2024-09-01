from googletrans import Translator, LANGUAGES

def TransLate(text: str, src: str, dest: str) -> str:
    """Функція повертає текст перекладений на задану мову, або повідомлення про помилку.
    
    text – текст, який необхідно перекласти;
    src – назва або код мови заданого тексту, відповідно до стандарту ISO-639, 
          або значення ‘auto’;
    dest – назва або код мови на яку необхідно перевести заданий текст, 
           відповідно до стандарту ISO-639
    """
    try:
        translator = Translator()
        translated = translator.translate(text, src=src, dest=dest)
        return translated.text
    except Exception as e:
        return f"Помилка при перекладі: {e}"

def LangDetect(text: str, set: str) -> str:
    """Функція визначає мову та коефіцієнт довіри для заданого тексту, 
    або повертає повідомлення про помилку.
    
    text – текст для якого потрібно визначити мову та коефіцієнт довіри;
    set = “lang” – функція повертає тільки мову тексту
    set = “confidence” – функція повертає тільки коефіцієнт довіри
    set = “all” (по замовченню) – функція повертає мову і коефіцієнт довіри
    """
    try:
        translator = Translator()
        detected = translator.detect(text)
        lang = detected.lang
        confidence = detected.confidence  # Google Translator не надає точного коефіцієнта довіри, це умовне значення
        if set == 'lang':
            return lang
        elif set == 'confidence':
            return str(confidence)
        else:  # 'all' за замовчуванням
            return f"{lang}, Confidence: {confidence}"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

def CodeLang(lang: str) -> str:
    """Функція повертає код мови (відповідно до таблиці), якщо в параметрі lang міститься назва
    мови, або повертає назву мови, якщо в параметрі lang міститься її код,
    або повідомлення про помилку
    
    lang – назва або код мови
    """
    try:
        lang_dict = LANGUAGES
        if lang in lang_dict.values():
            return [k for k, v in lang_dict.items() if v == lang][0]
        elif lang in lang_dict:
            return lang_dict[lang]
        else:
            return "Невідомий код або назва мови"
    except Exception as e:
        return f"Помилка при обробці мови: {e}"

def LanguageList(out: str, text: str) -> str:
    """Виводить в файл або на екран таблицю всіх мов, що підтримуються, та їх кодів,
    а також текст, перекладений на цю мову. Повертає ‘Ok’, якщо всі операції виконані,
    або повідомлення про помилку.
    
    out = “screen” (по замовченню) – вивести таблицю на екран
    out = “file” – вивести таблицю в файл. (Тип файлу на розсуд студента)
    text – текст, який необхідно перекласти. Якщо параметр відсутній, то відповідна колонка
    в таблиці також повинна бути відсутня.
    """
    try:
        lines = ["N\tLanguage\tISO-639 code\tText"]
        lines.append("-" * 50)

        for i, (code, name) in enumerate(LANGUAGES.items(), 1):
            translated_text = Translator().translate(text, src='auto', dest=code).text if text else ""
            lines.append(f"{i}\t{name}\t{code}\t{translated_text}")

        table = "\n".join(lines)

        if out == 'file':
            with open('languages_list.txt', 'w', encoding='utf-8') as file:
                file.write(table)
            return "Ok"
        else:
            print(table)
            return "Ok"
    except Exception as e:
        return f"Помилка при виведенні таблиці: {e}"

if __name__ == "__main__":
    # Демонстрація роботи функцій
    print(TransLate("Hello, world!", "en", "es"))
    print(LangDetect("Hello, world!", "all"))
    print(CodeLang("Spanish"))
    print(LanguageList("screen", "Good morning"))

import string

def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().strip()
            # Розбиття тексту на речення
            sentences = text.split('.')
            first_sentence = sentences[0].strip() + '.' if sentences else ''
            print("First sentence:", first_sentence)
            return text
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def split_and_sort_words(text):
    # Видалення пунктуації
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).split()
    
    # Розділення на українські та англійські слова
    ukrainian_words = []
    english_words = []
    
    for word in words:
        # Перевірка чи слово українське або англійське
        if all('а' <= char.lower() <= 'я' or char.lower() == 'є' or char.lower() == 'і' or char.lower() == 'ї' or char.lower() == 'ґ' for char in word):
            ukrainian_words.append(word.lower())
        elif all('a' <= char.lower() <= 'z' for char in word):
            english_words.append(word.lower())
    
    # Сортування слів
    ukrainian_words.sort()
    english_words.sort()
    
    return ukrainian_words, english_words

def count_words(ukrainian_words, english_words):
    total_words = len(ukrainian_words) + len(english_words)
    print(f"Number of words: {total_words}")
    return total_words

# Головна функція
def main():
    file_path = './lab5/text.txt'  # Назва файлу
    text = read_first_sentence(file_path)
    
    if text:
        ukrainian_words, english_words = split_and_sort_words(text)
        
        # Виведення слів в алфавітному порядку
        if ukrainian_words:
            print("Ukrainian words in alphabetical order:", ', '.join(ukrainian_words))
        if english_words:
            print("English words in alphabetical order:", ', '.join(english_words))
        
        # Підрахунок кількості слів
        count_words(ukrainian_words, english_words)

if __name__ == '__main__':
    main()

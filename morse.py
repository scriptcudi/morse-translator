MORSE_RUS = {         # Словарь с кириллицы на морзе
    'А': '.-',
    'Б': '-...',
    'В': '.--',
    'Г': '--.',
    'Д': '-..',
    'Е': '.',
    'Ж': '...-',
    'З': '--..',
    'И': '..',
    'Й': '.---',
    'К': '-.-',
    'Л': '.-..',
    'М': '--',
    'Н': '-.',
    'О': '---',
    'П': '.--.',
    'Р': '.-.',
    'С': '...',
    'Т': '-',
    'У': '..-',
    'Ф': '..-.',
    'Х': '....',
    'Ц': '-.-.',
    'Ч': '---.',
    'Ш': '----',
    'Щ': '--.-',
    'Ъ': '--.--',
    'Ы': '-.--',
    'Ь': '-..-',
    'Э': '..-..',
    'Ю': '..--',
    'Я': '.-.-',
}

MORSE_REVERSE = {v: k for k, v in MORSE_RUS.items()}


def to_morse(text):
    text = text.upper().replace('Ё', 'Е')
    result = []
    for letter in text:
        if letter in MORSE_RUS:
            result.append(MORSE_RUS[letter])
        elif letter == ' ':
            result.append('/')
        else:
            result.append('?')
    return ' '.join(result)


def from_morse(morse_code):
    words = morse_code.split('/')          
    decoded_words = []
    for word in words:
        codes = word.strip().split()
        letters = []
        for c in codes:
            if c in MORSE_REVERSE:
                letters.append(MORSE_REVERSE[c])
            else:
                letters.append('?')        
        decoded_words.append(''.join(letters))
    return ' '.join(decoded_words)         


while True:
    print("1. Русский → Морзе")
    print("2. Морзе → Русский")
    print("3. Выход")
    choice = input("Выбор: ")

    if choice == '1':
        text = input("Текст: ")
        print(to_morse(text))
    elif choice == '2':
        code = input("Код: ")
        print(from_morse(code))         
    elif choice == '3':
        break
    else:
        print("Неверный выбор.")

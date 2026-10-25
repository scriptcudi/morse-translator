import tkinter as tk
from tkinter import ttk, messagebox

MORSE_RUS = {
    'А': '.-',  'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..',
    'Е': '.',   'Ж': '...-', 'З': '--..', 'И': '..',  'Й': '.---',
    'К': '-.-', 'Л': '.-..', 'М': '--',   'Н': '-.',  'О': '---',
    'П': '.--.', 'Р': '.-.', 'С': '...',  'Т': '-',   'У': '..-',
    'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----',
    'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..',
    'Ю': '..--', 'Я': '.-.-',
}
MORSE_REVERSE = {v: k for k, v in MORSE_RUS.items()}


def to_morse(text):
    text = ' '.join(text.upper().replace('Ё', 'Е').split())
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
        letters = [MORSE_REVERSE.get(c, '?') for c in codes]
        decoded_words.append(''.join(letters))
    return ' '.join(decoded_words)


def on_encode():
    src = input_text.get('1.0', 'end').strip()
    if not src:
        messagebox.showwarning('Пусто', 'Введите текст для кодирования.')
        return
    output_text.delete('1.0', 'end')
    output_text.insert('1.0', to_morse(src))


def on_decode():
    src = input_text.get('1.0', 'end').strip()
    if not src:
        messagebox.showwarning('Пусто', 'Введите код Морзе для декодирования.')
        return
    output_text.delete('1.0', 'end')
    output_text.insert('1.0', from_morse(src))


def on_clear():
    input_text.delete('1.0', 'end')
    output_text.delete('1.0', 'end')


root = tk.Tk()
root.title('Азбука Морзе')
root.geometry('680x420')
root.minsize(560, 360)

top = ttk.Frame(root, padding=8)
top.pack(fill='x')
ttk.Button(top, text='Русский → Морзе', command=on_encode).pack(side='left', padx=4)
ttk.Button(top, text='Морзе → Русский', command=on_decode).pack(side='left', padx=4)
ttk.Button(top, text='Очистить',        command=on_clear).pack(side='right', padx=4)

ttk.Label(root, text='Ввод:', padding=(8, 0)).pack(anchor='w')
input_text = tk.Text(root, height=7, wrap='word', font=('Consolas', 12))
input_text.pack(fill='both', expand=True, padx=8)

ttk.Label(root, text='Результат:', padding=(8, 6)).pack(anchor='w')
output_text = tk.Text(root, height=7, wrap='word', font=('Consolas', 12))
output_text.pack(fill='both', expand=True, padx=8, pady=(0, 8))

root.mainloop()
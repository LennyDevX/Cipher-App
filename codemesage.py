import os
import random
import tkinter as tk
from tkinter import messagebox, filedialog

def decode(message_file):
    """
    Decodifica un mensaje a partir de un archivo.

    El archivo debe contener líneas con el formato "número palabra".
    Las palabras se ordenan según los números y se unen para formar el mensaje decodificado.

    Args:
        message_file (str): La ruta al archivo que contiene el mensaje codificado.

    Returns:
        str: El mensaje decodificado.

    Raises:
        Exception: Si el archivo no existe.
    """
    if not os.path.exists(message_file):
        raise Exception(f"El archivo {message_file} no existe.")

    with open(message_file, 'r') as file:
        lines = file.readlines()

    words = {}
    for line in lines:
        parts = line.strip().split(' ')
        if len(parts) != 2:
            continue
        
        number, word = parts
        if not number.isdigit():
            continue
        
        words[int(number)] = word

    message = ' '.join(words[i] for i in sorted(words.keys()))
    return message

def encode(message):
    """
    Codifica un mensaje.

    El mensaje se divide en palabras, y cada palabra se asocia con un número.
    Las palabras se desordenan y se unen para formar el mensaje codificado.

    Args:
        message (str): El mensaje a codificar.

    Returns:
        str: El mensaje codificado.
    """
    words = message.split(' ')
    encoded_words = [f"{i+1} {word}" for i, word in enumerate(words) if word.strip()]
    random.shuffle(encoded_words)
    encoded_message = '\n'.join(encoded_words)
    return encoded_message

def decode_file():
    """
    Decodifica un mensaje a partir de un archivo seleccionado por el usuario.

    Muestra el mensaje decodificado en la interfaz de usuario.
    """
    message_file = file_entry.get()
    try:
        decoded_message = decode(message_file)
        message_text.delete(1.0, tk.END)
        message_text.insert(tk.END, decoded_message)
        messagebox.showinfo("Éxito", "El mensaje se descodificó con éxito.")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al descodificar el mensaje: {e}")

def encode_file():
    """
    Codifica un mensaje a partir de un archivo seleccionado por el usuario.

    Muestra una vista previa del mensaje codificado en la interfaz de usuario antes de guardarlo.
    """
    message_file = file_entry.get()
    if not os.path.exists(message_file):
        messagebox.showerror("Error", f"El archivo {message_file} no existe.")
        return

    with open(message_file, 'r') as file:
        message = file.read().strip()

    encoded_message = encode(message)
    message_text.delete(1.0, tk.END)
    message_text.insert(tk.END, encoded_message)

def save_file():
    """
    Guarda el mensaje codificado en un archivo seleccionado por el usuario.
    """
    encoded_message = message_text.get(1.0, tk.END).strip()
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if filename:
        with open(filename, 'w') as file:
            file.write(encoded_message)
        messagebox.showinfo("Éxito", "El mensaje se guardó con éxito.")

def browse_file():
    """
    Permite al usuario seleccionar un archivo.

    Actualiza la entrada de archivo en la interfaz de usuario con la ruta del archivo seleccionado.
    """
    filename = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)

root = tk.Tk()

message_text = tk.Text(root, height=10, width=50)
message_text.pack()

file_entry = tk.Entry(root, width=50)
file_entry.pack()

button_frame = tk.Frame(root)
button_frame.pack()

browse_button = tk.Button(button_frame, text="Buscar", command=browse_file)
browse_button.pack(side=tk.LEFT)

decode_button = tk.Button(button_frame, text="Decodificar", command=decode_file)
decode_button.pack(side=tk.LEFT)

encode_button = tk.Button(button_frame, text="Codificar", command=encode_file)
encode_button.pack(side=tk.LEFT)

save_button = tk.Button(button_frame, text="Guardar", command=save_file)
save_button.pack(side=tk.LEFT)

root.mainloop()
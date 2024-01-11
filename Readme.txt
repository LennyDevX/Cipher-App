Codificador y Descodificador de Texto en Python
Este proyecto es una aplicación de codificación y decodificación de texto escrita en Python. La aplicación permite a los usuarios codificar mensajes de texto en números y luego decodificar los números de vuelta a texto.

Descripción
La aplicación consta de dos partes principales: la codificación y la decodificación.

Codificación
La codificación se realiza en la función encode. Esta función toma un mensaje de texto como entrada, divide el mensaje en palabras y asocia cada palabra con un número. Luego, desordena las palabras y las une para formar el mensaje codificado. El mensaje codificado consiste en números separados por saltos de línea.

Decodificación
La decodificación se realiza en la función decode. Esta función toma un archivo que contiene un mensaje codificado como entrada. El archivo debe contener líneas con el formato "número". Los números se traducen a palabras según el diccionario number_to_word y se unen para formar el mensaje decodificado.

Cómo funciona el código
El código utiliza la biblioteca tkinter de Python para proporcionar una interfaz de usuario gráfica. Los usuarios pueden seleccionar un archivo para codificar o decodificar, y el mensaje codificado o decodificado se muestra en la interfaz de usuario.

El código también utiliza los diccionarios word_to_number y number_to_word para mapear palabras a números y viceversa. Estos diccionarios deben ser llenados con las palabras y números correspondientes antes de que puedas codificar o decodificar mensajes.

Uso
Para usar la aplicación, simplemente ejecuta el script de Python en tu terminal. Se abrirá una ventana de la interfaz de usuario. Puedes seleccionar un archivo para codificar o decodificar utilizando el botón "Buscar". Luego, puedes codificar el archivo utilizando el botón "Codificar" o decodificar el archivo utilizando el botón "Decodificar". El mensaje codificado o decodificado se mostrará en la interfaz de usuario. También puedes guardar el mensaje codificado en un archivo utilizando el botón "Guardar".

Conclusión
Esta aplicación es una herramienta útil para codificar y decodificar mensajes de texto. Es fácil de usar y proporciona una forma rápida y eficiente de codificar y decodificar mensajes.
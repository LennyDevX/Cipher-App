#Cipher App - the easy way to decrypt and encrypt messages

Text Encoder and Decoder in Python
This project is a text encoding and decoding application written in Python. The application allows users to encode text messages into numbers and then decode the numbers back into text.

Description
The application consists of two main parts: encoding and decoding.

Encoding
The encoding is done in the encode function. This function takes a text message as input, splits the message into words, and associates each word with a number. Then, it shuffles the words and joins them to form the encoded message. The encoded message consists of numbers separated by line breaks.

Decoding
The decoding is done in the decode function. This function takes a file that contains an encoded message as input. The file should contain lines in the format "number". The numbers are translated into words according to the number_to_word dictionary and joined to form the decoded message.

How the Code Works
The code uses the Python tkinter library to provide a graphical user interface. Users can select a file to encode or decode, and the encoded or decoded message is displayed in the user interface.

The code also uses the word_to_number and number_to_word dictionaries to map words to numbers and vice versa. These dictionaries must be filled with the corresponding words and numbers before you can encode or decode messages.

Usage
To use the application, simply run the Python script in your terminal. A user interface window will open. You can select a file to encode or decode using the "Browse" button. Then, you can encode the file using the "Encode" button or decode the file using the "Decode" button. The encoded or decoded message will be displayed in the user interface. You can also save the encoded message to a file using the "Save" button.

Conclusion
This application is a useful tool for encoding and decoding text messages. It is easy to use and provides a quick and efficient way to encode and decode messages.
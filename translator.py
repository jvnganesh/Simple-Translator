#i have made a google translaator
import tkinter as tk
from googletrans import Translator

def translate_text():
    # Get the input text from the user
    input_text = input_entry.get()
    # Detect the source language (optional)
    src_lang = translator.detect(input_text).lang
    # Get the selected target language from the dropdown menu
    target_lang = target_language.get()
    # Translate the input text
    translated_text = translator.translate(input_text, src=src_lang, dest=target_lang).text
    # Update the output label with the translated text
    output_label.config(text=translated_text)
# Create a translator object
translator = Translator()
# Create the main application window
app = tk.Tk()
app.title("Language Translator")
# Create and pack a label for instructions
instructions_label = tk.Label(app, text="Enter text to translate:")
instructions_label.pack()
# Create and pack an entry widget for input text
input_entry = tk.Entry(app, width=100)
input_entry.pack()
# Create a dropdown menu for selecting the target language
target_language = tk.StringVar()
target_language.set("en")  # Set English as the default target language
target_language_menu = tk.OptionMenu(app, target_language, "en", "es", "fr", "de", "ja", "ko", "zh","gu","ar","hi")
target_language_menu.pack()
# Create and pack a button to trigger translation
translate_button = tk.Button(app, text="Translate", command=translate_text)
translate_button.pack()
# Create and pack a label for displaying the translated text
output_label = tk.Label(app, text="", wraplength=400, justify="left")
output_label.pack()
# Start the Tkinter main loop
app.mainloop()

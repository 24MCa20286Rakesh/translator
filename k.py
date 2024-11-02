from googletrans import Translator, LANGUAGES
import tkinter as tk
from tkinter import messagebox, ttk

def translate_text(text, dest_language):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

def translate():
    text = input_text.get("1.0", tk.END).strip()
    dest_language = lang_combobox.get()  # Get the selected language code

    if text and dest_language:
        try:
            translated_text = translate_text(text, dest_language)
            output_text.delete("1.0", tk.END)  # Clear previous output
            output_text.insert(tk.END, translated_text)  # Insert translated text
        except Exception as e:
            messagebox.showerror("Error", f"Translation failed: {str(e)}")
    else:
        messagebox.showwarning("Input Error", "Please provide both text and select a language.")

# Create the main Tkinter window
app = tk.Tk()
app.title("Simple Google Translate App")
app.geometry("500x400")  # Set window size

# Create and place the input text area
tk.Label(app, text="Enter text to translate:").pack(pady=10)
input_text = tk.Text(app, height=5, width=50)
input_text.pack(pady=5)

# Create and place the language selection
tk.Label(app, text="Select language to translate to:").pack(pady=10)
lang_combobox = ttk.Combobox(app, values=list(LANGUAGES.values()))
lang_combobox.pack(pady=5)
lang_combobox.set("Select a language")  # Default value

# Create and place the translate button
translate_button = tk.Button(app, text="Translate", command=translate)
translate_button.pack(pady=20)

# Create and place the output text area
tk.Label(app, text="Translated text:").pack(pady=10)
output_text = tk.Text(app, height=5, width=50)
output_text.pack(pady=5)

# Start the Tkinter event loop
app.mainloop()

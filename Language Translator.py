import tkinter as tk
from googletrans import Translator, LANGUAGES

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.root.configure(bg="#2C3E50")  # Set background color

        self.translator = Translator()

        self.label = tk.Label(root, text="Enter the text to translate:", font=("Arial", 14), bg="#2C3E50", fg="#ECF0F1")
        self.label.pack(pady=(20, 5))

        self.text_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.text_entry.pack()

        self.language_label = tk.Label(root, text="Select the target language:", font=("Arial", 14), bg="#2C3E50", fg="#ECF0F1")
        self.language_label.pack(pady=5)

        self.languages = list(LANGUAGES.values())
        self.selected_language = tk.StringVar(root)
        self.language_menu = tk.OptionMenu(root, self.selected_language, *self.languages)
        self.language_menu.config(font=("Arial", 12))
        self.language_menu.pack()

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text, font=("Arial", 14))
        self.translate_button.pack(pady=(10, 20))

        self.translated_text = tk.Label(root, text="", wraplength=300, font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1")
        self.translated_text.pack()

    def translate_text(self):
        text = self.text_entry.get()
        target_language = self.selected_language.get()

        if text and target_language:
            target_language_code = [code for code, lang in LANGUAGES.items() if lang == target_language][0]
            translated = self.translator.translate(text, dest=target_language_code)
            self.translated_text.config(text=translated.text)
        else:
            self.translated_text.config(text="Please enter text and select a target language.")

def main():
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

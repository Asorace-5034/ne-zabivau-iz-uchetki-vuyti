import sys
import tkinter as tk
import threading
import time
import string

class ConsoleWindow:
    def __init__(self, root):
        self.font_size = 14
        self.font_family = "Consolas"

        self.text = tk.Text(
            root,
            wrap="word",
            state="disabled",
            bg="black",
            fg="lime",
            font=(self.font_family, self.font_size)
        )
        self.text.pack(expand=True, fill="both")

        # биндим горячие клавиши
        root.bind("<Control-plus>", self.increase_font)
        root.bind("<Control-minus>", self.decrease_font)
        root.bind("<Control-0>", self.reset_font)

    def set_font(self):
        self.text.configure(font=(self.font_family, self.font_size))

    def increase_font(self, event=None):
        self.font_size += 2
        self.set_font()

    def decrease_font(self, event=None):
        if self.font_size > 6:
            self.font_size -= 2
            self.set_font()

    def reset_font(self, event=None):
        self.font_size = 14
        self.set_font()

    def write(self, message):
        self.text.configure(state="normal")
        self.text.insert("end", message)
        self.text.see("end")
        self.text.configure(state="disabled")

    def flush(self):
        pass

def run_tk():
    root = tk.Tk()
    root.title("Окно вывода")
    console = ConsoleWindow(root)
    sys.stdout = console
    root.mainloop()

# Запускаем окно в отдельном потоке
threading.Thread(target=run_tk, daemon=True).start()



text = 'I love this Academy'
temp = ''

def func():
    global text
    global temp
    for ch in text:
        for i in string.printable:
            if i == ch or ch == i:
                time.sleep(0.02)
                print(temp + i)
                temp += ch
                break
            else: 
                time.sleep(0.02)
                print(temp + i)

func()

import sys
import tkinter as tk
import threading
import time
import string

class ConsoleWindow:
    def __init__(self, root):
        self.text = tk.Text(root, wrap="word", state="disabled", bg="black", fg="lime")
        self.text.pack(expand=True, fill="both")

    def write(self, message):
        self.text.configure(state="normal")
        self.text.insert("end", message)
        self.text.see("end")  # автопрокрутка
        self.text.configure(state="disabled")

    def flush(self):
        pass  # нужен для совместимости с sys.stdout

def run_tk():
    root = tk.Tk()
    root.title("Окно вывода")
    console = ConsoleWindow(root)

    # перенаправляем stdout
    sys.stdout = console

    root.mainloop()

# Запускаем tkinter в отдельном потоке
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
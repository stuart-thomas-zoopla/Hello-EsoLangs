from tkinter import Tk, filedialog as fd
from time import sleep
from random import randint

tk = Tk()
tk.withdraw()

filetypes = [("Frog Scripts", "*.frgp"), ("All files", "*.*")]
code = fd.askopenfilename(title="Select a Script", filetypes=filetypes)
code = open(code, mode="r")
code = code.read()
code = code.split("\n")

answer = ""
answer_shouldBe = ""

def bug():
    print("ERROR")
    sleep(1)
    quit()

for i in code:
    try:
        if i.startswith("croak "): print(i[6:])
        elif i.startswith("quack "): answer = input(i[6:])
        elif i.startswith("ribbit "): answer_shouldBe = i[7:]
        elif i == "bark": print(answer == answer_shouldBe)
        elif i.startswith("beep "): print(randint(1, int(i[5:])))
        elif i.startswith("cluck "): sleep(int(i[6:]))
        elif i == "" or i.startswith("*"): pass
        else: bug()
    except: bug()

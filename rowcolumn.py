import tkinter as tk
from tkinter import messagebox

def ispermutationzad(keylistzad):
    n = len(keylistzad)
    return sorted(keylistzad) == list(range(1, n+1))

def encryptzad(textzad, keylistzad):
    textzad = textzad.replace(" ", "").upper()
    if not ispermutationzad(keylistzad):
        raise ValueError("key is not a valid permutation")

    n = len(keylistzad)
    rows = (len(textzad) + n - 1) // n

 
    matrixzad = [[''] * n for _ in range(rows)]
    idx = 0
    for r in range(rows):
        for c in range(n):
            if idx < len(textzad):
                matrixzad[r][c] = textzad[idx]
                idx += 1

  
    reading_order = sorted(range(n), key=lambda c: keylistzad[c])

   
    ciphertextzad = ""
    for c in reading_order:
        for r in range(rows):
            if matrixzad[r][c]:
                ciphertextzad += matrixzad[r][c]
    return ciphertextzad

def decryptzad(cipherzad, keylistzad):
    cipherzad = cipherzad.replace(" ", "").upper()
    if not ispermutationzad(keylistzad):
        raise ValueError("key is not a valid permutation")

    n = len(keylistzad)
    L = len(cipherzad)
    rows = (L + n - 1) // n

  
    col_lengths = [0] * n
    full_cols = L % n
    if full_cols == 0:
        full_cols = n
    for i in range(n):
        col_lengths[i] = rows if i < full_cols else rows - 1

   
    filling_order = sorted(range(n), key=lambda c: keylistzad[c])

    
    matrixzad = [[''] * n for _ in range(rows)]

 
    idx = 0
    for c in filling_order:
        length = col_lengths[c]
        for r in range(length):
            matrixzad[r][c] = cipherzad[idx]
            idx += 1

   
    plaintextzad = ""
    for r in range(rows):
        for c in range(n):
            if matrixzad[r][c]:
                plaintextzad += matrixzad[r][c]
    return plaintextzad.lower()  
def doencryptzad():
    textzad = entrytextzad.get("1.0", tk.END).strip()
    keystr = entrykeyzad.get().strip()
    try:
        keyzad = list(map(int, keystr.split()))
        result = encryptzad(textzad, keyzad)
        outputzad.delete("1.0", tk.END)
        outputzad.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def dodecryptzad():
    cipherzad = entrytextzad.get("1.0", tk.END).strip()
    keystr = entrykeyzad.get().strip()
    try:
        keyzad = list(map(int, keystr.split()))
        result = decryptzad(cipherzad, keyzad)
        outputzad.delete("1.0", tk.END)
        outputzad.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("row column transposition cipher - lock down crew")
root.geometry("600x550")
root.resizable(False, False)

primary = "#0d2471"
bg = "#e8ecf8"
root.config(bg=bg)

header = tk.Label(root, text="lock down crew",
                  font=("poppins", 20, "bold"),
                  bg=primary, fg="white", pady=10)
header.pack(fill="x")

cardzad = tk.Frame(root, bg="white", bd=2, relief="ridge")
cardzad.place(relx=0.5, rely=0.55, anchor="center", width=520, height=430)

titlezad = tk.Label(cardzad, text="row column transposition cipher",
                    font=("poppins", 16, "bold"), bg="white", fg=primary)
titlezad.pack(pady=10)

tk.Label(cardzad, text="enter text:", bg="white", fg="black",
         font=("poppins", 12)).pack()

entrytextzad = tk.Text(cardzad, height=4, width=50, font=("arial", 12))
entrytextzad.pack(pady=5)

tk.Label(cardzad, text="permutation key (e.g. 3 1 4 2):",
         bg="white", fg="black", font=("poppins", 12)).pack()

entrykeyzad = tk.Entry(cardzad, width=40, font=("arial", 12))
entrykeyzad.pack(pady=5)

btnframezad = tk.Frame(cardzad, bg="white")
btnframezad.pack(pady=10)

btnencryptzad = tk.Button(btnframezad, text="encrypt", command=doencryptzad,
                          bg=primary, fg="white", font=("poppins", 12), width=12)
btnencryptzad.grid(row=0, column=0, padx=10)

btndecryptzad = tk.Button(btnframezad, text="decrypt", command=dodecryptzad,
                          bg="#1e3899", fg="white", font=("poppins", 12), width=12)
btndecryptzad.grid(row=0, column=1, padx=10)

tk.Label(cardzad, text="output:", bg="white", fg="black",
         font=("poppins", 12)).pack()

outputzad = tk.Text(cardzad, height=4, width=50, font=("arial", 12))
outputzad.pack()

root.mainloop()
import tkinter as tk
import csv

FILE_NAME = "studenti.csv"



def add_student():
    ime = entry_ime.get()
    prezime = entry_prezime.get()
    indeks = entry_indeks.get()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ime, prezime, indeks])

    clear_entries()

def show_students():
    listbox.delete(0, tk.END)

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            listbox.insert(tk.END, row)

def delete_student():
    selected = listbox.curselection()
    if not selected:
        return

    index = selected[0]

    with open(FILE_NAME, "r") as file:
        rows = list(csv.reader(file))

    header = rows[0]
    data = rows[1:]

    del data[index]

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

    show_students()

def update_student():
    selected = listbox.curselection()
    if not selected:
        return

    index = selected[0]

    ime = entry_ime.get()
    prezime = entry_prezime.get()
    indeks = entry_indeks.get()

    with open(FILE_NAME, "r") as file:
        rows = list(csv.reader(file))

    header = rows[0]
    data = rows[1:]

    data[index] = [ime, prezime, indeks]

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

    show_students()
    clear_entries()

def clear_entries():
    entry_ime.delete(0, tk.END)
    entry_prezime.delete(0, tk.END)
    entry_indeks.delete(0, tk.END)



root = tk.Tk()
root.title("Evidencija studenata")


tk.Label(root, text="Ime").grid(row=0, column=0)
tk.Label(root, text="Prezime").grid(row=1, column=0)
tk.Label(root, text="Indeks").grid(row=2, column=0)


entry_ime = tk.Entry(root)
entry_prezime = tk.Entry(root)
entry_indeks = tk.Entry(root)

entry_ime.grid(row=0, column=1)
entry_prezime.grid(row=1, column=1)
entry_indeks.grid(row=2, column=1)


tk.Button(root, text="Dodaj", command=add_student).grid(row=3, column=0)
tk.Button(root, text="Prikazi", command=show_students).grid(row=3, column=1)
tk.Button(root, text="Obrisi", command=delete_student).grid(row=4, column=0)
tk.Button(root, text="Azuriraj", command=update_student).grid(row=4, column=1)


listbox = tk.Listbox(root, width=50)
listbox.grid(row=5, column=0, columnspan=2)

root.mainloop()
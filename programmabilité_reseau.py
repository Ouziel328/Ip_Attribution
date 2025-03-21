import tkinter as tk
from tkinter import messagebox

class AdresseIPApp:
    def __init__(self, master, height, width):
        self.master = master
        self.master.title('Adressage IP')
        self.ip_reserve = [i for i in range(224, 256)] + [0, 127]
        self.address_fin = []
        self.entries = []
        self.height = height
        self.width = width
        self.create_widgets()
        

    def create_widgets(self):
        self.master.geometry(f"{300}x{100}+{self.width // 2 - 300 // 2}+{self.height // 2 - 150 // 2}")
        label = tk.Label(self.master, text="Entrez les nombres entiers de votre adresse IP :")
        label.grid(row=0, column=0, columnspan=4, sticky='nsew', pady=(5, 5))

        for i in range(4):
            entry = tk.Entry(self.master, width=5, justify='center')
            entry.grid(row=1, column=i, sticky='nsew', pady=(0, 5), padx=5)
            entry.bind("<FocusOut>", lambda e, p=i: self.validate_entry(e.widget, p))
            entry.bind("<Return>", lambda e, p=i: self.validate_entry(e.widget, p))
            self.entries.append(entry)

        # Configuration de la grille pour une mise en page réactive
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)

    def validate_entry(self, entry, position):
        entree_ip = entry.get().strip()
        if entree_ip:
            try:
                entree_ip_int = int(entree_ip)
            except ValueError:
                self.raise_message("Erreur", f"'{entree_ip}' n'est pas un entier valide.")
                entry.delete(0, tk.END)
                entry.focus_set()
                return

            if not 0 <= entree_ip_int <= 255:
                self.raise_message("Erreur", "Le nombre doit être compris entre 0 et 255.")
                entry.delete(0, tk.END)
                entry.focus_set()
                return

            if position == 0 and entree_ip_int in self.ip_reserve:
                self.raise_message("Erreur", f"Le premier octet '{entree_ip_int}' est réservé.")
                entry.delete(0, tk.END)
                entry.focus_set()
                return

            if len(self.address_fin) > position:
                self.address_fin[position] = entree_ip_int
            else:
                self.address_fin.append(entree_ip_int)

            if len(self.address_fin) == 4:
                adresse_ip_str = ".".join(map(str, self.address_fin))
                classe_ip = self.atrib_class(self.address_fin[0])
                self.raise_message("Succès", f"Adresse IP attribuée avec succès : {adresse_ip_str}\nClasse de l'adresse : {classe_ip}")
                self.master.quit()  # Ferme la fenêtre après la validation complète

    def raise_message(self, title, message):
        messagebox.showinfo(title, message)

    def atrib_class(self, premier_octet):
        if 0 <= premier_octet <= 127:
            return "A"
        elif 128 <= premier_octet <= 191:
            return "B"
        elif 192 <= premier_octet <= 223:
            return "C"
        elif 224 <= premier_octet <= 239:
            return "D"
        elif 240 <= premier_octet <= 255:
            return "E"
        else:
            return "Inconnue"

if __name__ == "__main__":
    root = tk.Tk()
    h = root.winfo_screenheight()
    w = root.winfo_screenwidth()
    app = AdresseIPApp(root, h, w)
    root.mainloop()

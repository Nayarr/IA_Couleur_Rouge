import tkinter as tk
from tkinter import messagebox
import random
import IA

class NeuroneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Détecteur de couleur rouge")
        self.neurone = [1.0, 1.0, 1.0]
        self.epsilon = 0.2
        self.historique = []

        # Interface
        self.color_display = tk.Label(root, text="Aucune couleur choisie", width=60, height=10, bg="white")
        self.color_display.pack(pady=10)

        self.choose_button = tk.Button(root, text="Générer une couleur aléatoire", command=self.generer_couleur)
        self.choose_button.pack(pady=5)

        self.boutons_frame = tk.Frame(root)
        self.boutons_frame.pack(pady=5)

        self.rouge_button = tk.Button(self.boutons_frame, text="C'est rouge", bg="red", fg="white", command=lambda: self.apprentissage(1))
        self.rouge_button.grid(row=0, column=0, padx=5)

        self.pas_rouge_button = tk.Button(self.boutons_frame, text="Pas rouge", command=lambda: self.apprentissage(0))
        self.pas_rouge_button.grid(row=0, column=1, padx=5)

        self.test_button = tk.Button(root, text="Tester le neurone", command=self.tester_jeu_test)
        self.test_button.pack(pady=10)

        self.etat_label = tk.Label(root, text=f"État du neurone : {self.neurone}")
        self.etat_label.pack(pady=5)

        self.couleur_actuelle = (1, 1, 1)  # RGB par défaut

    def generer_couleur(self):
        r, g, b = [random.random() for _ in range(3)]
        self.couleur_actuelle = [r, g, b]
        hex_color = '#%02x%02x%02x' % tuple(int(x*255) for x in self.couleur_actuelle)
        self.color_display.config(bg=hex_color, text=str(self.couleur_actuelle))

    def apprentissage(self, objectif):
        self.neurone = IA.apprentissage(self.neurone.copy(), self.couleur_actuelle, objectif)
        self.etat_label.config(text=f"État du neurone : {[round(x, 2) for x in self.neurone]}")
        self.historique.append((self.couleur_actuelle, objectif))
        self.generer_couleur()  # Générer une nouvelle couleur après chaque apprentissage

    def tester_jeu_test(self):
        jeu_test = [ (0.9,0,0),(1,0.2,0.2),(0,0,1),(1,0,1),(1,0.5,0),(0.7,0.5,0.4) ]
        resultat = []
        for couleur in jeu_test:
            res = IA.activation(self.neurone, couleur)
            resultat.append((couleur, "rouge" if res else "pas rouge"))
        message = "\n".join([f"{c} => {r}" for c, r in resultat])
        messagebox.showinfo("Résultats du test", message)


if __name__ == '__main__':
    root = tk.Tk()
    app = NeuroneApp(root)
    app.generer_couleur()
    root.mainloop()
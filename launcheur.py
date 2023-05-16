import os
import tkinter as tk

# Créer un dictionnaire contenant les applications et leurs commandes d'exécution
applications = {
    "Chrome": "C:\Program Files\Google\Chrome\Application\chrome.exe",
    "Edge": "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "insta": "https://www.instagram.com/",
    "facebook": "https://www.facebook.com/",
    "gmail": "https://mail.google.com/mail/u/0/#inbox",
    "office": "https://www.office.com/?auth=1"
    }

# Créer une fenêtre
root = tk.Tk()
root.title("Launcher")

# Charger l'image de fond
background_image = tk.PhotoImage(file="Téléchargements\FD.jpg")

# Créer un canevas pour l'image de fond
canvas = tk.Canvas(root, width=background_image.width(), height=background_image.height())
canvas.pack()

# Placer l'image de fond sur le canevas
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Créer une étiquette
label = tk.Label(root, text="Applications disponibles :", bg="pink")
label.pack()

# Créer des boutons pour chaque application
for i, app_name in enumerate(applications.keys()):
    button = tk.Button(root, text=app_name, bg="pink", fg="blue", command=lambda app_path=applications[app_name]: os.startfile(app_path))
    button.pack()

# Créer une étiquette pour la demande de choix
label = tk.Label(root, text="Veuillez sélectionner une application :", bg="pink")
label.pack()

# Créer une entrée pour la sélection
entry = tk.Entry(root)
entry.pack()

# Fonction pour traiter la sélection
def select():
    # Récupérer le choix de l'utilisateur
    choice = int(entry.get())

    # Vérifier si la sélection est valide
    if choice < 1 or choice > len(applications):
        label.config(text="Sélection invalide. Veuillez choisir un nombre entre 1 et " + str(len(applications)), fg="red")
    else:
        # Récupérer le chemin d'accès de l'application sélectionnée
        app_path = list(applications.values())[choice-1]

        # Lancer l'application
        os.startfile(app_path)

# Créer un bouton pour valider la sélection
button = tk.Button(root, text="Valider", bg="navy blue", fg="white", command=select)
button.pack()

# Fonction pour quitter la fenêtre avec la touche Echap
def exit(event):
    if event.keysym == "Escape":
        root.destroy()

# Lier la touche Echap à la fonction de sortie
root.bind("<Key>", exit)

# Lancer la boucle principale
root.mainloop()

print("Au revoir !")

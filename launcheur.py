# git remote add origin https://github.com/faucheurlunair/launcheur
import os
import tkinter as tk

applications = {
    "Chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "Edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "insta": "https://www.instagram.com/",
    "facebook": "https://www.facebook.com/",
    "gmail": "https://mail.google.com/mail/u/0/#inbox",
    "office": "https://www.office.com/?auth=1"
}

root = tk.Tk()
root.title("lunary_launcheur")

label = tk.Label(root, text="Applications disponibles :", bg="pink")
label.pack()

for i, app_name in enumerate(applications.keys()):
    button = tk.Button(root, text=app_name, bg="pink", fg="blue", command=lambda app_path=applications[app_name]: os.startfile(app_path))
    button.pack()


label = tk.Label(root, text="Veuillez sélectionner une application :", bg="pink")
label.pack()

entry = tk.Entry(root)
entry.pack()

def select():
        choice = entry.get()

       if not choice.isdigit() or int(choice) < 1 or int(choice) > len(applications):
        label.config(text=f"Sélection invalide. Veuillez choisir un nombre entre 1 et {len(applications)}", fg="red")
    else:
                app_path = list(applications.values())[int(choice)-1]

            os.startfile(app_path)

button = tk.Button(root, text="Valider", bg="blue", fg="white", command=select)
button.pack()

def exit(event):
    if event.keysym == "Escape":
        root.destroy()

root.bind("<Key>", exit)

root.mainloop()

print("a bientot  !")

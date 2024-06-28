import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import threading
from diffusers import StableDiffusionPipeline

# Fonction pour générer l'image
def generate_image():
    prompt = entry_description.get()
    if not prompt:
        messagebox.showerror("Erreur", "Veuillez entrer une description.")
        return
    
    spinner.grid(row=1, column=2, padx=10, pady=10)  # Afficher le spinner
    spinner.start()  # Démarrer le spinner
    
    # Fonction de génération d'image en arrière-plan
    def generate():
        try:
            # Charger le modèle à partir du répertoire local
            model_path = "./tiny_stable_diffusion_local"
            pipe = StableDiffusionPipeline.from_pretrained(model_path)
            pipe.to("cpu")  # Utiliser le CPU pour la génération
            
            # Générer l'image
            image = pipe(prompt).images[0]
            
            # Afficher l'image générée dans la zone d'affichage
            img = ImageTk.PhotoImage(image.resize((400, 200)))
            canvas.create_image(0, 0, anchor='nw', image=img)
            canvas.image = img  # Sauvegarder une référence à l'image
            
            # Ajouter une légende sous l'image
            canvas.create_text(200, 180, text=prompt, fill="black")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
        finally:
            spinner.stop()  # Arrêter le spinner
            spinner.grid_remove()  # Cacher le spinner
    
    thread = threading.Thread(target=generate)
    thread.start()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Tkinter Application UI")
root.geometry("600x400")

# Création d'une étiquette et d'un champ de saisie pour la description
label_description = tk.Label(root, text="Description:")
label_description.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_description = tk.Entry(root, width=50)
entry_description.grid(row=0, column=1, padx=10, pady=10)

# Création du bouton pour générer l'image
button_generate = tk.Button(root, text="Generate Image", command=generate_image)
button_generate.grid(row=1, column=1, padx=10, pady=10)

# Création du spinner (utilisation de ttk.Progressbar)
spinner = ttk.Progressbar(root, mode='indeterminate')
spinner.grid(row=1, column=2, padx=10, pady=10)
spinner.grid_remove()  # Cacher le spinner initialement

# Création de la zone d'affichage de l'image
canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Lancement de la boucle principale
root.mainloop()

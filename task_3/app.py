import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk # type: ignore
from diffusers import StableDiffusionPipeline # type: ignore
import torch # type: ignore
import threading


# Fonction pour générer l'image
def generate_image():
    # Désactiver le bouton pendant la génération
    generate_button.config(state=tk.DISABLED)
    # Afficher le spinner
    spinner.start()
    
    # Récupérer le texte de description
    prompt = text_input.get("1.0", tk.END).strip()
    
    # Fonction pour exécuter la génération d'image dans un thread séparé
    def run_generation():
        try:
            # Générer l'image
            image = pipe(prompt).images[0]
            
            # Redimensionner l'image pour l'affichage
            image = image.resize((300, 300))
            
            # Convertir l'image PIL en PhotoImage pour Tkinter
            photo = ImageTk.PhotoImage(image)
            
            # Mettre à jour l'interface utilisateur dans le thread principal
            root.after(0, update_ui, photo, prompt)
        except Exception as e:
            print(f"Erreur lors de la génération de l'image : {e}")
            root.after(0, update_ui, None, prompt)

    # Lancer la génération dans un thread séparé
    threading.Thread(target=run_generation).start()

# Fonction pour mettre à jour l'interface utilisateur après la génération
def update_ui(photo, prompt):
    if photo:
        # Mettre à jour l'image et la légende
        image_label.config(image=photo)
        image_label.image = photo
        caption_label.config(text=prompt)
    else:
        caption_label.config(text="Erreur lors de la génération de l'image")
    
    # Arrêter le spinner et réactiver le bouton
    spinner.stop()
    generate_button.config(state=tk.NORMAL)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Générateur d'images")

# Créer et placer les widgets
text_input = tk.Text(root, height=3, width=40)
text_input.pack(pady=10)

generate_button = tk.Button(root, text="Générer l'image", command=generate_image)
generate_button.pack(pady=5)

spinner = ttk.Progressbar(root, mode='indeterminate', length=200)
spinner.pack(pady=5)

image_label = tk.Label(root)
image_label.pack(pady=10)

caption_label = tk.Label(root, wraplength=300)
caption_label.pack(pady=5)

# Charger le modèle de génération d'images
pipe = StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")
# pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

# Si CUDA est disponible, utiliser le GPU
if torch.cuda.is_available():
    pipe = pipe.to("cuda")

# Lancer l'application
root.mainloop()
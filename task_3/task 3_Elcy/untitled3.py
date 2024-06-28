from diffusers import StableDiffusionPipeline

model_id = "hf-internal-testing/tiny-stable-diffusion-torch"
save_directory = "./tiny_stable_diffusion_local"

# Téléchargement du modèle
pipeline = StableDiffusionPipeline.from_pretrained(model_id)
pipeline.save_pretrained(save_directory)

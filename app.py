import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tkinter as tk
from tkinter.ttk import Progressbar
import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
import threading

# Create main application window
root = ctk.CTk()
root.geometry("600x750")
root.title("Abhijeet's Image Generator")
ctk.set_appearance_mode("dark")

# Prompt entry
prompt = ctk.CTkEntry(master=root, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white", placeholder_text="Enter Prompt")
prompt.place(x=10, y=10)

# Style Options
Style_label = ctk.CTkLabel(root, text="Style Options:", font=("Arial", 16))
Style_label.place(x=10, y=60)
style_options = {
    "Realism": "A realistic ",
    "Cartoon": "A cartoon drawing of ",
    "Abstract": "An abstract art showing ",
    "Fantasy": "A magical, fantasy scene of ",
    "Cyberpunk": "A futuristic, cyberpunk "
}

selected_style = ctk.StringVar(value="Realism") # Default Style
style_menu = ctk.CTkOptionMenu(root, variable=selected_style, values=list(style_options.keys()))
style_menu.place(x=120, y=60)

# Resolution Slider
resolution_label = ctk.CTkLabel(root, text="Resolution (px):", font=("Arial", 16))
resolution_label.place(x=10, y=100)
resolution_var = tk.IntVar(value=512)
resolution_slider = ctk.CTkSlider(root, from_=256, to=1024, variable=resolution_var, number_of_steps=8)
resolution_slider.place(x=140, y=107)
resolution_value_label = ctk.CTkLabel(root, textvariable=resolution_var, font=("Arial", 16))
resolution_value_label.place(x=350, y=100)

# Image display
lmain = ctk.CTkLabel(master=root, height=512, width=512)
lmain.place(x=10, y=180)

# Progress Bar with label
progress_label = ctk.CTkLabel(root, text="Progress:", font=("Arial", 16))
progress_label.place(x=10, y=700)
progress = Progressbar(root, mode='indeterminate')
progress.place(x=100, y=700)

# Error label
error_label = ctk.CTkLabel(root, text="Prompt cannot be Empty!", font=("Arial", 16), text_color="crimson")
error_label.place(x=150, y=145)
        
# Load the Model
modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, torch_dtype=torch.float16, low_cpu_mem_usage=True)
pipe.to(device)

# task Function
def task(full_prompt, resolution):
    progress.start()
    try:
        with autocast(device):
            result = pipe(full_prompt, height=resolution, width=resolution, guidance_scale=8.5)
        image = result["images"][0]

        image.save(f'generated_image.png')   
            
        # Display the generated image
        img = CTkImage(light_image=image, size=(512, 512))
        lmain.configure(image=img)
        lmain.image = img
    except Exception as e:
        error_label.configure(text=f"Error: {str(e)}", text_color="crimson")
    finally:
        progress.stop()

# Toggle Appearance Mode
def toggle_mode():
    if ctk.get_appearance_mode().lower() == "light":
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

toggle_button = ctk.CTkButton(root, text="Toggle Mode", command=toggle_mode)
toggle_button.place(x=300, y=60)

# Generate function
def generate():    
    user_input = prompt.get()
    if not user_input.strip():  
        error_label.configure(text="Prompt cannot be Empty!")
        return

    error_label.configure(text="")

    style_prefix = style_options[selected_style.get()]
    full_prompt = f"{style_prefix} {prompt.get()}"
    resolution = resolution_var.get()

    threading.Thread(target=task, args=(full_prompt, resolution)).start()

# Generate Button
trigger = ctk.CTkButton(master=root, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="navy", command=generate)
trigger.configure(text="Generate")
trigger.place(x=10, y=140)

root.mainloop()
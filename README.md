# Stable-Diffusion-UI 🖼️
A user-friendly graphical interface for generating stunning AI-powered images using Stable Diffusion. Customize prompts, styles, and resolutions in a seamless workflow to bring your imagination to life.

## Credits 🤖
[![I tried to build a ML Text to Image App with Stable Diffusion in 15 Minutes](https://img.youtube.com/vi/7xc0Fs3fpCg&list=LL/0.jpg)](https://www.youtube.com/watch?v=7xc0Fs3fpCg&list=LL) - 
**Nicholas Renotte**.
The base code for this project was adapted from Nicholas Renotte. While the original concept and code were used as a foundation, several modifications were made to suit the specific functionality and features of this User Interface.

## Demo 🎬

## The Code files: 📄
**app.py:** creates a user-friendly graphical interface for generating images using the Stable Diffusion model. It allows users to input a text prompt, select artistic styles, adjust resolution, and toggle between dark and light themes. The script integrates a pre-trained Stable Diffusion pipeline for image generation, displays the output within the application, and saves the generated image locally.

## Functionality ⚙️
**GUI Setup:** CustomTkinter is used to build a modern and user-friendly interface for image generation.

**Prompt Input and Validation:** The user can enter a prompt, which is validated to ensure it is not empty.

**Style Selection:** Users can select from predefined artistic styles to influence the generated image (e.g., "Realism", "Cartoon", "Abstract", "Fantasy", "Cyberpunk").

**Resolution Control:** The image resolution is adjustable via a slider (from 256px to 1024px)..

**Stable Diffusion Model:** A pre-trained Stable Diffusion model is loaded and used for image generation.

**Background Processing:** The image generation process is run in a separate thread to prevent UI freezes.

**Error Handling:** Basic error handling is implemented for user input and model issues.

**Image Display and Saving:** The generated image is displayed in the app and saved locally.

**Appearance Mode Toggle:** The user can switch between light and dark modes for the app's interface.

**Multithreading:** Ensures smooth UI interaction during image generation.

## Installation 💻
To run the app.py Stable Diffusion project, you'll need to install the following dependencies:

*pip install torch==2.5.1*    -  download from here: **https://pytorch.org/**

*pip install customtkinter==5.2.2*

*pip install diffusers==0.31.0*  

*pip install Pillow==10.2.0*  

## How to get Hugging FaceToken 🤗
go to this website: https://huggingface.co/docs/hub/security-tokens

sign-up:

![image](https://github.com/user-attachments/assets/c4bad170-a606-4bbe-9636-d551e809b93c)

then go to settings and access tokens:

![image](https://github.com/user-attachments/assets/736101db-f6bc-4e02-b062-c4637e0342a0)

and create new token (**remember to store your token somewhere safe else they will remove leaked tokens**):

![image](https://github.com/user-attachments/assets/72a80eec-cd1e-4a88-8ae8-daae8d1952b1)






# Stable-Diffusion-UI 🖼️
A user-friendly graphical interface for generating stunning AI-powered images using Stable Diffusion. Customize prompts, styles, and resolutions in a seamless workflow to bring your imagination to life.

## Credits 🤖
[![I tried to build a ML Text to Image App with Stable Diffusion in 15 Minutes](https://img.youtube.com/vi/7xc0Fs3fpCg&list=LL/0.jpg)](https://www.youtube.com/watch?v=7xc0Fs3fpCg&list=LL) - 
**Nicholas Renotte**.
The base code for this project was adapted from Nicholas Renotte. While the original concept and code were used as a foundation, several modifications were made to suit the specific functionality and features of this User Interface.

## Demo 🎬

**The functional Demo** ✅

https://github.com/user-attachments/assets/e72188da-633b-472a-96b2-f934cfb0f9ef

**GPU Demand:** High-Resolution vs. Low-Resolution 💵

https://github.com/user-attachments/assets/bca81654-f65c-45e5-bc24-f046ebd04b02

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

## How to run the code: 🛠️
paste this in terminal: *huggingface-cli login*

**the output** should be like this:

![image](https://github.com/user-attachments/assets/a008142d-9e30-4d2a-bbb9-c84ee473eada)
the **red arrow** is where you paste the token by just right clicking (**Nothing else**) you will not see it visible but it has been pasted

the **blue arrow** is if you want to add token as a git credential up to you but I did no.

the final output should be *Login successful.*

## The Theory: 💡
Stable Diffusion is a **latent diffusion model** designed to generate images from text. It uses advanced machine learning techniques to efficiently create realistic and creative images. Here's how it works and the key theoretical concepts involved:

**What is a Diffusion Model?**
These are generative models that learn to create new data (like images) similar to what they've seen during training. Inspired by the concept of physical diffusion (e.g., ink spreading in water), these models corrupt images with noise and then learn to reverse this process.

**Forward Diffusion**
Images are gradually turned into noise.
Example: A clear cat image becomes completely random noise.
![image](https://github.com/user-attachments/assets/22a65eea-78d8-42c7-9e71-5153e29c502b)

**Reverse Diffusion**
Starting from noise, the model predicts and removes noise step-by-step to recreate an image.
Example: Recovering either a dog or cat image from noise, depending on the learned patterns.
![image](https://github.com/user-attachments/assets/27a3766b-f213-403b-a373-832b750c8b4a)

The image space is huge a 512x512 RGB image has ~786,000 dimensions, which makes direct operations computationally expensive. hence why Stable Diffusion works in a **latent space**, a compressed representation of images. 48 times smaller so it reaps the benefit of crunching a lot fewer numbers. That’s why it’s a lot faster.

**The Variational Autoencoder (VAE)** neural network has two parts: 

**(1) Encoder** compresses an image to a lower dimensional representation in the latent space.

**(2) Decoder** restores the image from the latent space.

## Training Stable Diffusion 📚

**Latent Noise in Latent Space:**
Instead of directly adding noise to pixel images, noise is added to a compressed latent space (instead of generating a noisy image, it generates a random tensor in latent space (latent noise)). This speeds up training since the latent space is much smaller than pixel space.

**Noise Prediction:**
A U-Net model learns to predict and remove this noise from the latent space. It is trained using many examples of noisy latent images.

**Reverse Diffusion:**
During generation, the U-Net removes noise step-by-step from a random latent tensor until a clean latent representation is formed, which is then decoded into the final image.

![cat](https://github.com/user-attachments/assets/b44035cc-29eb-4b1e-8645-58c264fb5da6)

## How Text Guides Image Generation: 🔋

**Tokenization:**
Words in the text prompt are broken into tokens. For example, "blue sky" becomes tokens for "blue" and "sky."

**Embeddings:**
Each token is converted into a 768-dimensional vector that captures its meaning. These embeddings represent the prompt in a way the model can understand.

**Cross-Attention:**
The model links parts of the text (e.g., "blue" and "sky") to parts of the latent image. This ensures the image aligns with the prompt during generation.

![image](https://github.com/user-attachments/assets/9b70e0e6-3feb-464e-ad81-a1377b42698b)



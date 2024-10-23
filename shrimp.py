import tkinter as tk
from PIL import Image, ImageTk
import pygame

# Initialize pygame for playing audio
pygame.mixer.init()

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def show_result(is_shrimp):
    if is_shrimp:
        # Show shrimp image and play shrimp sound
        shrimp_img = ImageTk.PhotoImage(Image.open("assets/shrimp_image.jpeg"))
        image_label.config(image=shrimp_img)
        image_label.image = shrimp_img
        play_sound("assets/shrimp_sound.mp3")
    else:
        # Show non-shrimp image and play non-shrimp sound
        not_shrimp_img = ImageTk.PhotoImage(Image.open("assets/not_shrimp.jpeg"))
        image_label.config(image=not_shrimp_img)
        image_label.image = not_shrimp_img
        play_sound("assets/not_shrimp_sound.mp3")

# Tkinter window setup
root = tk.Tk()
root.title("Are you a shrimp?")
root.geometry("1920x1080")

# Question label
question_label = tk.Label(root, text="Are you a shrimp?", font=("Arial", 16))
question_label.pack(pady=20)

# Yes button for shrimp
shrimp_button = tk.Button(root, text="Yes", command=lambda: show_result(True), font=("Arial", 14))
shrimp_button.pack(side="left", padx=30)

# No button for not a shrimp
not_shrimp_button = tk.Button(root, text="No", command=lambda: show_result(False), font=("Arial", 14))
not_shrimp_button.pack(side="right", padx=30)

# Label to show the image
image_label = tk.Label(root)
image_label.pack(pady=20)

# Start the application
root.mainloop()

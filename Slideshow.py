from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow")

image_paths = [
    r"C:\Users\Shailav\OneDrive\Pictures\Screenshots\Screenshot (1).png",
    r"C:\Users\Shailav\OneDrive\Pictures\Screenshots\Screenshot (2).png",
    r"C:\Users\Shailav\OneDrive\Pictures\Screenshots\Screenshot (3).png",
    r"C:\Users\Shailav\OneDrive\Pictures\Screenshots\Screenshot (9).png",
    r"C:\Users\Shailav\OneDrive\Pictures\Screenshots\Screenshot (10).png"
]

image_size = (1080, 1080)

images = [
    ImageTk.PhotoImage(Image.open(p).resize(image_size))
    for p in image_paths
]

slideshow = cycle(images)

label = tk.Label(root)
label.pack()

running = False

def update_image():
    if running:
        img = next(slideshow)
        label.config(image=img)
        label.image = img
        root.after(3000, update_image)

def start_slideshow():
    global running
    running = True
    update_image()

play_button = tk.Button(root, text="Start Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()
 
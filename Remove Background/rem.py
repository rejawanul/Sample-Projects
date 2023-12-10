import rembg
from PIL import Image
import tkinter as tk
from tkinter import filedialog

class BackgroundRemoverApp:
    def __init__(self, master):
        self.master = master
        master.title("Background Remover App")

        self.canvas = tk.Canvas(master, width=300, height=300, bg="white")
        self.canvas.pack()

        self.select_button = tk.Button(master, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=10)

        self.remove_button = tk.Button(master, text="Remove Background", command=self.remove_background)
        self.remove_button.pack(pady=10)

    def select_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def remove_background(self):
        if hasattr(self, "image_path"):
            input_path = self.image_path
            output_path = "output.png"  # You can change the output path as needed

            with rembg.open(input_path) as input_file, open(output_path, "wb") as output_file:
                output_file.write(input_file.read())

            self.display_image(output_path)
        else:
            tk.messagebox.showinfo("Error", "Please select an image first.")

if __name__ == "__main__":
    try:
        import tkinter as tk
        from tkinter import filedialog, messagebox
        from PIL import Image, ImageTk
    except ImportError:
        raise ImportError("Please install the required dependencies: rembg, Pillow, tkinter")

    root = tk.Tk()
    app = BackgroundRemoverApp(root)
    root.mainloop()

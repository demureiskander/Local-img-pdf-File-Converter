import customtkinter as ctk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from converter import convert_images
import threading
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class ImageConverterApp(TkinterDnD.Tk):

    def __init__(self):
        super().__init__()

        self.title("ImageFlow")
        self.geometry("700x560")

        self.files = []

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.drop_label = ctk.CTkLabel(
            self.frame,
            text="Drag & Drop Images Here\nor click 'Add Images'",
            height=80
        )
        self.drop_label.pack(fill="x", pady=10)
        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind("<<Drop>>", self.on_drop)

        self.add_btn = ctk.CTkButton(
            self.frame, text="Add Images", command=self.add_files
        )
        self.add_btn.pack(pady=5)

        self.list_frame = ctk.CTkScrollableFrame(
            self.frame, height=180
        )
        self.list_frame.pack(fill="x", pady=10)

        self.format_var = ctk.StringVar(value="PNG")
        self.format_menu = ctk.CTkOptionMenu(
            self.frame,
            values=["JPG", "PNG", "WEBP", "PDF"],
            variable=self.format_var,
            command=self.on_format_change
        )
        self.format_menu.pack(pady=10)

        self.quality_label = ctk.CTkLabel(self.frame, text="Quality")
        self.quality_slider = ctk.CTkSlider(
            self.frame, from_=10, to=100, number_of_steps=18
        )
        self.quality_slider.set(90)

        self.dpi_label = ctk.CTkLabel(self.frame, text="DPI (PDF)")
        self.dpi_entry = ctk.CTkEntry(self.frame)
        self.dpi_entry.insert(0, "300")

        self.progress = ctk.CTkProgressBar(self.frame)
        self.progress.set(0)
        self.progress.pack(fill="x", pady=15)

        self.status = ctk.CTkLabel(self.frame, text="")
        self.status.pack()

        self.convert_btn = ctk.CTkButton(
            self.frame, text="Convert", command=self.start_conversion
        )
        self.convert_btn.pack(pady=10)

        self.on_format_change("PNG")

    def add_files(self):
        files = filedialog.askopenfilenames(
            filetypes=[("Images", "*.png *.jpg *.jpeg *.webp *.bmp *.tiff")]
        )
        self.add_to_list(files)

    def on_drop(self, event):
        files = self.tk.splitlist(event.data)
        self.add_to_list(files)

    def add_to_list(self, files):
        for file in files:
            if file not in self.files and os.path.isfile(file):
                self.files.append(file)
                self.render_file(file)

    def render_file(self, file):
        row = ctk.CTkFrame(self.list_frame)
        row.pack(fill="x", pady=2)

        label = ctk.CTkLabel(row, text=os.path.basename(file), anchor="w")
        label.pack(side="left", fill="x", expand=True, padx=5)

        remove_btn = ctk.CTkButton(
            row, text="✕", width=30,
            command=lambda: self.remove_file(file, row)
        )
        remove_btn.pack(side="right", padx=5)

    def remove_file(self, file, row):
        if file in self.files:
            self.files.remove(file)
        row.destroy()

    def on_format_change(self, value):
        self.quality_label.pack_forget()
        self.quality_slider.pack_forget()
        self.dpi_label.pack_forget()
        self.dpi_entry.pack_forget()

        if value == "PDF":
            self.dpi_label.pack()
            self.dpi_entry.pack(pady=5)
        else:
            self.quality_label.pack()
            self.quality_slider.pack(pady=5)

    def start_conversion(self):
        if not self.files:
            self.status.configure(text="No files selected")
            return

        output_dir = filedialog.askdirectory()
        if not output_dir:
            return

        self.progress.set(0)
        self.status.configure(text="Converting...")

        threading.Thread(
            target=self.convert_thread,
            args=(output_dir,),
            daemon=True
        ).start()

    def convert_thread(self, output_dir):
        def update_progress(current, total):
            self.progress.set(current / total)

        count = convert_images(
            self.files,
            output_dir,
            self.format_var.get(),
            int(self.quality_slider.get()),
            int(self.dpi_entry.get()) if self.format_var.get() == "PDF" else 300,
            update_progress
        )

        self.status.configure(
            text=f"Converted {count} files successfully"
        )


if __name__ == "__main__":
    app = ImageConverterApp()
    app.mainloop()

import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk, ImageOps
import os
import time
from tkinter import ttk
from sklearn.cluster import KMeans
import numpy as np

def boot_screen():
    boot = tk.Toplevel()
    boot.geometry("600x400")
    boot.configure(bg="black")
    boot_label = tk.Label(boot, text="BOOTING", font=("Helvetica", 40), fg="white", bg="black")
    boot_label.pack(pady=100)
    progress = ttk.Progressbar(boot, orient="horizontal", length=400, mode="determinate")
    progress.pack(pady=50)
    
    def update_progress(value):
        progress['value'] = value
        if value < 100:
            boot.after(50, lambda: update_progress(value + 2))
        else:
            boot.after(500, boot.destroy)

    update_progress(0)

    root.withdraw()  # Hide main window during boot
    boot.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable closing during boot
    boot.after(4500, lambda: root.deiconify())  # Show main window after booting

root = tk.Tk()
root.title("Moodboard")
root.geometry("1400x900")
root.configure(bg="#2d3436")

boot_screen()

canvas = tk.Canvas(root, bg="white", scrollregion=(0, 0, 1200, 1000), bd=0)
hbar = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
hbar.pack(side="bottom", fill="x")
vbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
vbar.pack(side="right", fill="y")
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(fill="both", expand=True)

frame = tk.Frame(canvas, bg="lightgrey")
canvas.create_window((0, 0), window=frame, anchor="nw", width=1200, height=1000)

img_list = []
undo_list = []
redo_list = []

toolbar = tk.Frame(root, bg="#74b9ff")
toolbar.pack(side="top", fill="x", padx=10, pady=10)

status = tk.Label(root, text="", bd=1, relief="sunken", anchor="w", bg="#2d3436", fg="white", font=("Helvetica", 10))
status.pack(side="bottom", fill="x")

def clr_pick():
    color = colorchooser.askcolor()[1]
    if color:
        for lbl in img_list:
            lbl.config(bg=color)
        status.config(text=f"Applied color: {color}")

def add_img():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Image", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg")))
    if filename:
        load_img(filename)

def load_img(file):
    img = Image.open(file)
    img = img.resize((200, 200), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    lbl = tk.Label(frame, image=img_tk, bg="white", cursor="fleur", bd=2, relief="groove")
    lbl.image = img_tk
    lbl.bind("<B1-Motion>", lambda e: mv_el(e, lbl))
    lbl.bind("<Button-3>", lambda e: rmv_el(lbl))
    lbl.bind("<Button-2>", lambda e: rot_el(lbl))
    lbl.pack(padx=10, pady=10)
    img_list.append(lbl)
    undo_list.append(('add', lbl))
    status.config(text="Image added")

def mv_el(event, el):
    el.place(x=event.x_root - el.winfo_width() // 2, y=event.y_root - el.winfo_height() // 2)

def rmv_el(el):
    el.destroy()
    undo_list.append(('remove', el))
    status.config(text="Element removed")

def rot_el(el):
    img = el.image._PhotoImage__photo.zoom(1)
    img = img.transpose(Image.ROTATE_90)
    el.image = ImageTk.PhotoImage(img)
    el.config(image=el.image)

def connect_els():
    if len(img_list) >= 2:
        coords1 = img_list[0].winfo_rootx(), img_list[0].winfo_rooty()
        coords2 = img_list[1].winfo_rootx(), img_list[1].winfo_rooty()
        canvas.create_line(coords1, coords2, fill="black", width=2)
        status.config(text="Connected elements")

def extract_colors(image, n_colors=5):
    img = np.array(image)
    img = img.reshape((-1, 3))
    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(img)
    colors = kmeans.cluster_centers_.astype(int)
    display_palette(colors)

def display_palette(colors):
    palette_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
    palette_frame.pack(side="bottom", pady=10)
    for color in colors:
        color_hex = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
        tk.Label(palette_frame, bg=color_hex, width=10, height=2, relief="flat", bd=1).pack(side="left", padx=5)

def add_txt():
    txt_win = tk.Toplevel(root)
    txt_win.title("Add Text")
    txt_win.geometry("300x200")
    txt_win.configure(bg="#f4f4f4")
    tk.Label(txt_win, text="Enter your text:", bg="#f4f4f4").pack(pady=10)
    txt_entry = tk.Entry(txt_win, width=30)
    txt_entry.pack(pady=10)

    def save_txt():
        txt = txt_entry.get()
        if txt:
            txt_lbl = tk.Label(frame, text=txt, font=("Monospace", 12), bg="white", cursor="fleur", bd=2, relief="groove")
            txt_lbl.bind("<B1-Motion>", lambda e: mv_el(e, txt_lbl))
            txt_lbl.bind("<Button-3>", lambda e: rmv_el(txt_lbl))
            txt_lbl.pack(padx=10, pady=10)
            undo_list.append(('add', txt_lbl))
            status.config(text="Text added")
        txt_win.destroy()

    tk.Button(txt_win, text="Add Text", command=save_txt, bg="#74b9ff", fg="white", bd=0, relief="flat", font=("Helvetica", 10), cursor="hand2").pack(pady=10)

def undo():
    if undo_list:
        action, el = undo_list.pop()
        if action == 'add':
            el.destroy()
            redo_list.append(('remove', el))
        elif action == 'remove':
            el.pack(padx=10, pady=10)
            redo_list.append(('add', el))
        status.config(text="Undo completed")

def redo():
    if redo_list:
        action, el = redo_list.pop()
        if action == 'add':
            el.pack(padx=10, pady=10)
            undo_list.append(('add', el))
        elif action == 'remove':
            el.destroy()
            undo_list.append(('remove', el))
        status.config(text="Redo completed")

def save_board():
    try:
        canvas.postscript(file="moodboard.ps", colormode="color")
        img = Image.open("moodboard.ps")
        img.save("moodboard.png", "png")
        os.remove("moodboard.ps")
        messagebox.showinfo("Save", "Moodboard saved")
        status.config(text="Moodboard saved")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving moodboard: {e}")
        status.config(text="Error saving moodboard")

tk.Button(toolbar, text="Add Image", command=add_img, bg="#74b9ff", fg="white", padx=10, pady=5).pack(side="left", padx=10)
tk.Button(toolbar, text="Add Text", command=add_txt, bg="#74b9ff", fg="white", padx=10, pady=5).pack(side="left", padx=10)
tk.Button(toolbar, text="Connect Elements", command=connect_els, bg="#74b9ff", fg="white", padx=10, pady=5).pack(side="left", padx=10)
tk.Button(toolbar, text="Pick Color", command=clr_pick, bg="#74b9ff", fg="white", padx=10, pady=5).pack(side="left", padx=10)
tk.Button(toolbar, text="Undo", command=undo, bg="#74b9ff", fg="white", padx=10, pady=5).pack(side="left", padx=10)
tk.Button(toolbar, text="Redo", command=redo, bg="#74b9ff", fg="white", padx=10, pady=5).pack(side="left", padx=10)
tk.Button(toolbar, text="Save", command=save_board, bg="#74b9ff", fg="white", padx=10, pady=5).pack(side="left", padx=10)

root.mainloop()

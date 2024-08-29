import tkinter as tk
from tkinter import filedialog, messagebox

class CatatanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Catatan")
        self.root.geometry("600x400")
        
        self.text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(expand=True, fill=tk.BOTH)
        
        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)
        
        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Simpan", command=self.save_file)
        self.file_menu.add_command(label="Keluar", command=root.quit)
    
    def save_file(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text files", "*.txt"),
                                                                ("All files", "*.*")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                messagebox.showinfo("Sukses", "File berhasil disimpan!")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan saat menyimpan file: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CatatanApp(root)
    root.mainloop()

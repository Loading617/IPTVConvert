import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class CustomDropdownMenu(tk.Menu):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, tearoff=0, **kwargs)
        self.parent = parent

    def add_option(self, option, command=None):
        self.add_command(label=option, command=command)

    def add_submenu(self, label):
        submenu = CustomDropdownMenu(self)
        self.add_cascade(label=label, menu=submenu)
        return submenu

    def add_separator(self):
        self.add_separator()


class IPTVConvert(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("IPTVConvert")
        self.geometry("920x570")

        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        self.file_menu = CustomDropdownMenu(self.menu_bar)
        self.edit_menu = CustomDropdownMenu(self.menu_bar)
        self.tools_menu = CustomDropdownMenu(self.menu_bar)
        self.view_menu = CustomDropdownMenu(self.menu_bar)
        self.help_menu = CustomDropdownMenu(self.menu_bar)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.menu_bar.add_cascade(label="Tools", menu=self.tools_menu)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        self.create_file_menu()
        self.create_edit_menu()
        self.create_tools_menu()
        self.create_view_menu()
        self.create_help_menu()

        self.create_treeview()

    def create_file_menu(self):
        self.file_menu.add_option("Open Playlist...", lambda: print("Open"))
        self.file_menu.add_option("Save Playlist...", lambda: print("Save"))
        self.file_menu.add_option("Save As...", lambda: print("Save As"))
        self.file_menu.add_option("Import from URL...", lambda: print("Import"))
        self.file_menu.add_option("Export to Format...", lambda: print("Export"))
        self.file_menu.add_option("Exit", self.quit)

        self.file_menu.add_separator()

        sub_menu = self.file_menu.add_submenu("Export to Format")
        sub_menu.add_option(".M3U")
        sub_menu.add_option(".M3U8")
        sub_menu.add_option(".JSON")
        sub_menu.add_option(".TXT")

    def create_edit_menu(self):
        self.edit_menu.add_option("Undo")
        self.edit_menu.add_option("Redo")
        self.edit_menu.add_option("Cut")
        self.edit_menu.add_option("Copy")
        self.edit_menu.add_option("Paste")
        self.edit_menu.add_option("Find & Replace...")
        self.edit_menu.add_option("Batch Edit Channels...")

        self.edit_menu.add_separator()

    def create_tools_menu(self):
        self.tools_menu.add_option("Validate Playlist")
        self.tools_menu.add_option("Remove Duplicates")
        self.tools_menu.add_option("Sort Channels")
        self.tools_menu.add_option("Convert Encoding")
        self.tools_menu.add_option("Edit Channel Metadata...")
        self.tools_menu.add_option("Generate EPG (XMLTV)...")
        self.tools_menu.add_option("Customize Output")

        self.tools_menu.add_separator()

        sub_menu = self.tools_menu.add_submenu("Sort Channels")
        sub_menu.add_option("By Name")
        sub_menu.add_option("By Category")
        sub_menu.add_option("By URL")

        sub_menu = self.tools_menu.add_submenu("Convert Encoding")
        sub_menu.add_option("UTF-8")
        sub_menu.add_option("ANSI")
        sub_menu.add_option("ISO-8859-1")

    def create_view_menu(self):
        self.view_menu.add_option("Show Grid/List View")
        self.view_menu.add_option("Show Channel Logos")
        self.view_menu.add_option("Toggle Dark Mode")

        self.view_menu.add_separator()

    def create_help_menu(self):
        self.help_menu.add_option("User Guide")
        self.help_menu.add_option("Shortcuts Reference")
        self.help_menu.add_option("Check for Update")
        self.help_menu.add_option("About IPTVConvert")

    def create_treeview(self):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("#", "Channel Name", "URL", "Category", "Language", "Resolution", "Bitrate", "EPG ID")

        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=20)

        self.tree.heading("#", text="#")
        self.tree.heading("Channel Name", text="Channel Name")
        self.tree.heading("URL", text="Stream URL")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Language", text="Language")
        self.tree.heading("Resolution", text="Resolution")
        self.tree.heading("Bitrate", text="Bitrate")
        self.tree.heading("EPG ID", text="EPG ID")

        self.tree.column("#", width=40, anchor="center")
        self.tree.column("Channel Name", width=200)
        self.tree.column("URL", width=250)
        self.tree.column("Category", width=100, anchor="center")
        self.tree.column("Language", width=100, anchor="center")
        self.tree.column("Resolution", width=80, anchor="center")
        self.tree.column("Bitrate", width=80, anchor="center")
        self.tree.column("EPG ID", width=100, anchor="center")

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tree.insert("", "end", values=(1, "ESPN", "http://stream.espn.com/live.m3u8", "Sports", "English", "1080p", "4000kbps", "ESPN_US"))

if __name__ == "__main__":
    app = IPTVConvert()
    app.mainloop()

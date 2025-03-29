import customtkinter as ctk

class IPTVConvert(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("IPTVConvert")
        self.geometry("920x570")
        self.menu = ctk.CTkTitleMenu(root)

        self.file_menu = self.menu.add_cascade("File")
        self.edit_menu = self.menu.add_cascade("Edit")
        self.tools_menu = self.menu.add_cascade("Tools")
        self.view_menu = self.menu.add_cascade("View")
        self.help_menu = self.menu.add_cascade("Help")

        self.create_file_menu()
        self.create_edit_menu()
        self.create_tools_menu()
        self.create_view_menu()
        self.create_help_menu()

    def create_file_menu(self):
        """Create the File menu dropdown options."""
        dropdown = CustomDropdownMenu(widget=self.file_menu)
        dropdown.add_option(option="Open Playlist...", command=lambda: print("Open"))
        dropdown.add_option(option="Save Playlist...", command=lambda: print("Save"))
        dropdown.add_option(option="Save As...", command=lambda: print("Save As"))
        dropdown.add_option(option="Import from URL...", command=lambda: print("Import"))
        dropdown.add_option(option="Export to Format...", command=lambda: print("Export"))
        dropdown.add_option(option="Exit", command=lambda: print("Exit"))

        dropdown.add_separator()

        sub_menu = dropdown.add_submenu("Export to Format")
        sub_menu.add_option(option=".M3U")
        sub_menu.add_option(option=".M3U8")
        sub_menu.add_option(option=".JSON")
        sub_menu.add_option(option=".TXT")

    def create_edit_menu(self):
        """Create the Edit menu dropdown options."""
        dropdown = CustomDropdownMenu(widget=self.edit_menu)
        dropdown.add_option(option="Undo")
        dropdown.add_option(option="Redo")
        dropdown.add_option(option="Cut")
        dropdown.add_option(option="Copy")
        dropdown.add_option(option="Paste")
        dropdown.add_option(option="Find & Replace...")
        dropdown.add_option(option="Batch Edit Channels...")

        dropdown.add_separator()

    def create_tools_menu(self):
        """Create the Tools menu dropdown options."""
        dropdown = CustomDropdownMenu(widget=self.tools_menu)
        dropdown.add_option(option="Validate Playlist")
        dropdown.add_option(option="Remove Validates")
        dropdown.add_option(option="Sort Channels")
        dropdown.add_option(option="Convert Encoding")
        dropdown.add_option(option="Edit Channel Metadata...")
        dropdown.add_option(option="Generate EPG (XMLTV)...")
        dropdown.add_option(option="Customize Output")

        dropdown.add_separator()

        sub_menu = dropdown.add_submenu("Sort Channels")
        sub_menu.add_option(option="By Name")
        sub_menu.add_option(option="By Category")
        sub_menu.add_option(option="By URL")

        sub_menu = dropdown.add_submenu("Convert Encoding")
        sub_menu.add_option(option="UTF-8")
        sub_menu.add_option(option="ANSI")
        sub_menu.add_option(option="ISO-8859-1")

    def create_view_menu(self):
        """Create the View menu dropdown options."""
        dropdown = CustomDropdownMenu(widget=self.view_menu)
        dropdown.add_option(option="Show Grid/List View")
        dropdown.add_option(option="Show Channel Logos")
        dropdown.add_option(option="Toggle Dark Mode")

        dropdown.add_separator()

    def create_help_menu(self):
        """Create the Help menu dropdown options."""
        dropdown = CustomDropdownMenu(widget=self.help_menu)
        dropdown.add_option(option="User Guide")
        dropdown.add_option(option="Shortcuts Reference")
        dropdown.add_option(option="Check for Update")
        dropdown.add_option(option="About IPTVConvert")

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

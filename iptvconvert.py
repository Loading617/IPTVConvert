import customtkinter
from CTkMenuBar import *

root = customtkinter.CTk()
root.geometry("600x200")
root.title("IPTVConvert")

menu = CTkTitleMenu(root)
button_1 = menu.add_cascade("File")
button_2 = menu.add_cascade("Edit")
button_3 = menu.add_cascade("Tools")
button_4 = menu.add_cascade("View")
button_5 = menu.add_cascade("Help")

dropdown1 = CustomDropdownMenu(widget=button_1)
dropdown1.add_option(option="Open Playlist...", command=lambda: print("Open"))
dropdown1.add_option(option="Save Playlist...", command=lambda: print("Save"))
dropdown1.add_option(option="Save As...", command=lambda: print("Save"))
dropdown1.add_option(option="Import from URL...", command=lambda: print("Import"))
dropdown1.add_option(option="Export to Format...", command=lambda: print("Export"))
dropdown1.add_option(option="Exit", command=lambda: print("Exit"))

dropdown1.add_separator()

sub_menu = dropdown1.add_submenu("Export to Format")
sub_menu.add_option(option=".M3U")
sub_menu.add_option(option=".M3U8")
sub_menu.add_option(option=".JSON")
sub_menu.add_option(option=".TXT")

dropdown2 = CustomDropdownMenu(widget=button_2)
dropdown2.add_option(option="Undo")
dropdown2.add_option(option="Redo")
dropdown2.add_option(option="Cut")
dropdown2.add_option(option="Copy")
dropdown2.add_option(option="Paste")
dropdown2.add_option(option="Find & Replace...")
dropdown2.add_option(option="Batch Edit Channels...")

dropdown2.add_separator()

dropdown3 = CustomDropdownMenu(widget=button_3)
dropdown3.add_option(option="Validate Playlist")
dropdown3.add_option(option="Remove Validates")
dropdown3.add_option(option="Sort Channels")
dropdown3.add_option(option="Convert Encoding")
dropdown3.add_option(option="Edit Channel Metadata...")
dropdown3.add_option(option="Generate EPG (XMLTV)...")
dropdown3.add_option(option="Customize Output")

dropdown3.add_separator()

sub_menu = dropdown3.add_submenu("Sort Channels")
sub_menu.add_option(option="By Name")
sub_menu.add_option(option="By Category")
sub_menu.add_option(option="By URL")

sub_menu = dropdown3.add_submenu("Convert Encoding")
sub_menu.add_option(option="UTF-8")
sub_menu.add_option(option="ANSI")
sub_menu.add_option(option="ISO-8859-1")

dropdown4 = CustomDropdownMenu(widget=button_4)
dropdown4.add_option(option="Show Grid/List View")
dropdown4.add_option(option="Show Channel Logos")
dropdown4.add_option(option="Toggle Dark Mode")

dropdown4.add_separator()

dropdown5 = CustomDropdownMenu(widget=button_5)
dropdown5.add_option(option="User Guide")
dropdown5.add_option(option="Shortcuts Reference")
dropdown5.add_option(option="Check for Update")
dropdown5.add_option(option="About IPTVConvert")

root.mainloop()

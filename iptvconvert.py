import customtkinter
from CTkMenuBar import *

root = customtkinter.CTk()
root.geometry("600x200")
root.title("IPTVConvert")

menu = CTkMenuBar(root)
button_1 = menu.add_cascade("File")
button_2 = menu.add_cascade("Edit")
button_3 = menu.add_cascade("Tools")
button_4 = menu.add_cascade("View")
button_5 = menu.add_cascade("Help")
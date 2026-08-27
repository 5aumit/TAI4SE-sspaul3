import os
import tkinter as tk
from tkinter import messagebox
from os.path import join

from pynput import keyboard

from src.save_count import SaveCount


class MainApplication(tk.Frame):

    def __init__(self, root: tk.Tk):
        super().__init__(root)
        self.root = root
        self.pack(padx=32, pady=32, expand=True)

        self.root.option_add("*tearOff", False)
        self.root.title("Counter")

        frm_buttons = tk.Frame(self)
        frm_buttons.grid(row=0, column=0)

        self.var_count = tk.IntVar(frm_buttons)

        tk.Button(frm_buttons, textvariable=self.var_count, command=self.count_up, font="Times, 60") \
            .grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)

        tk.Button(frm_buttons, text="-1", command=self.count_down).grid(row=1, column=0)
        tk.Button(frm_buttons, text="Reset", command=self.reset).grid(row=1, column=1)
        tk.Button(frm_buttons, text="Save", command=self.save).grid(row=1, column=2)

        # tk.Button(frm_buttons, text="Undecorated Window", command=None).grid(row=2, column=0, columnspan=3)

        self.selected_count = ""

        self.lst_counts = tk.Listbox(self)
        self.lst_counts.grid(row=0,  column=1)
        self.lst_counts.bind("<<ListboxSelect>>", self.listbox_select)
        self.lst_counts.bind("<Button-3>", self.right_click)

        self.men_list = tk.Menu(self)
        self.men_list.add_command(label="Delete Selected", command=self.delete_save)

        self.root.bind("<Key>", self.key_press)

        try:
            saves = os.listdir("data")
        except FileNotFoundError:
            os.mkdir("data")
            messagebox.showerror("Save Error", "No data folder was found; created one now.")
            return
        for count_save in saves:
            self.lst_counts.insert(tk.END, count_save)

        listener = keyboard.Listener(on_release=self.on_key_release)
        listener.start()

    def count_up(self):
        # Save to entry, if it's the first one
        if self.var_count.get() == 0 and self.lst_counts.index(tk.END) == 0:
            SaveCount(tk.Toplevel(), self.save_to_listbox)
            return
        else:
            if not self.selected_count:
                messagebox.showerror("No Configuration Selected", "Please select a configuration.")
                return

        self.var_count.set(self.var_count.get() + 1)
        self.save_to_file(self.selected_count)

    def count_down(self):
        if not self.selected_count:
            messagebox.showerror("No Configuration Selected", "Please select a configuration.")
            return

        self.var_count.set(self.var_count.get() - 1)
        self.save_to_file(self.selected_count)

    def reset(self):
        if not self.selected_count:
            messagebox.showerror("No Configuration Selected", "Please select a configuration.")
            return

        choice = messagebox.askyesno("Reset", "Are you sure you want to reset the count?")
        if choice:
            self.var_count.set(0)
            self.save_to_file(self.selected_count)

    def save(self):
        SaveCount(tk.Toplevel(), self.save_to_listbox)

    def save_to_listbox(self, name: str):
        if self.save_to_file(name):  # If save is successful
            self.lst_counts.insert(tk.END, name)

    def save_to_file(self, name: str) -> bool:
        try:
            with open(join("data", name), "w") as file:
                file.write(str(self.var_count.get()))
                return True
        except FileNotFoundError:
            os.mkdir("data")
            messagebox.showerror("Save Error", "No data folder was found; created one now.")
            return False

    def delete_save(self):
        try:
            name_of_selected_count = self.lst_counts.get(int(self.lst_counts.curselection()[0]))
        except IndexError:
            return

        os.remove(join("data", name_of_selected_count))

        for i in range(self.lst_counts.size()):
            if self.lst_counts.get(i) == name_of_selected_count:
                self.lst_counts.delete(i)

    def listbox_select(self, event):
        widget = event.widget
        try:
            name_of_selected_count = widget.get(int(widget.curselection()[0]))
        except IndexError:
            return

        try:
            with open(join("data", name_of_selected_count), "r") as file:
                count = int(file.read())
        except FileNotFoundError:
            os.mkdir("data")
            messagebox.showerror("Save Error", "No data folder was found; created one now.")
            return

        self.var_count.set(count)
        self.selected_count = name_of_selected_count

    def right_click(self, event):
        self.men_list.tk_popup(event.x_root, event.y_root)

    def key_press(self, event):
        if event.char == " ":
            self.count_up()

    def on_key_release(self, key):
        if key == keyboard.KeyCode.from_char("+"):
            self.count_up()


def main():
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()

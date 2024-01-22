import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class TodoListApp:

    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        icon_path = "todo.png"
        self.root.iconbitmap(icon_path)

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=15, pady=15)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.load_tasks()


    def load_tasks(self):
        try:
            with open("todo_gui.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
                self.update_listbox()
        except FileNotFoundError:
            pass


    def save_tasks(self):
        with open("todo_gui.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")


    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


    def add_task(self):
        task = self.task_entry.get()
        if task:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task_with_timestamp = f"{task} - {timestamp}"
            self.tasks.append(task_with_timestamp)
            self.update_listbox()
            self.save_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")


    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to remove the selected task?")
            if confirmed:
                self.tasks.pop(selected_index[0])
                self.update_listbox()
                self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

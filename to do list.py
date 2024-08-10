print("Task - 1")
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import pickle
import os

TASKS_FILE = "tasks.pkl"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'rb') as f:
            return pickle.load(f)
    return {}

def save_tasks(tasks):
    with open(TASKS_FILE, 'wb') as f:
        pickle.dump(tasks, f)

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = load_tasks()
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Task Description:").pack(pady=5)
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=5)
        
        tk.Button(self.root, text="Add Task", command=self.add_task).pack(pady=5)
        tk.Button(self.root, text="View Tasks", command=self.view_tasks).pack(pady=5)
        tk.Button(self.root, text="Update Task", command=self.update_task).pack(pady=5)
        tk.Button(self.root, text="Delete Task", command=self.delete_task).pack(pady=5)
        
        self.task_list = tk.Text(self.root, height=15, width=50)
        self.task_list.pack(pady=10)

    def add_task(self):
        description = self.task_entry.get()
        if not description:
            messagebox.showwarning("Input Error", "Task description cannot be empty.")
            return
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = description
        save_tasks(self.tasks)
        self.task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Task added successfully.")

    def view_tasks(self):
        self.task_list.delete(1.0, tk.END)
        if not self.tasks:
            self.task_list.insert(tk.END, "No tasks found.")
        else:
            for task_id, description in self.tasks.items():
                self.task_list.insert(tk.END, f"{task_id}. {description}\n")

    def update_task(self):
        task_id = self.ask_for_task_id("Update")
        if task_id is None or task_id not in self.tasks:
            return
        new_description = self.task_entry.get()
        if not new_description:
            messagebox.showwarning("Input Error", "Task description cannot be empty.")
            return
        self.tasks[task_id] = new_description
        save_tasks(self.tasks)
        self.task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Task updated successfully.")

    def delete_task(self):
        task_id = self.ask_for_task_id("Delete")
        if task_id is None or task_id not in self.tasks:
            return
        del self.tasks[task_id]
        save_tasks(self.tasks)
        self.task_list.delete(1.0, tk.END)
        messagebox.showinfo("Success", "Task deleted successfully.")

    def ask_for_task_id(self, action):
        task_id_str = tk.simpledialog.askstring("Input", f"Enter task ID to {action.lower()}:")
        if task_id_str is None:
            return None
        try:
            task_id = int(task_id_str)
            return task_id
        except ValueError:
            messagebox.showwarning("Input Error", "Invalid task ID.")
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

print("All task noted...!")
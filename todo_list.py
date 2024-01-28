import tkinter as tk
from tkinter import messagebox
class ToDoListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("500x500")
        self.todo_list = []
        self.create_widgets()
        self.configure(bg="#B5E5CF")
    def create_widgets(self):
        # To-Do List
        self.listbox = tk.Listbox(  
        self,  
        width = 50,  
        height = 9,  
        font="bold",
        selectmode = 'SINGLE',  
        background = "WHITE",
        foreground="BLACK",    
        selectbackground = "#D4AC0D",  
        selectforeground="BLACK"
    )  
        self.listbox.pack(pady=10)
        self.display_list()
        # Add Task
        self.entry_task = tk.Entry(self, width=30)
        self.entry_task.pack(pady=5)
        self.button_add_task = tk.Button(self, text="Add Task",width =15,bg='#D4AC0D',command=self.add_task)
        self.button_add_task.pack()
        # Remove Task
        self.entry_index = tk.Entry(self, width=30)
        self.entry_index.pack(pady=5)
        self.button_remove_task = tk.Button(self, text="Remove Task",width =15,bg='#D4AC0D',command=self.remove_task)
        self.button_remove_task.pack()
        # Mark Task as Done
        self.entry_done_index = tk.Entry(self, width=30)
        self.entry_done_index.pack(pady=5)
        self.button_mark_done = tk.Button(self, text="Mark Task as Done",width =15,bg='#D4AC0D',command=self.mark_done)
        self.button_mark_done.pack()
        # Save and Load To-Do List
        self.entry_filename = tk.Entry(self, width=30)
        self.entry_filename.pack(pady=5)
        self.button_save = tk.Button(self, text="Save To-Do List",width =15,bg='#D4AC0D',command=self.save_to_file)
        self.button_save.pack()
    def display_list(self):
        self.listbox.delete(0, tk.END)
        for index, item in enumerate(self.todo_list, start=1):
            self.listbox.insert(tk.END, f"{index}. {'[X]' if item['done'] else '[ ]'} {item['task']}")
    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.todo_list.append({"task": task, "done": False})
            self.entry_task.delete(0, tk.END)
            self.display_list()
            messagebox.showinfo("Task Added", "Task added successfully!")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a task before adding.")
    def remove_task(self):
        try:
            task_index = int(self.entry_index.get())
            if 1 <= task_index <= len(self.todo_list):
                removed_task = self.todo_list.pop(task_index - 1)
                self.entry_index.delete(0, tk.END)
                self.display_list()
                messagebox.showinfo("Task Removed", f"Task '{removed_task['task']}' removed successfully!")
            else:
                messagebox.showwarning("Invalid Index", "Invalid task index.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please provide a valid task index.")
    def mark_done(self):
        try:
            task_index = int(self.entry_done_index.get())
            if 1 <= task_index <= len(self.todo_list):
                self.todo_list[task_index - 1]['done'] = True
                self.entry_done_index.delete(0, tk.END)
                self.display_list()
                messagebox.showinfo("Task Marked Done", "Task marked as done!")
            else:
                messagebox.showwarning("Invalid Index", "Invalid task index.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please provide a valid task index.")
    def save_to_file(self):
        filename = self.entry_filename.get()
        if not filename:
            filename = "todo_list.txt"
        with open(filename, "w") as file:
            for item in self.todo_list:
                file.write(f"{item['done']},{item['task']}\n")
        messagebox.showinfo("To-Do List Saved", "To-Do list saved successfully!")
if __name__ == "__main__":
    app = ToDoListApp()
    app.mainloop()
    
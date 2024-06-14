import tkinter as tk

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        master.title("Lista de Tarefas")

        self.label_task = tk.Label(master, text="Tarefa:")
        self.label_task.grid(row=0, column=0)

        self.entry_task = tk.Entry(master)
        self.entry_task.grid(row=0, column=1)

        self.add_button = tk.Button(master, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.grid(row=0, column=2)

        self.tasks_listbox = tk.Listbox(master)
        self.tasks_listbox.grid(row=1, column=0, columnspan=3)

        self.remove_button = tk.Button(master, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, columnspan=3)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks_listbox.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)

    def remove_task(self):
        try:
            selected_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_index)
        except IndexError:
            pass

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

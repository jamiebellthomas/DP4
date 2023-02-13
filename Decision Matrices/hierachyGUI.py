import tkinter as tk

class HierarchyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Hierarchy")

        self.classes = []
        self.current_class = None

        self.class_entry = tk.Entry(master)
        self.class_entry.pack()

        self.add_class_button = tk.Button(
            master,
            text="Add Class",
            command=self.add_class
        )
        self.add_class_button.pack()

        self.inherit_class_button = tk.Button(
            master,
            text="Inherit Class",
            command=self.inherit_class
        )
        self.inherit_class_button.pack()

    def add_class(self):
        class_name = self.class_entry.get()
        new_class = type(class_name, (object,), {})
        self.classes.append(new_class)
        self.current_class = new_class
        print(f"Added class: {class_name}")

    def inherit_class(self):
        class_name = self.class_entry.get()
        parent_class = next((c for c in self.classes if c.__name__ == class_name), None)
        if parent_class:
            new_class = type(
                self.current_class.__name__,
                (self.current_class, parent_class),
                {}
            )
            self.classes.remove(self.current_class)
            self.classes.append(new_class)
            self.current_class = new_class
            print(f"Class {self.current_class.__name__} now inherits from {class_name}")
        else:
            print(f"Class {class_name} not found.")

root = tk.Tk()
app = HierarchyGUI(root)
root.mainloop()

print (app.current_class.__name__)
print("Task - 4")
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

contacts = {}

def add_contact(name, phone, email, address):
    if name in contacts:
        return "Contact already exists."
    contacts[name] = {"phone": phone, "email": email, "address": address}
    return "Contact added successfully."

def view_contacts():
    return contacts

def search_contact(search_term):
    result = {name: info for name, info in contacts.items() if search_term.lower() in name.lower() or search_term in info['phone']}
    return result

def update_contact(name, phone=None, email=None, address=None):
    if name not in contacts:
        return "Contact not found."
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address
    return "Contact updated successfully."

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        return "Contact deleted successfully."
    else:
        return "Contact not found."
    
class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        
        self.create_widgets()
        
    def create_widgets(self):
        tk.Button(self.root, text="Add Contact", command=self.add_contact).pack(pady=5)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).pack(pady=5)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).pack(pady=5)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).pack(pady=5)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).pack(pady=5)
        
        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.pack(pady=10)
        
    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if not name:
            return
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email address:")
        address = simpledialog.askstring("Input", "Enter address:")
        
        result = add_contact(name, phone, email, address)
        messagebox.showinfo("Result", result)
        
    def view_contacts(self):
        contacts_list = view_contacts()
        result = "\n".join([f"{name}: {info['phone']}" for name, info in contacts_list.items()])
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result if result else "No contacts found.")
        
    def search_contact(self):
        search_term = simpledialog.askstring("Input", "Enter name or phone number to search:")
        if not search_term:
            return
        results = search_contact(search_term)
        result = "\n".join([f"{name}: {info['phone']}, {info['email']}, {info['address']}" for name, info in results.items()])
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result if result else "No contacts found.")
        
    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name to update:")
        if not name or name not in contacts:
            messagebox.showerror("Error", "Contact not found.")
            return
        phone = simpledialog.askstring("Input", "Enter new phone number (leave blank to keep current):")
        email = simpledialog.askstring("Input", "Enter new email address (leave blank to keep current):")
        address = simpledialog.askstring("Input", "Enter new address (leave blank to keep current):")
        
        result = update_contact(name, phone if phone else None, email if email else None, address if address else None)
        messagebox.showinfo("Result", result)
        
    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name to delete:")
        if not name:
            return
        result = delete_contact(name)
        messagebox.showinfo("Result", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()

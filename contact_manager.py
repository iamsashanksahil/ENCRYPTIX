import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector
import re 

# DATABASE CONFIG
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "port": 3306
}

# DATABASE CONNECTION
def create_database():

    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            port=DB_CONFIG["port"]
        )

        cursor = connection.cursor()

        cursor.execute("""
        CREATE DATABASE IF NOT EXISTS contact_manager
        """)

        connection.commit()
        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        messagebox.showerror(
            "Database Error",
            f"Error creating database:\n{err}"
        )

def get_connection():

    return mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database="contact_manager",
        port=DB_CONFIG["port"]
    )

def create_table():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(15) UNIQUE NOT NULL,
        email VARCHAR(100),
        address TEXT
    )
    """)

    connection.commit()
    cursor.close()
    connection.close()

# CONTACT MANAGER APP

class ContactManager:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Contact Manager"
        )

        self.root.geometry(
            "950x600"
        )

        self.root.configure(
            bg="#f4f6f9"
        )

        self.selected_contact_id = None

        title = tk.Label(
            root,
            text="Contact Management System",
            font=("Segoe UI", 20, "bold"),
            bg="#f4f6f9",
            fg="#1f2937"
        )

        title.pack(pady=10)

        self.create_form()
        self.create_buttons()
        self.create_table()

        self.load_contacts()

    def create_form(self):

        form_frame = tk.Frame(
            self.root,
            bg="#f4f6f9"
        )

        form_frame.pack(
            pady=10,
            padx=20,
            fill="x"
        )

        tk.Label(
            form_frame,
            text="Name",
            font=("Segoe UI", 10),
            bg="#f4f6f9"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )

        self.name_entry = tk.Entry(
            form_frame,
            width=30,
            font=("Segoe UI", 10)
        )

        self.name_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=5
        )

        tk.Label(
            form_frame,
            text="Phone",
            font=("Segoe UI", 10),
            bg="#f4f6f9"
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=5,
            sticky="w"
        )

        self.phone_entry = tk.Entry(
            form_frame,
            width=30,
            font=("Segoe UI", 10)
        )

        self.phone_entry.grid(
            row=0,
            column=3,
            padx=10,
            pady=5
        )

        tk.Label(
            form_frame,
            text="Email",
            font=("Segoe UI", 10),
            bg="#f4f6f9"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )

        self.email_entry = tk.Entry(
            form_frame,
            width=30,
            font=("Segoe UI", 10)
        )

        self.email_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=5
        )

        tk.Label(
            form_frame,
            text="Address",
            font=("Segoe UI", 10),
            bg="#f4f6f9"
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=5,
            sticky="w"
        )

        self.address_entry = tk.Entry(
            form_frame,
            width=30,
            font=("Segoe UI", 10)
        )

        self.address_entry.grid(
            row=1,
            column=3,
            padx=10,
            pady=5
        )

        tk.Label(
            form_frame,
            text="Search",
            font=("Segoe UI", 10),
            bg="#f4f6f9"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.search_entry = tk.Entry(
            form_frame,
            width=30,
            font=("Segoe UI", 10)
        )

        self.search_entry.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

    def create_buttons(self):

        button_frame = tk.Frame(
            self.root,
            bg="#f4f6f9"
        )

        button_frame.pack(
            pady=10
        )

        tk.Button(
            button_frame,
            text="Add Contact",
            command=self.add_contact,
            bg="#10b981",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=15
        ).grid(
            row=0,
            column=0,
            padx=10
        )

        tk.Button(
            button_frame,
            text="Update Contact",
            command=self.update_contact,
            bg="#3b82f6",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=15
        ).grid(
            row=0,
            column=1,
            padx=10
        )

        tk.Button(
            button_frame,
            text="Delete Contact",
            command=self.delete_contact,
            bg="#ef4444",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=15
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        tk.Button(
            button_frame,
            text="Search",
            command=self.search_contact,
            bg="#8b5cf6",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=15
        ).grid(
            row=0,
            column=3,
            padx=10
        )

        tk.Button(
            button_frame,
            text="Refresh",
            command=self.load_contacts,
            bg="#6b7280",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=15
        ).grid(
            row=0,
            column=4,
            padx=10
        )

    def create_table(self):

        table_frame = tk.Frame(
            self.root
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        columns = (
            "ID",
            "Name",
            "Phone",
            "Email",
            "Address"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for col in columns:
            self.tree.heading(
                col,
                text=col
            )

        self.tree.column(
            "ID",
            width=50
        )

        self.tree.pack(
            fill="both",
            expand=True
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_contact
        )

    def validate_inputs(
        self,
        name,
        phone,
        email
    ):

        if not name or not phone:
            messagebox.showerror(
                "Error",
                "Name and phone are required."
            )
            return False

        if not phone.isdigit():
            messagebox.showerror(
                "Error",
                "Phone must contain only digits."
            )
            return False

        if email and not re.match(
            r"[^@]+@[^@]+\.[^@]+",
            email
        ):
            messagebox.showerror(
                "Error",
                "Invalid email format."
            )
            return False

        return True

    def add_contact(self):

        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not self.validate_inputs(
            name,
            phone,
            email
        ):
            return

        try:

            connection = get_connection()
            cursor = connection.cursor()

            query = """
            INSERT INTO contacts
            (name, phone, email, address)
            VALUES (%s, %s, %s, %s)
            """

            cursor.execute(
                query,
                (
                    name,
                    phone,
                    email,
                    address
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Success",
                "Contact added successfully."
            )

            self.clear_fields()
            self.load_contacts()

        except mysql.connector.IntegrityError:
            messagebox.showerror(
                "Error",
                "Phone number already exists."
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def update_contact(self):

        if not self.selected_contact_id:
            messagebox.showwarning(
                "Warning",
                "Select a contact first."
            )
            return

        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not self.validate_inputs(
            name,
            phone,
            email
        ):
            return

        try:

            connection = get_connection()
            cursor = connection.cursor()

            query = """
            UPDATE contacts
            SET name=%s,
                phone=%s,
                email=%s,
                address=%s
            WHERE id=%s
            """

            cursor.execute(
                query,
                (
                    name,
                    phone,
                    email,
                    address,
                    self.selected_contact_id
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Success",
                "Contact updated successfully."
            )

            self.clear_fields()
            self.load_contacts()

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )


    def delete_contact(self):

        if not self.selected_contact_id:
            messagebox.showwarning(
                "Warning",
                "Select a contact first."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this contact?"
        )

        if not confirm:
            return

        try:

            connection = get_connection()
            cursor = connection.cursor()

            query = """
            DELETE FROM contacts
            WHERE id=%s
            """

            cursor.execute(
                query,
                (
                    self.selected_contact_id,
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Success",
                "Contact deleted successfully."
            )

            self.clear_fields()
            self.load_contacts()

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )


    def search_contact(self):

        search_term = self.search_entry.get().strip()

        try:

            connection = get_connection()
            cursor = connection.cursor()

            query = """
            SELECT *
            FROM contacts
            WHERE name LIKE %s
            OR phone LIKE %s
            """

            search_value = f"%{search_term}%"

            cursor.execute(
                query,
                (
                    search_value,
                    search_value
                )
            )

            records = cursor.fetchall()

            self.tree.delete(
                *self.tree.get_children()
            )

            for row in records:
                self.tree.insert(
                    "",
                    "end",
                    values=row
                )

            cursor.close()
            connection.close()

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )


    def load_contacts(self):

        try:

            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "SELECT * FROM contacts"
            )

            records = cursor.fetchall()

            self.tree.delete(
                *self.tree.get_children()
            )

            for row in records:
                self.tree.insert(
                    "",
                    "end",
                    values=row
                )

            cursor.close()
            connection.close()

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def select_contact(
        self,
        event
    ):

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(
            selected,
            "values"
        )

        self.selected_contact_id = values[0]

        self.name_entry.delete(
            0,
            tk.END
        )

        self.name_entry.insert(
            0,
            values[1]
        )

        self.phone_entry.delete(
            0,
            tk.END
        )

        self.phone_entry.insert(
            0,
            values[2]
        )

        self.email_entry.delete(
            0,
            tk.END
        )

        self.email_entry.insert(
            0,
            values[3]
        )

        self.address_entry.delete(
            0,
            tk.END
        )

        self.address_entry.insert(
            0,
            values[4]
        )

    def clear_fields(self):

        self.selected_contact_id = None

        self.name_entry.delete(
            0,
            tk.END
        )

        self.phone_entry.delete(
            0,
            tk.END
        )

        self.email_entry.delete(
            0,
            tk.END
        )

        self.address_entry.delete(
            0,
            tk.END
        )

        self.search_entry.delete(
            0,
            tk.END
        )

# APP START
if __name__ == "__main__":

    login_root = tk.Tk()
    login_root.withdraw()

    db_password = simpledialog.askstring(
        "MySQL Login",
        "Enter MySQL Password:",
        show="*"
    )

    if not db_password:
        messagebox.showerror(
            "Error",
            "Password is required."
        )
        exit()

    DB_CONFIG["password"] = db_password

    try:
        create_database()
        create_table()

    except Exception as e:
        messagebox.showerror(
            "Database Connection Error",
            f"Could not connect to MySQL:\n{e}"
        )
        exit()

    login_root.destroy()

    root = tk.Tk()

    app = ContactManager(root)

    root.mainloop()

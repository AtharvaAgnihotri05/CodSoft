import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("600x400")
        self.contacts = []
        icon_path = "phone.jpg"
        self.root.iconbitmap(icon_path)
        # Create and set up widgets
        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)

        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)

        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Grid layout
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button.grid(row=4, column=1, columnspan=2, pady=5)
        self.view_button.grid(row=4, column=2, columnspan=2, pady=5)
        self.search_button.grid(row=4, column=4, columnspan=2, pady=5)
        self.update_button.grid(row=4, column=6, columnspan=2, pady=5)
        self.delete_button.grid(row=4, column=8, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone are required!")

    def view_contacts(self):
        if self.contacts:
            view_window = tk.Toplevel(self.root)
            view_window.title("Contact List")

            for i, contact in enumerate(self.contacts, start=1):
                contact_info = f"{i}. {contact['Name']} - {contact['Phone']}"
                tk.Label(view_window, text=contact_info).pack(pady=5)
        else:
            messagebox.showinfo("Info", "No contacts available!")

    def search_contact(self):
        search_name = simpledialog.askstring("Search Contact", "Enter name to search:")
        if search_name:
            for contact in self.contacts:
                if contact["Name"].lower() == search_name.lower():
                    messagebox.showinfo("Contact Found", f"Name: {contact['Name']}\nPhone: {contact['Phone']}")
                    return
            messagebox.showinfo("Contact Not Found", f"No contact found with the name '{search_name}'.")

    def update_contact(self):
        search_name = simpledialog.askstring("Update Contact", "Enter name to update:")
        if search_name:
            for i, contact in enumerate(self.contacts):
                if contact["Name"].lower() == search_name.lower():
                    updated_name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact["Name"])
                    updated_phone = simpledialog.askstring("Update Contact", "Enter new phone:", initialvalue=contact["Phone"])
                    updated_email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact["Email"])
                    updated_address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contact["Address"])

                    if updated_name and updated_phone:
                        self.contacts[i] = {"Name": updated_name, "Phone": updated_phone, "Email": updated_email, "Address": updated_address}
                        messagebox.showinfo("Success", "Contact updated successfully!")
                        return
                    else:
                        messagebox.showerror("Error", "Name and Phone are required!")
                        return

            messagebox.showinfo("Contact Not Found", f"No contact found with the name '{search_name}'.")

    def delete_contact(self):
        search_name = simpledialog.askstring("Delete Contact", "Enter name to delete:")
        if search_name:
            for i, contact in enumerate(self.contacts):
                if contact["Name"].lower() == search_name.lower():
                    del self.contacts[i]
                    messagebox.showinfo("Success", "Contact deleted successfully!")
                    return

            messagebox.showinfo("Contact Not Found", f"No contact found with the name '{search_name}'.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()

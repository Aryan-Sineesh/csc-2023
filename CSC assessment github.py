import tkinter as tk
from tkinter import messagebox
import csv

def create_receipt():
    enter_name = name_entry.get()
    receipt_number = receipt_entry.get()
    item_hired = item_entry.get()
    number_hired = number_entry.get()

    if enter_name and receipt_number and item_hired and number_hired:
        with open('receipts.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([enter_name, receipt_number, item_hired, number_hired ])
        messagebox.showinfo("Success","Receipt created successfully.")
        clear_entries()
    else:
     messagebox.showwarning("Error","Please fill in the fields.")

def display_receipts():
    receipt_list.delete(0, tk.END)
    with open('receipts.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            receipt_list.insert(tk.END, f"Enter Name: {row[1]}, Receipt Number: {row[2]}, Item Hired: {row[3]}, Number of Items Hired: {row[4]}")

def delete_receipt():
    selected_receipt = receipt_list.get(tk.ACTIVE)
    if selected_receipt:
        receipt_number = selected_receipt.split("Receipt Number: ")[1].split(",")[0]
        rows = []
        with open('receipts.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] != receipt_number:
                    rows.append(row)

        with open('receipts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        messagebox.showinfo("Success", "Receipt deleted successfully.")
        display_receipts()
    else:
        messagebox.showwarning("Error","Please select a receipt.")

def clear_entries():
    name_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)

def print_row():
    selected_receipt = receipt_list.get(tk.ACTIVE)
    if selected_receipt:
        messagebox.showinfo("Selected Receipt", selected_receipt)
    else:
        messagebox.showwarning("Error", "Please select a receipt.")

def quit_application():
    result = messagebox.askyesno("Quit", "Are you sure you want to quit?")
    if result == tk.YES:
        window.destroy()

# Create the main window
window = tk.Tk()
window.title("Julie's Party Hire")

# Create and position the entry fields
name_label = tk.Label(window, text=" Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=5)

receipt_label = tk.Label(window, text="Receipt Number:")
receipt_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
receipt_entry = tk.Entry(window)
receipt_entry.grid(row=1, column=1, padx=10, pady=5)

item_label = tk.Label(window, text="Items Hired:")
item_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
item_entry = tk.Entry(window)
item_entry.grid(row=2, column=1, padx=10, pady=5)

number_label = tk.Label(window, text="Number of Items Hired")
number_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
number_entry = tk.Entry(window)
number_entry.grid(row=3, column=1, padx=10, pady=5)

# Create and position the buttons
create_button = tk.Button(window, text="Create Receipt", command=create_receipt)
create_button.grid(row=4, column=0, padx=10, pady=5)

display_button = tk.Button(window, text="Display Receipts",command=display_receipts)
display_button.grid(row=4, column=1, padx=10, pady=5)

delete_button = tk.Button(window, text="Delete Receipt", command=delete_receipt)
delete_button.grid(row=4, column=2, padx=10, pady=5)

print_button = tk.Button(window, text="Print Row", command=print_row)
print_button.grid(row=5, column=0, padx=10, pady=5)

quit_button = tk.Button(window, text="Quit", command=quit_application )
quit_button.grid(row=5, column=2, padx=10, pady=5)
            
# Create the receipt list 
receipt_list = tk.Listbox(window, width=60)
receipt_list.grid(row=6, columnspan=3, padx=10, pady=5)

# Start the GUI event loop
window.mainloop()


    
            



import tkinter as tk
from tkinter import ttk


def main_window():

    def cancel_cmd():
        root.destroy()

    def ok_cmd():
        print("Here is the data:")
        entered_name = name_entry.get()
        print("Name: {}".format(entered_name))
        entered_id = id_entry.get()
        print("ID: {}".format(entered_id))
        entered_blood_type = blood_letter.get()
        entered_rh_factor = rh_factor.get()
        print("Blood Type: {}".format(entered_blood_type+entered_rh_factor))
        entered_donor_center = donor_center.get()
        print("Nearest Donation Center: {}".format(entered_donor_center))

    root = tk.Tk()
    root.title("Health Database")
    root.geometry("700x400")

    ttk.Label(root, text="Blood Donor Database").grid(column=0, row=0,
                                                      columnspan=2,
                                                      sticky="w")
    ttk.Label(root, text="Name:").grid(column=0, row=1, sticky="e")
    name_entry = tk.StringVar()
    name_entry.set("Enter a name here")
    ttk.Entry(root, width=40, textvariable=name_entry)\
        .grid(column=1, row=1, sticky="w")

    ttk.Label(root, text="ID:").grid(column=0, row=2, sticky="e")
    id_entry = tk.StringVar()
    ttk.Entry(root, textvariable=id_entry).grid(column=1, row=2, sticky="w")

    blood_letter = tk.StringVar()
    ttk.Radiobutton(root, text="A", variable=blood_letter, value="A")\
        .grid(column=0, row=3, sticky="w")
    ttk.Radiobutton(root, text="B", variable=blood_letter, value="B")\
        .grid(column=0, row=4, sticky="w")
    ttk.Radiobutton(root, text="AB", variable=blood_letter, value="AB")\
        .grid(column=0, row=5, sticky="w")
    ttk.Radiobutton(root, text="O", variable=blood_letter, value="O")\
        .grid(column=0, row=6, sticky="w")

    rh_factor = tk.StringVar()
    rh_factor.set("+")
    ttk.Checkbutton(root, text="Rh positive", variable=rh_factor,
                    onvalue="+", offvalue="-").grid(column=1, row=4)

    ttk.Label(root, text="Nearest Donation Center").grid(column=2, row=0)
    donor_center = tk.StringVar()
    center_dropdown = ttk.Combobox(root, textvariable=donor_center)
    center_dropdown.grid(column=2, row=1)
    center_dropdown["values"] = ("Durham", "Raleigh", "Cary", "Apex")

    ttk.Button(root, text="OK", command=ok_cmd).grid(column=1, row=20)
    ttk.Button(root, text="Cancel", command=cancel_cmd).grid(column=2, row=20)

    root.mainloop()


if __name__ == '__main__':
    main_window()

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from PIL import Image, ImageTk


def verify_GUI_inputs(input_id):
    try:
        id_integer = int(input_id)
    except ValueError:
        return False
    return id_integer


def main_window():

    def cancel_cmd():
        root.destroy()

    def ok_cmd():
        from health_db_client import upload_patient_data_to_server
        # Get data from interface
        entered_name = name_entry.get()
        entered_id = id_entry.get()
        entered_blood_letter = blood_letter.get()
        entered_rh_factor = rh_factor.get()
        entered_blood_type = entered_blood_letter + entered_rh_factor
        entered_donor_center = donor_center.get()
        # Call other functions to do the work
        patient_number = verify_GUI_inputs(entered_id)
        if patient_number is False:
            status_label.configure(text="Patient ID must be an integer.")
            return
        status_string = upload_patient_data_to_server(entered_name,
                                                      patient_number,
                                                      entered_blood_type)
        # Update interface based on results
        status_label.configure(text=status_string)

    def image_cmd():
        filename = filedialog.askopenfilename()
        if filename == "":
            return
        pil_image_raw = Image.open(filename)
        pil_image = pil_image_raw.resize((200, 200))
        tk_image = ImageTk.PhotoImage(pil_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image

    # Create root/base window
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

    # Status Indicator
    status_label = ttk.Label(root, text="Status")
    status_label.grid(column=0, row=20)

    # Image
    pil_image_raw = Image.open("chapel.jpg")
    pil_image = pil_image_raw.resize((200, 200))
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label = ttk.Label(root, image=tk_image)
    image_label.image = tk_image
    image_label.grid(column=4, row=0, rowspan=10)

    # Buttons
    ttk.Button(root, text="OK", command=ok_cmd).grid(column=1, row=20)
    ttk.Button(root, text="Cancel", command=cancel_cmd).grid(column=2, row=20)
    ttk.Button(root, text="Change image", command=image_cmd).grid(column=3,
                                                                  row=20)

    # Start GUI
    root.after(2000, image_cmd)
    root.mainloop()


if __name__ == '__main__':
    main_window()

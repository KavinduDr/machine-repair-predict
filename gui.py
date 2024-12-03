from customtkinter import *
from PIL import Image

# Initialize the main app
app = CTk()
app.geometry("500x500")
set_appearance_mode("dark")

# Load the initial image
my_image = CTkImage(light_image=Image.open("./assests/ml.jpg"),
                    dark_image=Image.open("./assests/ml.jpg"),
                    size=(500, 500))

# Function to replace content in the main window
def click_handler():
    # Clear the existing content
    for widget in app.winfo_children():
        widget.destroy()


    label = CTkLabel(app, text="Enter values of the machine", font=("Arial", 20, "bold"))
    label.pack(pady=10)
    
    # Input fields
    input_frame = CTkFrame(app, width=250)  # 50% of 500px width
    input_frame.pack(pady=10, anchor="center")

    # UDI input
    udi_frame = CTkFrame(input_frame)
    udi_frame.pack(pady=5, anchor="w")

    udi_label = CTkLabel(udi_frame, text="UDI:", font=("Arial", 15, "bold"), width=170)
    udi_label.pack(side="left", padx=5)

    udi_entry = CTkEntry(udi_frame, width=150)
    udi_entry.pack(side="right", padx=5)

    # Type input
    type_frame = CTkFrame(input_frame)
    type_frame.pack(pady=5, anchor="w")

    type_label = CTkLabel(type_frame, text="Type:", font=("Arial", 15, "bold"), width=170)
    type_label.pack(side="left", padx=5)

    type_entry = CTkEntry(type_frame, width=150)
    type_entry.pack(side="left", padx=5)

    # Air temperature input
    air_temp_frame = CTkFrame(input_frame)
    air_temp_frame.pack(pady=5, anchor="w")

    air_temp_label = CTkLabel(air_temp_frame, text="Air Temperature:", font=("Arial", 15, "bold"), width=170)
    air_temp_label.pack(side="left", padx=5)

    air_temp_entry = CTkEntry(air_temp_frame, width=150)
    air_temp_entry.pack(side="left", padx=5)

    # Process temperature input
    proc_temp_frame = CTkFrame(input_frame)
    proc_temp_frame.pack(pady=5, anchor="w")

    proc_temp_label = CTkLabel(proc_temp_frame, text="Process Temperature:", font=("Arial", 15, "bold"), width=170)
    proc_temp_label.pack(side="left", padx=5)

    proc_temp_entry = CTkEntry(proc_temp_frame, width=150)
    proc_temp_entry.pack(side="left", padx=5)

    # Torque input
    torque_frame = CTkFrame(input_frame)
    torque_frame.pack(pady=5, anchor="w")

    torque_label = CTkLabel(torque_frame, text="Torque:", font=("Arial", 15, "bold"), width=170)
    torque_label.pack(side="left", padx=5)

    torque_entry = CTkEntry(torque_frame, width=150)
    torque_entry.pack(side="left", padx=5)

    # Tool wearing input
    tool_wear_frame = CTkFrame(input_frame)
    tool_wear_frame.pack(pady=5, anchor="w")

    tool_wear_label = CTkLabel(tool_wear_frame, text="Tool Wearing:", font=("Arial", 15, "bold"), width=170)
    tool_wear_label.pack(side="left", padx=5)

    tool_wear_entry = CTkEntry(tool_wear_frame, width=150)
    tool_wear_entry.pack(side="left", padx=5)
    
    # Predict Button
    predict_btn = CTkButton(master=app, text="Predict", corner_radius=32, fg_color="transparent",
                            hover_color="#4158D0", border_color="#4158D0", border_width=2,
                            font=("Arial", 20, "bold"), width=200, height=50, command=click_handler)
    predict_btn.pack(pady=20)

    back_btn = CTkButton(master=app, text="Back", corner_radius=32, fg_color="transparent",
                         hover_color="#4158D0", border_color="#4158D0", border_width=2,
                         font=("Arial", 20, "bold"), width=200, height=50, command=load_initial_content)
    back_btn.pack(pady=20)

# Function to load the initial content
def load_initial_content():
    # Clear the existing content
    for widget in app.winfo_children():
        widget.destroy()

    image_label = CTkLabel(app, image=my_image, text="")
    image_label.image = my_image  # Prevent garbage collection of the image
    image_label.place(relx=-0.3, rely=0.5, anchor="w")

    btn = CTkButton(master=app, text="Let's Predict", corner_radius=32, fg_color="transparent",
                    hover_color="#4158D0", border_color="#4158D0", border_width=2,
                    font=("Arial", 20, "bold"), width=200, height=50, command=click_handler)
    btn.place(relx=1, rely=0.5, anchor="e")

# Load the initial content
load_initial_content()

# Run the app
app.mainloop()

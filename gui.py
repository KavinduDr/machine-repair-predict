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


    label = CTkLabel(app, text="Prediction in Progress", font=("Arial", 20, "bold"))
    label.pack(pady=10)

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

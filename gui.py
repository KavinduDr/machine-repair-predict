from tkinter import PhotoImage, messagebox
from customtkinter import *
from PIL import Image
import numpy as np
import joblib

# Load the saved scaler and model
scaler = joblib.load('scaler.pkl')
model = joblib.load('svc_model.pkl')

scalar_forest = joblib.load('scaler_forest.pkl')
model_forest = joblib.load('svc_model_forest.pkl')

# Initialize the main app
app = CTk()
app.geometry("500x500")
set_appearance_mode("dark")
app.title("Machine Learning")

# Set the title bar icon  
icon_image = PhotoImage(file='./assests/brain.png')  # Use a PNG or another supported format  
app.iconphoto(False, icon_image)
app.icon_image = icon_image

# Load the initial image
my_image = CTkImage(light_image=Image.open("./assests/ml.jpg"),
                    dark_image=Image.open("./assests/ml.jpg"),
                    size=(500, 500))

# Predict functions
def predict(model, scaler):
    """Get user input, process it, and make predictions."""
    try:
        # Get values from input fields
        type_val = float(type_entry.get())
        air_temp_val = float(air_temp_entry.get())
        proc_temp_val = float(proc_temp_entry.get())
        torque_val = float(torque_entry.get())
        tool_wear_val = float(tool_wear_entry.get())

        # Create a feature array and scale it
        input_features = np.array([[type_val, air_temp_val, proc_temp_val, torque_val, tool_wear_val]])
        scaled_features = scaler.transform(input_features)

        # Make predictions
        prediction = model.predict(scaled_features)

        # Display the result
        result = "Prediction: Machine will fail" if prediction[0] == 1 else "Prediction: No Failure"
        CTkLabel(app, text=result, font=("Arial", 18, "bold")).pack(pady=10)

    except ValueError:
        CTkLabel(app, text="Invalid input! Please enter numeric values.", font=("Arial", 14, "bold"), fg_color="red").pack(pady=10)

# Function to replace content in the main window
def click_handler(model, scaler):
    # Clear the existing content
    for widget in app.winfo_children():
        widget.destroy()

    label = CTkLabel(app, text="Enter values of the machine", font=("Arial", 20, "bold"))
    label.pack(pady=10)
    
    # Input fields
    input_frame = CTkFrame(app, width=250)  # 50% of 500px width
    input_frame.pack(pady=10, anchor="center")

    global type_entry, air_temp_entry, proc_temp_entry, torque_entry, tool_wear_entry  # Make fields accessible in predict()

    # Create input fields dynamically
    fields = [
        ("Type:", "type_entry"),
        ("Air Temperature:", "air_temp_entry"),
        ("Process Temperature:", "proc_temp_entry"),
        ("Torque:", "torque_entry"),
        ("Tool Wearing:", "tool_wear_entry"),
    ]
    
    for label_text, var_name in fields:
        frame = CTkFrame(input_frame)
        frame.pack(pady=5, anchor="w")
        label = CTkLabel(frame, text=label_text, font=("Arial", 15, "bold"), width=170)
        label.pack(side="left", padx=5)
        entry = CTkEntry(frame, width=150)
        entry.pack(side="left", padx=5)
        globals()[var_name] = entry
    
    # Predict Button
    predict_btn = CTkButton(master=app, text="Predict", corner_radius=32, fg_color="transparent",
                            hover_color="#4158D0", border_color="#4158D0", border_width=2,
                            font=("Arial", 20, "bold"), width=200, height=50, 
                            command=lambda: predict(model, scaler))
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

    # Single Predict Button
    predict_btn = CTkButton(master=app, text="Let's Predict", corner_radius=32, fg_color="transparent",
                            hover_color="#4158D0", border_color="#4158D0", border_width=2,
                            font=("Arial", 20, "bold"), width=200, height=50, command=choose_model)
    predict_btn.place(relx=1, rely=0.5, anchor="e")

# Function to choose the model
def choose_model():
    response = messagebox.askquestion("Model Selection", "Which model would you like to use?\n\nYes: SVC Model\nNo: Forest Model")
    if response == 'yes':
        click_handler(model, scaler)
    elif response == 'no':
        click_handler(model_forest, scalar_forest)

# Load the initial content
load_initial_content()

# Run the app
app.mainloop()

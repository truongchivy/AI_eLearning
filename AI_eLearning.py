
#######################################################

import tkinter as tk
from tkinter import ttk, Text
from openai import OpenAI # Import the OpenAI package
import os

# Set your OpenAI API key
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("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"),
)

# Function to update the options in the second dropdown based on the first dropdown selection
def update_options(event):
    # Clear the current options in the second dropdown
    class_dropdown['values'] = []
    # Get the selected value from the first dropdown
    selected_level = level_var.get()

    # Update the options based on the selected level
    if selected_level == "Cấp 1":
        class_dropdown['values'] = ["Lớp 1", "Lớp 2", "Lớp 3", "Lớp 4", "Lớp 5"]
    elif selected_level == "Cấp 2":
        class_dropdown['values'] = ["Lớp 6", "Lớp 7", "Lớp 8", "Lớp 9", "Lớp 10"]
    elif selected_level == "Cấp 3":
        class_dropdown['values'] = ["Lớp 11", "Lớp 12", "Lớp 13"]

    # Reset the selected value of the second dropdown
    class_var.set('')

# Function to send a request to ChatGPT and get a response
def send_to_chatgpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Choose the appropriate model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,  # Adjust the response length as needed
    )
    return response['choices'][0]['message']['content'].strip()

# Function to handle the confirmation button click
def test_prompt():
    selected_level = level_var.get()
    selected_class = class_var.get()
    selected_language = language_var.get()
    selected_subject = subject_var.get()
    selected_quiz = quiz_var.get()
    text = f"Hãy tạo một bài giảng cho {selected_class} về môn {selected_subject} theo phong cách {selected_level}, bài giảng dùng tiếng {selected_language}, {selected_quiz} cần quiz"
    text_widget.insert(tk.END, text + '\n')

def confirm_selection():
    selected_level = level_var.get()
    selected_class = class_var.get()
    selected_language = language_var.get()
    selected_subject = subject_var.get()
    selected_quiz = quiz_var.get()

    # Create the prompt for ChatGPT
    prompt = f"Hãy tạo một bài giảng cho {selected_class} về môn {selected_subject} theo phong cách {selected_level}, bài giảng dùng tiếng {selected_language}, {selected_quiz} cần quiz"

    # Get the response from ChatGPT
    response = send_to_chatgpt(prompt)

    # Print the response in the UI
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, response)

# Create the main window
root = tk.Tk()
root.title("Educational Level Selection")

# Create a variable to store the selected level
level_var = tk.StringVar()

# Create the first dropdown (Educational Level)
level_label = ttk.Label(root, text="Chọn cấp học:")
level_label.pack(pady=10)
level_dropdown = ttk.Combobox(root, textvariable=level_var, values=["Cấp 1", "Cấp 2", "Cấp 3"])
level_dropdown.pack(pady=10)

# Create a variable to store the selected level
lang_var = tk.StringVar()

# Bind the dropdown selection to the update_options function
level_dropdown.bind("<<ComboboxSelected>>", update_options)

# Create a variable to store the selected class
class_var = tk.StringVar()

# Create the second dropdown (Class) with no initial values
class_label = ttk.Label(root, text="Chọn lớp:")
class_label.pack(pady=10)
class_dropdown = ttk.Combobox(root, textvariable=class_var)
class_dropdown.pack(pady=10)

# Create a variable to store the selected subject
subject_var = tk.StringVar()

# Create the subject dropdown
level_label = ttk.Label(root, text="Chọn môn học:")
level_label.pack(pady=10)
level_dropdown = ttk.Combobox(root, textvariable=subject_var, values=["Toán", "Anh Văn", "Ngữ Văn (Tiếng Việt)", "Đạo đức", "Lịch sử", "Địa lý", "Vật lý", "Sinh học" , "Hóa học"])
level_dropdown.pack(pady=10)

# Create a variable to store the selected language
language_var = tk.StringVar()

# Create the language dropdown
level_label = ttk.Label(root, text="Chọn ngôn ngữ:")
level_label.pack(pady=10)
level_dropdown = ttk.Combobox(root, textvariable=language_var, values=["Việt", "Anh", "Pháp"])
level_dropdown.pack(pady=10)

# Create a variable to store the quiz confirm
quiz_var = tk.StringVar()

# Create the quiz confirm dropdown
level_label = ttk.Label(root, text="Cần quiz:")
level_label.pack(pady=10)
level_dropdown = ttk.Combobox(root, textvariable=quiz_var, values=["Có", "Không"])
level_dropdown.pack(pady=10)

# Check Prompt
confirm_button = ttk.Button(root, text="Test Prompt", command=test_prompt)
confirm_button.pack(pady=20)

text_widget = tk.Text(root, wrap='word', height=10, width=40)
text_widget.pack(padx=10, pady=10)

# Create a confirmation button
confirm_button = ttk.Button(root, text="Confirm", command=confirm_selection)
confirm_button.pack(pady=20)

# Create a text box to display the ChatGPT response
output_text = Text(root, wrap=tk.WORD, height=10, width=50)
output_text.pack(pady=10)

# Start the main loop
root.mainloop()

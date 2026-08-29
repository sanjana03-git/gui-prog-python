import tkinter

window = tkinter.Tk()
window.title("Hello World")
window.geometry("400x300")
window.configure(bg="lightblue")

my_label = tkinter.Label(window, text="Welcome to Tkinter!", font=("Arial", 16), bg="lightblue")
my_label.pack()

my_label["text"] = "Hello again!"
my_label.config(text="Hello again!")

#Button
# def on_button_click():
#     print("Button clicked!")

# my_button = tkinter.Button(window, text="Click Me", command=on_button_click)
# my_button.pack(pady=10)


#Entry
# def on_entry_submit():
#     user_input = my_entry.get()
#     print("You entered:", user_input)

# my_entry = tkinter.Entry(window)
# my_entry.pack(pady=10)
# submit_button = tkinter.Button(window, text="Submit", command=on_entry_submit)
# submit_button.pack(pady=5)


def on_entry_submit():
    user_input = my_entry.get()
    my_label.config(text=user_input)

my_entry = tkinter.Entry(window)
my_entry.pack(pady=10)

submit_button = tkinter.Button(window, text="Submit", command=on_entry_submit)
submit_button.pack(pady=5)



window.mainloop()
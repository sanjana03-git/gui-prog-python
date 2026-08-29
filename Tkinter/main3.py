import tkinter

window = tkinter.Tk()
window.title("HELLO WORLD")
window.minsize(width=500, height=300)
label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# label.pack()
# label.place(x=100, y=100)
label.grid(column=0, row=0)

#Button
def action():
    user_input = entry.get()
    label.config(text=user_input)   
button = tkinter.Button(text="Click Me", command=action)
button.grid(column=1, row=0)

#Entry
entry = tkinter.Entry(width=30) 
entry.grid(column=2, row=0)





window.mainloop()
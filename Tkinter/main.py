import tkinter

window = tkinter.Tk()
window.title("Hello World")
window.geometry("400x300")
window.configure(bg="lightblue")

my_label = tkinter.Label(window, text="Welcome to Tkinter!", font=("Arial", 16), bg="lightblue")
# my_label.pack(pady=20)
# my_label.grid(row=0, column=0, padx=20, pady=20)
# my_label.place(x=100, y=50)
# my_label.pack(side="left")
# my_label.pack(side="top", pady=20)
# my_label.pack(expand=True)
my_label.pack()

def fun(a, b=2, c=3):
    print(a, b, c)

fun(1)
fun(1, 4)
fun(1, 4, 5)
fun(1, c=5)

def unlimited_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

unlimited_args(1, 2, 3, name="Alice", age=30)

def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(1, 2)
bar(toast='nah', spam=4, eggs=2)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.year = kwargs.get('year')

car1 = Car(make='Toyota', model='Corolla', year=2020)
print(car1.make, car1.model, car1.year)



window.mainloop()
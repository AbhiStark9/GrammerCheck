from tkinter import *
import language_tool_python


def main_func():
    input_data = input_1.get()
    tool = language_tool_python.LanguageTool('en-US')
    correction = tool.correct(input_data)
    output_1.delete(0, END)
    output_1.insert(0, correction)

def mainw():

    global input_1, output_1
    window = Tk()
    window.geometry('500x400')
    window.resizable(False, False)
    window.configure(bg='blue')
    window.title("Grammar Check")

    label_1 = Label(window, text="Enter text", font=("Times New Roman", 30, 'bold'), bg="aqua", fg='black')
    label_1.place(x=100, y=25, height=50, width=300)
    input_1 = Entry(window, font=("Times New Roman", 15))
    input_1.place(x=50, y=100, height=50, width=400)

    label_2 = Label(window, text="Corrections", font=("Times New Roman", 30, 'bold'), bg="aqua", fg='black')
    label_2.place(x=100, y=180, height=50, width=300)
    output_1 = Entry(window, font=("Times New Roman", 15))
    output_1.place(x=50, y=255, height=50, width=400)

    button = Button(window, text='Enter', font=("Times New Roman", 20, 'bold'), bg="black", fg='white', command=main_func)
    button.place(x=200, y=330, height=50, width=100)

    window.mainloop()

mainw()

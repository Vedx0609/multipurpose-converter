import customtkinter
from PIL import Image, ImageTk
from PIL import Image as pim

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk() #Main window
app.geometry("400x780")
app.title("Converter")

a = customtkinter.CTkImage(Image.open("fire.jpg"), size=(120, 100))
b = customtkinter.CTkImage(Image.open("bmi.jpg"), size=(120, 100))
c = customtkinter.CTkImage(Image.open("images2.png"), size=(130, 110))

frame_1 = customtkinter.CTkFrame(master=app) #Frame for main window
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

import tkinter as tk
from tkinter import *
from tkinter import messagebox
geometry_parameter="980x700"

def button_bmi():
    root = tk.Toplevel()  # This creates a window.

    root.title("GUI : BMI calculator")  # Gives the title of the project
    icon = pim.open("bmii.jpg")
    icon.resize((10, 10))
    icon = ImageTk.PhotoImage(icon)
    Tops = Frame(root, bg='cyan', pady=2, width=1850, height=100,relief="ridge")  # It is going to be the top display of the window
    Tops.grid(row=0, column=0)

    headlabel = tk.Label(Tops, image=icon, compound=LEFT, font=('lato black', 19, 'bold'),text=' BMI CALCULATOR ', bg='cyan', fg='white')
    headlabel.grid(row=1, column=0, sticky=W)  # It is going to added in as the headlalbel of the project.

    variable1 = tk.StringVar(root)  # Further going to be used for getting the age
    variable2 = tk.StringVar(root)  # This is for the height
    variable3 = tk.StringVar(root)  # weight

    variable1.set("age")
    variable2.set("currency")
    variable3.set("weight")

    age_tf = variable1.get()
    height_tf = variable2.get()
    weight_tf = variable3.get()

    def reset_entry():
        age_tf.delete(0, 'end')
        height_tf.delete(0, 'end')
        weight_tf.delete(0, 'end')

    def calculate_bmi():
        kg = float(weight_tf.get())
        m = float(height_tf.get())
        bmi = kg / (m * m)
        bmi = float("{:.2f}".format(bmi))
        bmi_index(bmi)

    def bmi_index(bmi):

        if bmi < 18.5:
            messagebox.showinfo('BMI', f'BMI = {bmi} is Underweight')
        elif (bmi > 18.5) and (bmi < 24.9):
            messagebox.showinfo('BMI', f'BMI = {bmi} is Normal')
        elif (bmi > 24.9) and (bmi < 29.9):
            messagebox.showinfo('BMI', f'BMI = {bmi} is Overweight')
        elif (bmi > 29.9):
            messagebox.showinfo('BMI', f'BMI = {bmi} is Obesity')
        else:
            messagebox.showerror('BMI', 'something went wrong!')

    root.configure(background='#e5e6e5')
    root.geometry(geometry_parameter)

    Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_1.grid(row=1, column=0, sticky=W)


    label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Age :  ", bg="#e6e5e5", fg="black")
    label1.grid(row=2, column=0, sticky=W)

    label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Height (m) :  ", bg="#e6e5e5", fg="black")
    label1.grid(row=3, column=0, sticky=W)

    label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Weight (kg) :  ", bg="#e6e5e5", fg="black")
    label1.grid(row=4, column=0, sticky=W)

    Label_1 = Label(root, font=('lato black', 15, 'bold'), text="\t    Gender :  ", bg="#e6e5e5", fg="black")
    Label_1.grid(row=5, column=0, sticky=W)

    Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_1.grid(row=7, column=0, sticky=W)

    var = IntVar()
    age_tf = tk.Entry(root)
    age_tf.grid(row=2, column=0, ipadx=28, sticky=E)
    height_tf = tk.Entry(root)
    height_tf.grid(row=3, column=0, ipadx=28, sticky=E)
    weight_tf = tk.Entry(root)
    weight_tf.grid(row=4, column=0, ipadx=28, sticky=E)
    male_rb = Radiobutton(root, text='Male', variable=var, value=1)
    male_rb.grid(row=5, column=0, ipadx=4, sticky=E)
    female_rb = Radiobutton(root, text='Female', variable=var, value=2)
    female_rb.grid(row=6, column=0, sticky=E)

    Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Calculate ", padx=2, pady=2, bg="black", fg="white",command=calculate_bmi)
    Label_9.grid(row=8, column=0)

    Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_1.grid(row=11, column=0, sticky=W)

    Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="white", fg="red",command=reset_entry)
    Label_9.grid(row=12, column=0)

    root.mainloop()



def button_curr():
    root = tk.Toplevel()  # This creates a window.
    root.title("GUI : Currency Conversion")  # Gives the title of the project

    Tops = Frame(root, bg='cyan', pady=2, width=1850, height=100,relief="ridge")  # It is going to be the top display of the window
    Tops.grid(row=0, column=0)

    icon = pim.open("Currency convertor image.jpeg")
    icon.resize((10,10))
    img = ImageTk.PhotoImage(icon)


    headlabel = tk.Label(Tops, image=img, compound=LEFT, font=('lato black', 19, 'bold'),text=' Currency Converter  ', bg='cyan', fg='white',width=930,anchor="w")
    #headlabel.image = img
    headlabel.grid(row=1, column=0, sticky=W)  # It is going to added in as the headlalbel of the project.

    variable1 = tk.StringVar(root)  # Further going to be used for getting the input currency
    variable2 = tk.StringVar(root)  # This is for the output currency

    variable1.set("currency")
    variable2.set("currency")
    Amount2_field = tk.Entry(root)
    Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

    def RealTimeCurrencyConversion():
        from forex_python.converter import CurrencyRates  # This is going to give help us in converting the currencies according to the chosen currencies.
        c = CurrencyRates()

        from_currency = variable1.get()
        to_currency = variable2.get()

        if (Amount1_field.get() == ""):
            tk.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please enter a valid amount user.")

        elif (from_currency == "currency" or to_currency == "currency"):
            tk.messagebox.showinfo("Error !!","Currency Not Selected.\n Please select FROM and TO Currency from menu.")
        elif (from_currency == to_currency):
            tk.messagebox.showinfo('Error!!','FROM currency and TO Currency are same.\n Please select a different currency for converting the currency.')

        else:
            new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
            new_amount = float("{:.4f}".format(new_amt))
            Amount2_field.insert(0, str(new_amount) + " " + to_currency)

    def clear_all():
        Amount1_field.delete(0, tk.END)

        Amount2_field.delete(0, tk.END)

    CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR", "AUD", "JPY", "GBP", "RUB", "NZD"]

    root.configure(background='#e5e6e5')
    root.geometry(geometry_parameter)

    Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_1.grid(row=1, column=0, sticky=W)

    label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Amount  :  ", bg="#e6e5e5", fg="black")
    label1.grid(row=2, column=0, sticky=W)

    label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    From Currency  :  ", bg="#e6e5e5", fg="black")
    label1.grid(row=3, column=0, sticky=W)

    label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    To Currency  :  ", bg="#e6e5e5", fg="black")
    label1.grid(row=4, column=0, sticky=W)

    label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Converted Amount  :  ", bg="#e6e5e5",fg="black")
    label1.grid(row=8, column=0, sticky=W)

    Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_1.grid(row=5, column=0, sticky=W)

    Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_1.grid(row=7, column=0, sticky=W)

    FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
    ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)

    FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
    ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)

    Amount1_field = tk.Entry(root)
    Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)

    Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="black", fg="white",command=RealTimeCurrencyConversion)
    Label_9.grid(row=6, column=0)

    Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_1.grid(row=9, column=0, sticky=W)

    Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="white", fg="red",command=clear_all)
    Label_9.grid(row=10, column=0)

    root.mainloop()


def button_temp():
    root = tk.Toplevel()  # Creates a window.
    root.title("GUI : Temperature Converter")  # Adds title to the window

    icon = pim.open("temperature-scales.jpg")
    icon.resize((10, 10))
    img = ImageTk.PhotoImage(icon)  # Adds image to the window

    Tops = Frame(root, bg='cyan', pady=2, width=1850, height=100,relief='ridge')  # Used to create a frame (ridge is used to make the style as ridge)
    Tops.grid(row=0, column=0)

    headlabel = tk.Label(Tops, image=img, compound=LEFT, font=('lato black', 19, 'bold'),text=' Temperature Converter ', bg='cyan', fg='black',width=930,anchor="w")
    headlabel.grid(row=1, column=0, sticky=W)  # It is going to added in as the headlalbel of the Temperature GUI

    variable1 = tk.StringVar(root)  # Further going to be used for getting the input temperature unit
    variable2 = tk.StringVar(root)  # This is for the output temperature unit

    variable1.set("Unit")
    variable2.set("Unit")

    def TemperatureConversion():
        initial_unit = variable1.get()
        final_unit = variable2.get()
        if (Temp1_field.get() == ""):
            tk.messagebox.showinfo("Error !!","Temperature Not Entered.\n Please enter a valid temperature.")  # To show an error in a new window
        elif (initial_unit == "Unit" or final_unit == "Unit"):
            tk.messagebox.showinfo("Error !!","Unit Not Selected.\nPlease select Initial Unit and Final Unit from menu.")
        elif (initial_unit == final_unit):
            tk.messagebox.showinfo("Error !!", "Same Unit Selected.\nPlease select different Units from menu.")
        else:
            result = 0
            if initial_unit == "°C":
                result = (float(Temp1_field.get()) * 1.8 + 32) if final_unit == "°F" else (float(Temp1_field.get()) + 273.15)
            elif initial_unit == "°F":
                result = ((float(Temp1_field.get()) - 32) * (5 / 9)) if final_unit == "°C" else (((float(Temp1_field.get()) - 32) * (5 / 9)) + 273.15)
            elif initial_unit == " K":
                result = (((float(Temp1_field.get()) - 273.15) * 1.8) + 32) if final_unit == "°F" else (float(Temp1_field.get()) - 273.15)

            res = float("{:.2f}".format(result))
            Temp2_field.insert(0, str(res) + " " + final_unit)

    def clear_all():
        Temp1_field.delete(0, tk.END)  # Used to clear the input
        Temp2_field.delete(0, tk.END)  # Used to clear the output

    Temperature_code = ["°C", "°F", " K"]  # To contain the units

    root.configure(background='#e5e6e5')  # Create white background
    root.geometry(geometry_parameter)

    Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_1.grid(row=1, column=0, sticky=W)  # Used for formatting (empty line)

    label2 = tk.Label(root, font=('lato black', 15, 'bold'), text="\tTemperature : ", bg="#e6e5e5", fg="black")
    label2.grid(row=2, column=0, sticky=W)
    Temp1_field = tk.Entry(root)
    Temp1_field.grid(row=2, column=0, ipadx=28, sticky=E)  # To take input temperature

    label3 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Initial Unit : ", bg="#e6e5e5", fg="black")
    label3.grid(row=3, column=0, sticky=W)
    FromTemperature_option = tk.OptionMenu(root, variable1, *Temperature_code)
    FromTemperature_option.grid(row=3, column=0, ipadx=45, sticky=E)  # To take initial unit

    label4 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Final Unit : ", bg="#e6e5e5", fg="black")
    label4.grid(row=4, column=0, sticky=W)
    ToTemperature_option = tk.OptionMenu(root, variable2, *Temperature_code)
    ToTemperature_option.grid(row=4, column=0, ipadx=45, sticky=E)  # To take desired unit

    Label_5 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_5.grid(row=5, column=0, sticky=W)  # Formatting

    Label_6 = Button(root, font=('arial', 15, 'bold'), text=" Convert ", padx=2, pady=2, bg="black", fg="white",command=TemperatureConversion)
    Label_6.grid(row=6, column=0)  # To get the converted temperature

    Label_7 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_7.grid(row=7, column=0, sticky=W)  # Formatting

    label8 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Converted Temperature : ", bg="#e6e5e5",fg="black")
    label8.grid(row=8, column=0, sticky=W)
    Temp2_field = tk.Entry(root)
    Temp2_field.grid(row=8, column=0, ipadx=31, sticky=E)  # Used to display converted temperature

    Label_9 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_9.grid(row=9, column=0, sticky=W)  # Formatting

    Label_10 = Button(root, font=('arial', 15, 'bold'), text=" Clear All ", padx=2, pady=2, bg="white", fg="red",command=clear_all)
    Label_10.grid(row=10, column=0)  # To clear all and take new input

    root.mainloop()  # To run the GUI


button_1 = customtkinter.CTkButton(master=frame_1, text="temperature\nconversion", text_color="black",command=button_temp, width=125, height=100, image=a, fg_color="white")
button_1.pack(pady=30, padx=10)

button_2 = customtkinter.CTkButton(master=frame_1, text="bmi calculator", text_color="black", command=button_bmi,width=120, height=120, image=b, fg_color="white")
button_2.pack(pady=30, padx=10)

button_3 = customtkinter.CTkButton(master=frame_1, text="currency conversion", text_color="black", command=button_curr,width=95, height=100, image=c, fg_color="white")
button_3.pack(pady=30, padx=10)

app.mainloop()
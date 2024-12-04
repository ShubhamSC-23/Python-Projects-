from tkinter import * 


FONT = ("Arial", 24)  


def miles_to_km():
    input_miles = float(entry_miles.get())
    km_str = str(input_miles*1.689)
    label_km.config(text=km_str)


window = Tk()
window.title("Mile to km converter ")  
window.minsize(width=500, height=300)  
window.config(padx=100, pady=100)  

label_1 = Label(text="miles", font=FONT)
label_1.grid(column=2, row=0)  
label_1.config(padx=20, pady=20)  

entry_miles = Entry(width=10)  
entry_miles.insert(END, string="0")
entry_miles.grid(column=1, row=0)  

label_2 = Label(text="is equal to", font=FONT)
label_2.grid(column=0, row=1)
label_2.config(padx=20, pady=20)  

label_km = Label(text="0")
label_km.grid(column=1, row=1)  

label_3 = Label(text="km", font=FONT)
label_3.grid(column=2, row=1)  
label_3.config(padx=20, pady=20)  

button = Button(text="calculate", command=miles_to_km)  
button.grid(column=1, row=3)
button.config(padx=20, pady=20)  

window.mainloop()  
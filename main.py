from tkinter import *
from tkinter import messagebox
def calculate_bill():
    total=0
    order_details=""
    for item,price in menu.items():
        quantity=quantities[item].get()
        if quantity>0:
            total=total+(quantity*price)
            order_details=order_details+f"{item} x {quantity}=${quantity*price}\n"
    messagebox.showinfo("Your bill",f"Your order\n{order_details}\ntotal:${total}")  

def reset_order():
    for item in menu:
        quantities[item].set(0)

menu={"burger":5,"pizza":8,"fries":2,"coke":3}
window=Tk()
window.title("Resturant management app")
window.geometry("300x300")
title_label=Label(window,text="Resturant menu",font=("Arial",16))
title_label.pack(pady=10)
menu_frame=Frame(window)
menu_frame.pack(pady=10)
quantities={}

for item,price in menu.items():
    frame=Frame(menu_frame)
    frame.pack(pady=10)
    label2=Label(frame,text=f"{item}(${price})",font=("Arial",12))
    label2.pack(side="right")
    quantities[item]=IntVar()
    entry =Entry(frame, textvariable=quantities[item], width=5)
    entry.pack(side="right")

button_frame=Frame(window)
button_frame.pack(pady=20)
submit_button=Button(button_frame,text="Submit",command=calculate_bill,bg="green",fg="white")
reset_button=Button(button_frame,text="Reset",command=reset_order,bg="red",fg="white")
submit_button.pack(side="left",padx=10)
reset_button.pack(side="right",padx=10)
window.mainloop()
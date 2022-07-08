import requests
from tkinter import *

delta = 0


def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    data = response.json()

    canvas.itemconfig(quote_text, text=data["quote"])


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)
window.config(bg="white")

canvas = Canvas(width=300, height=414, bg="white", highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click me for a Qoute", width=250,
                                font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote,
                      highlightbackground="white", bg='white')
kanye_button.grid(row=1, column=0)

window.mainloop()

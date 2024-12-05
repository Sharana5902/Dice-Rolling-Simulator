import tkinter as tk
from PIL import Image, ImageTk
import random

#list of dice images
dice = ["dice 1.jpg","dice 2.jpg","dice 3.jpg","dice 4.jpg","dice 5.jpg","dice 6.jpg"]



# function to roll dice
def roll_dice():
    random_1 = random.choice(dice)
    random_2 = random.choice(dice)
    first_dice = Image.open(random_1)
    second_dice = Image.open(random_2)

    image1 = ImageTk.PhotoImage(first_dice) #store random dice as first image
    label1.configure(image=image1)
    label1.image = image1
    image2 = ImageTk.PhotoImage(second_dice) #store random dice as second image
    label2.configure(image=image2)
    label2.image = image2

    #storing total value of the dice
    total = dice.index(random_1)+dice.index(random_2)+2
    total_label.config(text=total)





#create GUI components
window = tk.Tk()
window.title("Dice Roll Simulator")
window.geometry("500x350")

#creating a label for displaying images
#storing images of dice

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))


label1 = tk.Label(window,image=image1)
label1.place(x= 150, y= 117 )
label2 = tk.Label(window,image=image2)
label2.place(x=250, y= 117)

#create button to roll the dice
button = tk.Button(window, text="Roll Dice", command=roll_dice, fg="white", bg="green",font="Times 18 bold")
button.place(x=185, y= 60 )

#frame for displaying total value
frame = tk.Frame(window, relief='solid',borderwidth=3)
frame.place(x=350, y= 140)
total_label = tk.Label(frame, text='1', font='Times 15 bold',fg='green')
total_label.pack(padx=5, pady=5)


window.mainloop()

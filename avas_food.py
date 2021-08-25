
from tkinter import *
import random as rd
from PIL import ImageTk, Image
global page_num
global theme_frame
page_num = 0
#create main widget 
root = Tk()
root.title("Ava's Meal Assistance")
root.geometry("400x400")
root.iconbitmap('icon_hellokitty.ico')



bg_color = ["#EEA2AD", "#436EEE"]
root.configure(bg= bg_color[page_num])

#list of images that will be used 
my_img1 = ImageTk.PhotoImage(Image.open("hellokittybg.png"))
my_img2 = ImageTk.PhotoImage(Image.open("doraemonbg.png"))
my_images = [my_img1, my_img2]

#create entry widget
e = Entry(root, font= ("Helvetica", 20, "bold italic"), width = 25)
e.grid(column=0, row =0, padx=10 , pady= 10, columnspan= 3, sticky = E + W)

#create function to return the meal
def meal_choice():
    #but this in heat so new meal in chosin whith each click
    meals = ["pesto pasta", "tofu scramble", "poke bowl", "smoothie bowl", "tofu with veggies", "vegan dumplings", "veggie tacos"]
    index = rd.randint(0, (len(meals)-1))
    e.delete(0, END)
    e.insert(0, meals[index])

def forward(page_num):
    global theme_frame
    global hello_kitty
    global doraemon
    
    page_num += 1

    root.configure(bg = bg_color[page_num])

    #update photo
    hello_kitty.grid_forget()
    doraemon = Label(padx= 10, pady = 10, image= my_images[page_num], bg = bg_color[page_num])
    doraemon.grid(row= 4, column = 1)

    #update frame
    theme_frame.grid_forget()
    theme_frame = LabelFrame(root, text= "Theme", font =("Helvetica", 10, "bold italic"), bg = bg_color[page_num], padx= 25)
    theme_frame.grid(row= 6, column = 1, )

    spacer = Label(bg = bg_color[page_num])
    spacer.grid(row= 3, column = 1)
    
    button_for  = Button(theme_frame, text= ">>", command= lambda: forward(page_num), activebackground = "pink",bg= "white", font =("Helvetica", 10, "bold italic"),state= DISABLED)
    button_back = Button(theme_frame, text= "<<", command= lambda: backward(page_num), activebackground = "pink",bg= "white", font =("Helvetica", 10, "bold italic") )
    button_for.grid(row = 6, column = 2)
    button_back.grid(row = 6, column = 0)

    
    

def backward(page_num):
    global theme_frame
    global doraemon
    global hello_kitty

    page_num -= 1 
    
    root.configure(bg = bg_color[page_num])

    #update photo
    doraemon.grid_forget()
    hello_kitty = Label(padx= 10, pady = 10, image= my_images[page_num], bg = bg_color[page_num])
    hello_kitty.grid(row= 4, column = 1)

    #update frame
    theme_frame.grid_forget()
    theme_frame = LabelFrame(root, text= "Theme", font =("Helvetica", 10, "bold italic"), bg = bg_color[page_num], padx= 25)
    theme_frame.grid(row= 6, column = 1, )

    spacer = Label(bg = bg_color[page_num])
    spacer.grid(row= 3, column = 1)
    
    button_for  = Button(theme_frame, text= ">>", command= lambda: forward(page_num), activebackground = "pink",bg= "white", font =("Helvetica", 10, "bold italic"))
    button_back = Button(theme_frame, text= "<<", command= lambda: backward(page_num), activebackground = "pink",bg= "white", font =("Helvetica", 10, "bold italic"), state = DISABLED)
    button_for.grid(row = 6, column = 2)
    button_back.grid(row = 6, column = 0)
    
    
#create frame 
theme_frame = LabelFrame(root, text= "Theme", font =("Helvetica", 10, "bold italic"), bg = bg_color[page_num], padx= 25)
theme_frame.grid(row= 6, column = 1, )
    
 
#create button 
button_choose = Button(root, text= "click me", command= meal_choice, activebackground = "pink",bg= "white", font =("Helvetica", 10, "bold italic") )
button_for  = Button(theme_frame, text= ">>", command= lambda: forward(page_num), activebackground = "pink",bg= "white", font =("Helvetica", 10, "bold italic") )
button_back = Button(theme_frame, text= "<<", command= lambda: backward(page_num), activebackground = "pink",bg= "white", font =("Helvetica", 10, "bold italic") )
#place button 
button_choose.grid(row= 1 , column =  1, rowspan= 2)
button_for.grid(row = 6, column = 2)
button_back.grid(row = 6, column = 0)


#create picture label 
hello_kitty = Label(padx= 10, pady = 10, image= my_img1, bg = bg_color[page_num])
hello_kitty.grid(row= 4, column = 1)

#create spacer label
spacer = Label(bg = bg_color[page_num])
spacer.grid(row= 3, column = 1)

root.mainloop()
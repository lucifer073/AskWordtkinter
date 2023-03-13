from enum import unique
from tkinter import *
from tkinter import messagebox
from tkinter import font
import requests
from bs4 import BeautifulSoup
import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.resizable(False,False)

# setting dimensions of tk window
root.geometry("500x500")

# using title() to display message at the top
root.title("ShabdhKosh with Python")

# search word string 
search_word = StringVar()

#entry box to write word
search_word_Entry = customtkinter.CTkEntry(root, width=180, height = 40,fg_color="black", textvariable=search_word).place(x=160, y=100)



def submit():


    # #website used for finding meaning
    search_website = 'https://www.dictionary.com/browse/'
    
    word = str(search_word.get())

    url = str(search_website) + str(word)

    resp = requests.get(url)

    soup=BeautifulSoup(resp.text,'html.parser')    
  
    # # l is the list which contains all the meaning 
    
    l=soup.find("span",{"class":"one-click-content css-nnyc96 e1q3nk1v1"})
    # #now we want to print only the text part of the anchor.
    # #find all the elements of a, i.e anchor tag
    
    material = ""

    if l is not None:
        for i in l:
             material = material + i.text

    # #show meaning in messagebox
    if l is None:
        material = "Sorry, couldn't find your word😥😓"

    messagebox.showinfo("meaning of " + word , material)
    
    # print(word)


button = customtkinter.CTkButton(master = root , text = 'Search!' , command = submit).place(x = 180 , y = 200)


root.mainloop()


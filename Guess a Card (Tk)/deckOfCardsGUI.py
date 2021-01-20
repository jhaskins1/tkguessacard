#This program will pick a random card and have the user guess it, with a gui
from random import randint
from time import sleep
from tkinter import *

suitList = ["diamonds", "clubs", "hearts", "spades"]
valueList = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
guesses = 9
randomCard = valueList[randint(0, 12)] + " of " + suitList[randint(0, 3)]
print(randomCard)

def submit(buttonS):
    global randomCard
    global guesses
    global textEntry
    guesses = guesses - 1
    enteredText = textEntry.get() #Retrieve value from text box
    enteredText = enteredText.lower() #Make value lower cased so that it will match randomcard
    if guesses == 0 and enteredText != randomCard:
        #Test if the person has no more guesses left and has guessed wrong.
        output = Label(frame, width=85, text="You have no more guesses left and have guessed wrong! Better luck next time Bozo!", background="white", font='fixedsys 17 bold')
        output.grid(row=5, column=0, columnspan=2, sticky=N, pady=5)

        Button (frame, text="SUBMIT", width=30, state=DISABLED, bg="black", fg="white", font='fixedsys 20 bold') .grid(row=4, column=0, sticky=N, pady=5)
        window.unbind("<Return>", submit)
        
        textEntry.delete( 0, END)
        textEntry.config(state=DISABLED)
        
    elif guesses == 0 and enteredText == randomCard:
        #Text if the person has no more guesses left and has guessed correctly.
        output = Label(frame, width=85, text="Congratulations! You got it right on your last guess!", background="white", font='fixedsys 17 bold')
        output.grid(row=5, column=0, columnspan=2, sticky=N, pady=5)

        Button (frame, text="SUBMIT", width=30, state=DISABLED, bg="black", fg="white", font='fixedsys 20 bold') .grid(row=4, column=0, sticky=N, pady=5)
        window.unbind("<Return>", submit)
        
        textEntry.delete( 0, END)
        textEntry.config(state=DISABLED)
        
    elif guesses != 0 and enteredText != randomCard:
        #Test if the user has guesses left and has guessed wrong.
        output = Label(frame, width=85, text="You have guessed wrong Bozo! You have " + str(guesses) + " guesses left!", background="white", font='fixedsys 17 bold')
        output.grid(row=5, column=0, columnspan=2, sticky=N, pady=5)

        textEntry.delete( 0, END)
        
    elif guesses != 0 and enteredText == randomCard:
        #Test if the user has guesses left and has guessed correctly.
        if guesses != 7:
            output = Label(frame, width=85, text="Congratulations! It took you " + str(8 - guesses) + " tries to get it right.", background="white", font='fixedsys 17 bold')
            output.grid(row=5, column=0, columnspan=2, sticky=N, pady=5)

            Button (frame, text="SUBMIT", width=30, state=DISABLED, bg="black", fg="white", font='fixedsys 20 bold') .grid(row=4, column=0, sticky=N, pady=5)
            window.unbind("<Return>", submit)
            
            textEntry.delete( 0, END)
            textEntry.config(state=DISABLED)
            
        else:
            output = Label(frame, width=85, text="Congratulations! It took you only 1 try to get it right.", background="white", font='fixedsys 17 bold')
            output.grid(row=5, column=0, columnspan=2, sticky=N, pady=5)

            Button (frame, text="SUBMIT", width=30, state=DISABLED, bg="black", fg="white", font='fixedsys 20 bold') .grid(row=4, column=0, sticky=N, pady=5)
            window.unbind("<Return>", submit)

            textEntry.delete( 0, END)
            textEntry.config(state=DISABLED)


def stop():
    window.destroy()
    
############################################################################################ GUI
window = Tk()
window.title("The Deck of Cards Card Picking Game That Was Coded by a Literal Living Legend")
window.configure(background='#004d00', cursor="pirate")
frame = Frame(window, background='#004d00')
frame.pack(anchor=CENTER, pady=15)

# make it cover the entire screen
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.overrideredirect(1) #ENABLE TO GO FULLSCREEN
window.geometry("%dx%d+0+0" % (w, h))

#Deck of Cards photo
photo1 = PhotoImage(file='cards.gif')
Label (frame, image=photo1, bg='black') .grid(row=0, column=0, sticky=N, pady=20)

#Label to explain
explain = Label (frame, text='''\nWe have selected a random card from our deck of 52 cards.
Try to guess which card we have chosen!
When you format your guess please type it like this: "Jack of Spades".
Capitalization is not required to match.
Good luck!\n''', bg='#004d00', fg='white', font='fixedsys 22 bold') .grid(row=1, column=0, sticky=N, pady=20)

#Label to put guess
Label (frame, text="Enter your guess", bg='#004d00', fg='white', font='fixedsys 20 bold') .grid(row=2, column=0, sticky = N)

#Text box for guess
textEntry = Entry (frame, width=30, bg='white', font='fixedsys 18 bold', justify='center')
textEntry.grid(row=3, column = 0, sticky=N, pady=5)

#Button to submit
buttonS = Button(frame, text="SUBMIT", width=30, command=submit(0), bg="black", fg="white", font='fixedsys 20 bold')
buttonS.grid(row=4, column=0, sticky=N, pady=5)

#Right or wrong label
output = Label(frame, width=85, text="", background="white", font='fixedsys 17 bold')
output.grid(row=5, column=0, columnspan=2, sticky=N, pady=5)

#EXIT BUTTON
Button(frame, width=30, text="EXIT", command=stop, bg="red", fg="white", font='fixedsys 20 bold') .grid(row=6, column=0, sticky=N, pady=5)

window.bind("<Return>", submit)
buttonS.bind("<Button-1>", submit)

window.mainloop()



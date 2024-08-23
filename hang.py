import random
from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.title("Hangman")
screen.geometry("400x400")

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret ' \
        'fox frog goat goose hawk lion lizard lama mole monkey moose mouse mule newt otter owl panda parrot pigeon ' \
        'python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad ' \
        'trout turkey turtle weasel whale wolf wombat zebra'.split()
a = random.choice(words)

x = []
y = []
hg_fig = 0

head = Label(screen, text="Welcome to Hangman Game, \nWhere you have to guess the word randomly selected by computer")
head.grid(row=0, column=1, padx=30, pady=10)

for i in a:
    x.append(i)
for i in x:
    y.append("_")

lives = len(HANGMANPICS) - 2
space = Label(screen, text=str(y))
space.grid(row=2, column=1)
hg = Label(screen, text=HANGMANPICS[hg_fig])
hg.grid(row=3, column=1)


def getit():
    gue = al.get()
    global lives, hg_fig
    res = Label(screen, text="")
    res.grid(row=8, column=1)
    if lives > 0:
        if gue in x:
            for i in range(len(x)):
                if x[i] == gue:
                    y[i] = x[i]
            space = Label(screen, text=str(y))
            space.grid(row=2, column=1)
            res.config(text="Yes! You have guessed it right")
        elif gue not in x:
            res.config(text="Oops! You guessed it wrong")
            res.grid(row=8, column=1)
            lives -= 1
            hg_fig += 1
            hg.config(text=HANGMANPICS[hg_fig])
            l_variable.config(text=f"Lives Count: {lives+1}")

    elif lives == 0:
        l_variable.config(text=f"Lives Count: {lives}")
        hg.config(text=HANGMANPICS[hg_fig+1])
        final = Label(screen, text="You Have lost")
        final.grid(row=9, column=1)
        al.destroy()
        l2.destroy()
        b1.destroy()
        messagebox.showinfo("Hangman", "You have lost all the lives \nYou Lost")


    if x == y:
        final = Label(screen, text="You Have Guessed the word")
        final.grid(row=9, column=1)
        al.destroy()
        l2.destroy()
        b1.destroy()
        messagebox.showinfo("Hangman", "Congrats! You Have guessed the word")




guessed = False

al = Entry()
l2 = Label(screen, text="Enter the letter:")
l2.grid(row=5, column=1)
al.grid(row=6, column=1)
b1 = Button(screen, text="Enter", command=getit)
b1.grid(row=7, column=1)
l_variable = Label(screen, text=f"Lives Count: {lives+1}")

l_variable.grid(row=4, column=1)
l_c = Label(screen, text=lives)
screen.mainloop()
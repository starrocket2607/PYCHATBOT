from nltk.chat.util import Chat, reflections

from tkinter import *


def open_window(): 
    top = Toplevel() 
    top.title("Space Time")
    top.geometry("400x500") 
    top.resizable(width=TRUE, height=FALSE)
    chatWindow = Text(top, bd=1, bg="black",  width="50",  font=("Arial", 15), foreground="#00ffff") 
    chatWindow.place(x=6,y=6, height=385, width=370)
    def chattychatty():     
        pairs = [['(hi|hola|hiya|hey|hey there|hello)', ['Hi there Astronaut','I am an Astronaut reporting at your service','Hello Space Explorer']],
             ['(What (.*) name?|Whats (.*) name)', ['Call me whatever you like. Enter a name in the textbox that just dropped into your screen from SPACE!']],
             ['Name: (.*)', ['What a Spacetacular name! %1']],
             ['(.*) is space weather (.*)', ['OOOOO COLD!']],
             ['(How do you do|howz life|how is life|wassup|whats up)', ['Another day in the darknesss of space', 'Counting meteorites and stars', 'Burning in the heat of the Sun']],
             ['Who made you|Who is your creater|WHo is the genius that made you|Who is the smartest person on earth', ['My creaters who are probably the smartest people on Earth are: Rishabh And Anshu']],
             ['(.*)', ['I am sorry... I am just a machine lost in space... Try asking me \n Jokes \n Quiz \n or tey contacting my SOLAR SYSTEM DETECTER']],
             ['(.*) Jokes', ['How do you throw a space party... You PlanET', 'Why did the sun go to school.... To get brighter!', 'What is a spaceman’s favorite chocolate?......  A marsbar!', 'What kind of music do planets sing?....  Neptunes!', 'What’s a light-year?.... The same as a regular year, but with less calories.']]] 
        chat = Chat(pairs, reflections) 
        chatWindow.insert(INSERT,chat.respond( e.get())+'\n') 
        e.delete(0, 'end') 
        if (chatWindow.cget('text')=='Call me whatever you like. Enter a name in the textbox that just dropped into your screen from SPACE!'): 
            e.insert(0, 'Name: ')
    e = Entry(top, bd=0, bg="black",width="30", font=("Arial", 23), foreground="#00ffff") 
    chatWindow.pack()
    e.pack()
    c = Button(top, command=chattychatty,text="Send",  width="12", height=5,
                    bd=0, bg="pink", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12)).pack() 
    top.mainloop()

    
    
  



root = Tk()
button = Button(root, text="open window", command=open_window)
button.pack()

root.geometry("300x300+120+120")
root.mainloop()


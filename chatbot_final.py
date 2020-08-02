from nltk.chat.util import Chat, reflections
from tkinter import *

root = Tk()
root.title("Space Time")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)
main_menu = Menu(root)
file_menu = Menu(root)

file_menu.add_command(label="New..")
file_menu.add_command(label="Save As..")
file_menu.add_command(label="Exit")
main_menu.add_cascade(label="File", menu=file_menu)
   
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
root.config(menu=main_menu)

chatWindow = Text(root, bd=1, bg="black",  width="50",  font=("Arial", 15), foreground="#00ffff")
chatWindow.place(x=6,y=6, height=385, width=370)
messageWindow = Text(root, bd=0, bg="black",width="30", height="4", font=("Arial", 23), foreground="#00ffff")
messageWindow.place(x=6, y=400, height=88, width=260)
Button123= Button(root, text="Send",  width="12", height=5,
                    bd=0, bg="pink", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12))
Button123.place(x=260, y=400, height=88)


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
    
            
e = Entry(root, width=50)
chatWindow.pack()

e.pack()
#chatWindow.pack(fill=BOTH)

c = Button(root, command=chattychatty).pack()

root.mainloop()
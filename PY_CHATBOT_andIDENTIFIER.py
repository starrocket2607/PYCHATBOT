from tkinter import *
  
from PIL import ImageTk, Image 
    
from tkinter import filedialog 
from numpy import loadtxt
from keras.models import load_model
import numpy as np
from numpy import asarray

model = load_model('modelnew.h5')
model.summary()

planets = {0:'Mercury', 1:'Venus', 2:'Earth', 3:'Mars', 4:'Jupiter', 5:'Saturn', 6:'Uranus', 7:'Neptune', 8:'Pluto', 9:'Galaxy'}
root = Tk() 
  
root.title("Planet Predicter") 
  
root.geometry("400x500")
  
root.resizable(width = True, height = False) 

def open_window(): 
    
    
    top = Toplevel() 
    top.title("Astrobot")
    top.geometry("500x700") 
    top.resizable(width=True, height=True)
    chatWindow = Text(top, bd=1, bg="black",  width="50",  font=("Arial", 15), foreground="#40ffff") 
    chatWindow.place(x=6,y=6, height=385, width=370)
    
    def chattychatty():     
        pairs = [['(hi|hola|hiya|hey|hey there|hello)', ['Hi there Astronaut','I am an Astronaut reporting at your service','Hello Space Explorer']],
             ['(What (.*) name?|Whats (.*) name)', ['My name is AstroBot']],
             ['(.*) space weather', ['OOOOO COLD!']],
             ['(.*)you are a genius',['I know!my creaters made me that way']],
             ['(.*) fact',['There are an estimated 100-400 billion stars in our galaxy, the Milky Way','There are an estimated 100-400 billion stars in our galaxy, the Milky Way','Space is a hard vacuum, meaning it is a void containing very little matter.' ]],
             ['(How do you do|howz life|how is life|wassup|whats up)', ['Another day in the darknesss of space', 'Counting meteorites and stars', 'Burning in the heat of the Sun']],
             ['(Who made you|Who is your creater|WHo is the genius that made you|Who is the smartest person on earth)', ['My creaters who are probably the smartest people on Earth are: Rishabh And Anshu']],
             ['(.*) joke', ['How do you throw a space party... You PlanET', 'Why did the sun go to school.... To get brighter!', 'What is a spaceman’s favorite chocolate?......  A marsbar!', 'What kind of music do planets sing?....  Neptunes!', 'Whats a light-year?.... The same as a regular year, but with less calories.']],
             ['(.*)', ['I am sorry... I am just a machine lost in space... \n Try asking me- \nJokes \nFacts \Try contacting my SOLAR SYSTEM DETECTER']]] 
        chat = Chat(pairs, reflections) 
        chatWindow.insert(INSERT,"--> Astrobot: \n \n"+chat.respond( e.get())+'\n'+'\n') 
        e.delete(0, 'end') 
    
    e = Entry(top, bd=0, bg="black",width="30", font=("Arial", 23), foreground="#fcba03") 
    chatWindow.pack()
    e.pack()
    c = Button(top, command=chattychatty,text="Send",  width="12", height="5",
                    bd=0, bg="pink", activebackground="pink",foreground='#1c1b1a',font=("Arial", 12)).pack() 
    top.mainloop()

def openfilename(): 
  
    filename = filedialog.askopenfilename(title ='"pen') 
    return filename 
 

def open_img(): 
      
    x = openfilename()
    img = Image.open(x)     
    img = img.resize((250, 250), Image.ANTIALIAS)  
    img = ImageTk.PhotoImage(img)   
    panel = Label(root, image = img, bg="black")       
    panel.image = img 
    panel.place(x=87, y=87, height=250) 
    
    imgpredicted = np.zeros((1, 300,300,3))
    img1234567 = np.array(Image.open(x).resize((300,300)))
    imgpredicted[0] = img1234567
    x123 = imgpredicted
    print(x123)
    print(x123.shape)
    disp = Label(root, text=planets[model.predict(x123).argmax()], bd=1, bg="black",  width="43",  font=("Arial", 15), foreground="#00ffff")
    disp.place(x=0, y=338, height=88)

btn = Button(root, text ='Click here to open a planet photo \n and predict which planet it is \n I am a Convolutional Neural Network!!', command = open_img, width="44", height=5, 
             bd=1, bg="#ffb300", activebackground="yellow",foreground='#1c1b1a',font=("Arial", 12)) 
btn.place(x=0, y=0, height=88)

button = Button(root, text="open our astro chatbot",width='22', height='5',bd=1, bg="#ffb300", activebackground="yellow",foreground='#1c1b1a',font=("Arial", 12),command = open_window)
button.place(x=100,y=400)


root.mainloop() 
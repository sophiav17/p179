from tkinter import*
import random

root = Tk()

root.title("Color Randomiser")
root.geometry("800x600")
root.configure(background="pink")

label_score = Label(root, text = "Score: 0", font = ("ComicSans", 15, "bold"), bg = "pink")
label_score.place(relx = 0.1, rely= 0.2, anchor = CENTER)

random_name = Label(root, font = ("Comicsans", 18, "bold"), bg = "pink")
random_name.place(relx = 0.5, rely = 0.4, anchor = CENTER)

input_value = Entry(root)
input_value.place(relx = 0.5, rely = 0.5, anchor = CENTER)


class game :
    def __init__(self) :
        self.__score = 0
    def updateGame(self) :
        self.text = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
        self.random_number_for_text = random.randint(0, 6)
        self.color = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
        self.random_number_for_color = random.randint(0, 6)
        random_name["text"] = self.text[self.random_number_for_text]
        random_name["fg"] = self.color[self.random_number_for_color]
        
    def __updateScore(self, input_value) :
        if(input_value == self.color[self.random_number_for_color]) :
            self.__score = self.__score + random.randint(0, 10)
            label_score["text"] = "Score: " + str(self.__score)
            
    def get_user_value(self, input_value) :
        self.__updateScore(input_value)
        
obj = game()

def get_input(self, input_value) :
    value = input_value.get()
    obj.get_user_value(value)
    obj.updateGame()
    input_value.delete(0, END)

btn1 = Button(root, text= "START", command = obj.updateGame, bg = "DarkOliveGreen3", fg = "white", relief = FLAT, padx = 10, pady = 1, font = ("Comicsans", 15 ))
btn1.place(relx = 0.6, rely = 0.6, anchor = CENTER)

btn2 = Button(root, text= "CHECK", command = get_input, bg = "VioletRed1", fg = "white", relief = FLAT, padx = 10, pady = 1, font = ("Comicsans", 15 ))
btn2.place(relx = 0.4, rely = 0.6, anchor = CENTER)

root.mainloop()
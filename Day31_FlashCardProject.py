from tkinter import * 
import pandas
import random 

BACKGROUND_COLOR = "#B1DDC6"

df = pandas.read_csv("C:\\Users\\KIIT\\Desktop\\100Days_code_programming\\data\\french_words.csv") 

df_dict = df.to_dict(orient="records")  # to convert into dictionary data with orient = record french:English key, value all the records there in dict  
#print(df_dict)
#Create a next card function 
current_card = {}    # Set new blank dictionary 
def next_card():
    global current_card, flip_time   # here assigned global variable 
    current_card = random.choice(df_dict)  # here user can choose choice 
    #print(current_card["French"])
    root.after_cancel(flip_time)
    canvas.itemconfig(canvas_title, Text="French", fill="black")
    canvas.itemconfig(canvas_words, Text=current_card["French"], fill="black")
    canvas.itemconfig(card_background,image=card_back_img, )

def flip_card():
    canvas.config(canvas_title, text="English")
    canvas.config(canvas_words, text = current_card["English"])
    canvas.config(card_background, image=card_back_img)
    root.after(3000, func=flip_card)


def is_known():
    df_dict.remove(current_card)  # here the element will be remove df_dict with method current_card 
    print(len(df_dict))
    data1 = pandas.DataFrame(df_dict)
    data1.to_csv("C:\\Users\\KIIT\\Desktop\\100Days_code_programming\\data\\words_to_learn.csv")



    next_card()
    
root = Tk()
root.title("Flashy")
root. config(padx=50, pady=50)

flip_time = root.after(3000, func=flip_card) # window will new background after 3000

canvas = Canvas(root, width=800, height=526)
card_front_img =PhotoImage(file="C:\\Users\\KIIT\\Desktop\\100Days_code_programming\\images\\card_front.png")
card_back_img = PhotoImage(file="C:\\Users\\KIIT\\Desktop\\100Days_code_programming\\images\\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas_title =canvas.create_text(400, 150, text="Title", font=("Arial", 40,"italic"))
canvas_words =canvas.create_text(400, 263, text="Words", font=("Arial", 60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightbackground="blue")   # here it's used for backgroud color and highlight border all around 
canvas.grid(row=0, column=0, columnspan=2)
cross_button =PhotoImage(file="C:\\Users\\KIIT\\Desktop\\100Days_code_programming\\images\\wrong.png")
unknown_button = Button(image=cross_button, highlightbackground="red")
unknown_button.grid(row=1, column=0)

right_button =PhotoImage(file="C:\\Users\\KIIT\\Desktop\\100Days_code_programming\\images\\right.png")
known_button = Button(image=right_button, highlightbackground="red")  
known_button.grid(row=1, column=1)






root.mainloop()
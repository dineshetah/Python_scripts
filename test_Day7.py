Step-1
word_list = ["ardvark","baboon","camel"]
Todo-1- Randomly choose a word from the word_list and assign it to a variable called chosen_word 
import random
like_word = random.choice(word_list)
print(like_word)

Todo-2-Ask the user to guess a letter and assign their answer to a variable 
called guess. make guess lower can 
guess = input("Enter the guess letter: ").lower 

Todo-3- Check if the letter the user guessed (guess) is one of the letters in the like_word
for word in like_word:
    if word == guess:
      print("Right")
else:
    print("wrong")

Step-2
    import random
    word_list = ["ardvark","baboon","camel"]
    like_word = random.choice(word_list)
    #print(f"EPSTTT, the solution is {like_word} ") # testing code
    guess = input("Enter the guess letter: ").lower 
Todo -1.1 - create an empty list called display.
for each letter in the like_word, add a "-" to 'display 

So, if the like_word was "apple",display should be ["_","_","_","_"] with 5 "_"representing each lette to guess.
for letter in like_word:
    if letter == guess:
        print("Right")
    else:
        print("Wroug")
for more practice go for website developer goggle 
display = []
#for _ in range (len(like_word_word))
word_length = len(word_list)
for _ in range(word_length)
#for letter in like_word:
    display += "_"
    print(display)
    guess = input ("Gauss a letter") .lower()              

ToDo-3:-print display and you should see the guessed letter in the correct position and 
every other letter replace with "_"

e.g if the user guessed "p" and the chosen word was "apple", then display 
   should be [ "_","_", "p"            

for position in range (word_list):
    letter = like_word[position]
    if letter ==guess:
           display[position]=letter

display =[]
word_length = len(like_word)
for _ in range(word_length)
letter = like_word(position)

if letter == guess:
     display[position]= letter
     print(display )

Step 3 
import random
word_list = ["ardvark","baboon","camel"]
chose_word = random.choice(word_list)
word_length = len(chose_word)
 
if not True:
   end_of_game = False

# create blanks 
display = []
for _ in range(word_length):
    display +=""
#guess = input("Enter the guess letter: ").lower
# Todo -1: - Use a while loop to let the user guess again. The loop should
#only stopp once the user has guessed all the letters in the chosen_word and display has no more bankks("")
#them you can tell the user they have wo.

end_of_game = False
while not end_of_game:
    guess = input("Enter the guess letter: ").lower
# check guessed letter 
for position in range (word_list):
   letter= chose_word[position]
   print (f"Current postition: {position}\nCurrent letter :{letter}\n guessed letter : {guess}")

   if letter == guess:
          display[position]= letter
print(display)

if "_" not in display:
     end_of_game = True
     print("You Win.")
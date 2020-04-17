from random import *
import turtle

def drawstruct():
    #t.pencolor("white")
    turtle.ht()
    turtle.up()
    turtle.goto(180,0)
    turtle.down()
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(45)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.up()

def drawtitle():
    turtle.ht()
    turtle.up()
    turtle.goto(-325,250)
    style = ('Courier', 23, 'underline')
    turtle.write("Andie's Hangman: You get 10 guesses! ", font=style)
    
    
def makeblank(word):
    return len(word)

def drawblanks(blank, size, space):
    turtle.ht()
    x = -300
    y = 0
    count = 0
    while count < blank:
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
        turtle.forward(size)
        x += (space + size)
        count += 1
    turtle.up()

def writeguessed(letters):
    count = 0
    style = ('Courier', 20)
    style2 = ('Courier', 18)
    turtle.up()
    turtle.goto(-325, 200)
    turtle.down()
    turtle.write("Guessed Letters: ", font=style)
    turtle.up()
    x = -45
    y = 201
    
    for i in letters:
        turtle.up()
        turtle.goto(x,y)
        x += 20
        turtle.down()
        let = str(i)
        turtle.write(let, font=style2)
        turtle.up()
        
def placeletter(letter, word, blank, size, space):
    count = 0
    temp = -1
    x = -323
    y = 1
    while count < len(word):
        if(letter == word[count]):
            turtle.goto(x, y)
            turtle.down()
            style = ('Courier', 25)
            turtle.write(letter, font=style)
            turtle.up()
        x += space
        x += size
        count += 1
            
        
def checkwin(word, letters):
    count = 0
    numOfLetters = 0
    won = False
    while(count < len(word)):
        for i in letters:
            if word[count] == i:
                numOfLetters += 1
        count += 1
    if numOfLetters >= len(word):
        return True
    else:
        return False

def drawbody(numWrong):
    if(numWrong == 1):
        turtle.up()
        turtle.goto(135,125)
        turtle.down()
        turtle.circle(10)
        turtle.up()
    elif(numWrong == 2):
        turtle.up()
        turtle.goto(135,105)
        turtle.down()
        turtle.left(90)
        turtle.forward(35)
        turtle.up()
    elif(numWrong == 3):
        turtle.up()
        turtle.goto(135,70)
        turtle.down()
        turtle.left(45)
        turtle.forward(10)
        turtle.right(15)
        turtle.forward(15)
        turtle.up()
    elif(numWrong == 4):
        turtle.up()
        turtle.goto(135,70)
        turtle.down()
        turtle.right(75)
        turtle.forward(10)
        turtle.left(15)
        turtle.forward(15)
        turtle.up()
    elif(numWrong == 5):
        turtle.up()
        turtle.goto(135,95)
        turtle.down()
        turtle.right(15)
        turtle.forward(15)
        turtle.left(10)
        turtle.forward(10)
        turtle.up()
    elif(numWrong == 6):
        turtle.up()
        turtle.goto(135,95)
        turtle.down()
        turtle.left(75)
        turtle.forward(15)
        turtle.right(10)
        turtle.forward(10)
        turtle.up()
    elif(numWrong == 7):
        turtle.up()
        turtle.goto(117, 75)
        turtle.down()
        turtle.circle(3)
    elif(numWrong == 8):
        turtle.up()
        turtle.goto(148, 75)
        turtle.down()
        turtle.circle(3)
    elif(numWrong == 9):
        turtle.up()
        turtle.goto(117, 45)
        turtle.down()
        turtle.circle(3)
        turtle.up()
    elif(numWrong == 10):
        turtle.up()
        turtle.goto(148, 45)
        turtle.down()
        turtle.circle(3)
        turtle.up()

        
def Wongame(word, letters):
    print("You won!")
    turtle.up()
    turtle.goto(-325, 75)
    turtle.down()
    style = ('Courier', 30)
    turtle.write("YOU WON!", font=style)
    
def Lostgame(word):
    print("You lost! The word was: " + word)
    turtle.up()
    turtle.goto(-380, 75)
    turtle.down()
    style = ('Courier', 30)
    lostPhrase = "You Lost! The word was: " + word
    turtle.write(lostPhrase, font=style)
   

def playground(word, letters, wrong):
    turtle.setup(900,1000,100,100)
    turtle.clear()
    turtle.pencolor("white")
    turtle.bgcolor("black")
    turtle.bgpic("starImage.gif")

    drawstruct()
    drawtitle()
    player = True
    blank = makeblank(word)
    size = 30
    space = 10
    drawblanks(blank, size, space)
    xcoord = -400
    ycoord = 400
    line = 0
    playvar = True

    wrong = 0
    numRight = 0
    
    while playvar:
        print(letters)
        writeguessed(letters)
        letter = turtle.textinput("Title Window", "Guess a Letter")
        line = line + 1
        if letter in letters:
            print("Sorry, that letter has already been guessed!")
        elif letter in word:
            placeletter(letter, word, blank, size, space)
            letters.append(letter)
            if checkwin(word,letters):
                Wongame(word,letters)
                playvar = False
        else:
            wrong += 1
            drawbody(wrong)
            letters.append(letter)
            if wrong == 10:
                Lostgame(word)
                playvar = False
        print(blank)
    return

def getWord():
    listOfWords = ["python", "coding", "music", "movie", "school", "guitar", "word", "pet","dog", "happy", "cat", "mouse", "rabbit", "fox", "puppy", "box", "socks", "computer", "keyboard", "delaware", "test"]
    randNum = randrange(0, len(listOfWords))
    return(listOfWords[randNum])

letters = []
newWord = getWord()
playground(newWord, letters, False)

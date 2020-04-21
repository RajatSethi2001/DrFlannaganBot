from graphics import *
import time
import random

def Respond(prompt):
    global waitTime
    time.sleep(waitTime)
    promptArr = prompt.split(':')
    FlannyText = ''
    if (len(promptArr) == 1): #Enqueue Random Quote
        myPrompt = promptArr[0]
        myPrompt = myPrompt.upper()
        if ("MR. FLANNAGAN" in myPrompt or "MISTER FLANNAGAN" in myPrompt):
            Enqueue([2, "Um, that's Dr. Flannagan."])
        
        elif ('SPONGEBOB' in myPrompt or 'SQUAREPANTS' in myPrompt):
            Enqueue([2, "I wouldn't say that Spongebob Squarepants is a form of literature."])
            
        elif ("UNIVERSITY" in myPrompt or "COLLEGE" in myPrompt or "UVA" in myPrompt or "UNIVERSITY OF VIRGINIA" in myPrompt or
              "SOUTHERN ILLINOIS" in myPrompt or "BA" in myPrompt or "MA" in myPrompt or "PHD" in myPrompt or "BACHELOR" in myPrompt or "MASTER" in myPrompt or "DOCTOR" in myPrompt):
            Enqueue([2, "Fun Fact: I got my BA at UVA and my MA/PhD in American Literature at Southern Illinois University."], 18)
        
        elif ("FILM" in myPrompt or "INTERIM" in myPrompt):
            Enqueue([2, "I highly recommend that you join either my film interim or film class... or both!"])
            
        elif ("HOBBIES" in myPrompt or "HOBBY" in myPrompt in myPrompt or "FUN" in myPrompt):
            Enqueue([2, "I like to play soccer, chess, and Scrabble."])
        
        elif ("CHINA" in myPrompt or "RESEARCH" in myPrompt or "DOCUMENTARY" in myPrompt):
            Enqueue([2, "I made a documentary in China during the 2019-2020 SPRI. Ask Dr. Newsome about it!"])
            
        elif ("HELLO" in myPrompt or "HI" in myPrompt or "HOWDY" in myPrompt or
              "HEY" in myPrompt or "GREETING" in myPrompt or "GOOD MORNING" in myPrompt or "GOOD AFTERNOON" in myPrompt or "GOOD EVENING" in myPrompt):
            Enqueue([2, "Hello User! Did you bring you remember to bring your red book today?"])
        
        elif ("BOOMER" in myPrompt):
            Enqueue([2, "Shouldn't you treat your elders with more respect?"])
            
        else:
            Option = random.randint(1, 10)
            if (Option == 1):
                FlannyText = 'Significant Pause!'
            elif (Option == 2):
                FlannyText = 'That will go into your portfolio.'
            elif (Option == 3):
                FlannyText = 'You do know that you have a reading response due Thursday, right?'
            elif (Option == 4):
                FlannyText = 'You should visit the writing center some time.'
            elif (Option == 5):
                FlannyText = 'Try reading the README file.'
            elif (Option == 6):
                FlannyText = "Don't be so dismissive of English literature."
            elif (Option == 7):
                FlannyText = 'Write that down!'
            elif (Option == 8):
                FlannyText = "Can I see you after class today to discuss your writing?"
            elif (Option == 9):
                FlannyText = 'Cheers!'
            elif (Option == 10):
                FlannyText = "Y'know my wife teaches at Francis Marion."
            
            Enqueue([2, FlannyText])
    else:
        Story = promptArr[1]
        Story = Story.replace(' ', '')
        Story = Story.upper()
        if (promptArr[0].upper() == 'SUMMARIZE'):
            if ('GATSBY' in Story):
                Enqueue([2, "Nick Carraway is a young man that recently moved to Manhattan's West Egg."])
                time.sleep(waitTime)
                Enqueue([2, "He meets a wealthy man named Jay Gatsby, who throws grand parties every night."])
                time.sleep(waitTime)
                Enqueue([2, "Gatsby uses these parties to lure his old love, Daisy, who lives in East Egg."])
                time.sleep(waitTime)
                Enqueue([2, "Nick helps Gatsby engage in an affair with Daisy, as she is already married."])
                time.sleep(waitTime)
                Enqueue([2, "Daisy's husband, Tom, has a mistress of his own, Myrtle, and Daisy drives over her."])
                time.sleep(waitTime)
                Enqueue([2, "Gatsby takes the fall for Daisy and is later killed by Myrtle's husband, George."])
                time.sleep(waitTime)
            
                
            elif ('OEDIPUS' in Story):
                Enqueue([2, 'Oedipus is the ruler of Thebes, which is currently going through a massive plague.'])
                time.sleep(waitTime)
                Enqueue([2, "An oracle tells Oedipus that he must punish whoever killed Laius, the former king, to lift the curse."], 18)
                time.sleep(waitTime)
                Enqueue([2, "Oedipus calls in the prophet Tiresias for guidance, but the prophet claims that Oedipus is the murderer."], 17)
                time.sleep(waitTime)
                Enqueue([2, "Oedipus's wife, Jocasta, enters and tells Oedipus about a prophecy that her son would commit patricide and incest."], 16)
                time.sleep(waitTime)
                Enqueue([2, "It turns out that Oedipus was that son, and that he really killed Laius and married his own mother."], 18)
                time.sleep(waitTime)
                Enqueue([2, "Distraught, Jocasta hangs herself and Oedipus gouges his eyes out using Jocasta's jewelry."], 19)
                time.sleep(waitTime)
            
            elif ('HAMLET' in Story):
                Enqueue([2, 'The Danish King has just died and the heir prince, Hamlet finds his ghost. The ghost claims that his brother, Claudius, poisoned him.'], 14)
                time.sleep(waitTime)
                Enqueue([2, "Hamlet tries to avenge his father by assassinating Claudius, so he feigns madness to his friends, family and even his lover, Ophelia."], 14)
                time.sleep(waitTime)
                Enqueue([2, 'Hamlet proves that Claudius is the killer by paying actors to re-enact the murder scene and force a reaction out of Claudius.'], 14)
                time.sleep(waitTime)
                Enqueue([2, "He then goes for the kill but mistakenly attacks Polonius, Claudius's right hand man. Hamlet is exiled (and almost executed) in England."], 14)
                time.sleep(waitTime)
                Enqueue([2, 'Hamlet returns to Denmark, but Ophelia drowns herself and her brother Laertes challenges Hamlet to a duel.'], 17)
                time.sleep(waitTime)
                Enqueue([2, "Claudius poisons Laertes's blade, but both fighters end up cut by it. Before dying, Hamlet takes the sword and kills Claudius."], 14)
                time.sleep(waitTime)
                
            elif ('ROMANFEVER' in Story):
                Enqueue([2, 'Two old women, Ms. Slade and Ms. Ansley, sit on the terrace of an Italian Restaurant.'])
                time.sleep(waitTime)
                Enqueue([2, 'Their daughters are set to be married soon, but Ms. Slade is jealous of Ms. Ansley\'s daughter, Barbara.'], 17)
                time.sleep(waitTime)
                Enqueue([2, 'An argument starts, and Ms. Slade reveals that 25 years ago, she wrote a letter (under the guise of her fiance, Delphin) to Ms. Ansley.'], 13)
                time.sleep(waitTime)
                Enqueue([2, 'The letter told Ms. Ansley to meet Delphin at the Colosseum, where she would find no one there and get exposed to Malaria.'], 14)
                time.sleep(waitTime)
                Enqueue([2, 'However, Ms. Ansley had replied back to the letter, and Delphin ended up meeting at the Colosseum.'], 18)
                time.sleep(waitTime)
                Enqueue([2, 'Ms. Slade is flustered, but remarks that she had Delphin for 25 years, only for Ms. Ansley to remark that she "had Barbara."'], 14)
                time.sleep(waitTime)
                
            elif ('SWEAT' in Story):
                Enqueue([2, 'Delia is a washerwoman in Florida. Her husband, Sykes, is unemployed and abusive.'])
                time.sleep(waitTime)
                Enqueue([2, 'Delia has a phobia of snakes, and Sykes exploits that fear by getting one of his own.'])
                time.sleep(waitTime)
                Enqueue([2, 'Delia and Sykes eventually split up, and Sykes decides to make a new life with his mistress, Bertha.'], 18)
                time.sleep(waitTime)
                Enqueue([2, 'Sykes then plots to kill Delia by putting a rattlesnake in her washing basket, but the snake attacks him instead.'], 16)
                time.sleep(waitTime)
                Enqueue([2, 'As Sykes dies from the poison, he screams in agony and begs for Delia, who sits under a tree and ignores him.'], 16)
                time.sleep(waitTime)
            
            elif ('ROSEFOREMILY' in Story):
                Enqueue([2, 'An old woman, Emily Grierson, has recently died. She was very strange, as she was reclusive and had an odd past.'], 15)
                time.sleep(waitTime)
                Enqueue([2, 'When her father died thirty years prior, she would not give up the body, claiming that he was still alive and well.'], 15)
                time.sleep(waitTime)
                Enqueue([2, 'After a while, Emily falls in love with a gay northerner named Homer Barron. They start an affair together.'], 17)
                time.sleep(waitTime)
                Enqueue([2, 'Strangely, Emily goes to the druggist to buy some Arsenic "for rats." After this purchase, the affair falls apart.'], 15)
                time.sleep(waitTime)
                Enqueue([2, 'Homer enters Emily\'s house one evening and is never seen again. Ever since, no strangers were allowed in her house.'], 15)
                time.sleep(waitTime)
                Enqueue([2, 'At her funeral, the curious townspeople find a secret room. There, they find Homer\'s dead body on a bed, with Emily\'s hair next to him.'], 13)
                time.sleep(waitTime)
            
            else:
                Enqueue([2, "I do not have that Book/Character/Author in memory right now. Blame Rajat."])
                
        elif (promptArr[0].upper() == 'ANALYZE'):
            if ("VALLEY" in Story or "ASHES" in Story):
                Enqueue([2, 'The Valley of Ashes is a desolate wasteland between West Egg and NYC.'])
                time.sleep(waitTime)
                Enqueue([2, 'It represents how morality decays in the presence of money.'])
                time.sleep(waitTime)
                Enqueue([2, 'Like how an industry can destroy nature for profits, the rich indulge themselves without respect for others.'], 16)
                time.sleep(waitTime)
                Enqueue([2, 'It also symbolizes the plight of the poor, like how the Wilsons live in dirty and hopeless conditions.'], 18)
                time.sleep(waitTime)
                Enqueue([2, 'Living in such environmental hazard is bound to cause damage, such as when Myrtle dies and when George goes mad.'], 15)
                time.sleep(waitTime)

                
            elif ("OPHELIA" in Story):
                Enqueue([2, 'Ophelia is a representation of misogny and expected submissiveness.'])
                time.sleep(waitTime)
                Enqueue([2, 'Throughout the play, she must deal with the desires of three men, Polonius, Hamlet, and Laertes.'], 18)
                time.sleep(waitTime)
                Enqueue([2, 'In Act One, Laertes and Polonius admonish her love for Hamlet and his madness.'])
                time.sleep(waitTime)
                Enqueue([2, 'In Act Three, Hamlet\'s "madness" leads to a misogynistic rant, validating Polonius\'s views.'])
                time.sleep(waitTime)
                Enqueue([2, 'When Hamlet kills Polonius, it\'s the last straw. Her lover has gone insane and her father is dead.'], 18)
                time.sleep(waitTime)
                Enqueue([2, 'She is powerless to control Hamlet and incapable of protecting her father, as she loses her innocence and her life.'], 15)
                time.sleep(waitTime)
                
            elif ("ARABY" in Story):
                Enqueue([2, '"Araby" is mostly a "Coming of Age" story, where the narrator grows mentally and sexually.'])
                time.sleep(waitTime)
                Enqueue([2, 'The narrator does not want to be treated like a child but rather as a full-grown adult.'])
                time.sleep(waitTime)
                Enqueue([2, 'He shifts his attention from his younger friends to Mangan\'s older sister, for his interests are shifting with adolescence.'], 14)
                time.sleep(waitTime)
                Enqueue([2, 'On the subject of Mangan\'s sister, the story is also a representation of religion and blind following.'], 18)
                time.sleep(waitTime)
                Enqueue([2, 'The narrator has made a "Church of Mangan\'s Sister," where her body is a "chalice" worth praying to."'], 18)
                time.sleep(waitTime)
                Enqueue([2, 'As many teenagers tend to do, the narrator is forsaking God for his materialistic desires and sexuality.'], 18)
                time.sleep(waitTime)
            
            elif ("SECONDCOMING" in Story):
                Enqueue([2, '"The Second Coming" represents how the world is falling apart and humanity may collapse.'])
                time.sleep(waitTime)
                Enqueue([2, 'In Christianity, the Second Coming of Christ symbolizes God\'s last judgment... and the End of the World.'], 17)
                time.sleep(waitTime)
                Enqueue([2, 'When this poem was written, it was after World War I and the Spanish Flu Outbreak.'])
                time.sleep(waitTime)
                Enqueue([2, 'In Yeats\' eyes, the world is collapsing and "the centre cannot hold."'])
                time.sleep(waitTime)
                Enqueue([2, 'The second stanza of the poem takes a religious undertone to the world\'s situation, like a biblical apocalypse.'], 17)
                time.sleep(waitTime)
                Enqueue([2, 'With the deaths of millions of people, it feels like some slow, demonic creature is wreaking havoc on Earth.'], 17)
                time.sleep(waitTime)
                
                
            else:
                Enqueue([2, "I do not have that Book/Character/Author in memory right now. Ask Rajat."])
                
        else:
            Enqueue([2, "I did not understand your instruction. Try again."])    
                  
def Enqueue(info, textSize = 20):
    global RectList
    global TextQueue    
    
    if (len(TextQueue) == 6):
        TextQueue.pop(0)
        for i in range(len(TextQueue)):
            prevText = TextQueue[i][1].getText()
            prevOwner = TextQueue[i][0]
            prevTextSize = TextQueue[i][2]
            TextQueue[i][1].undraw()
            newText = Text(RectList[i].getCenter(), prevText)
            TextQueue[i] = [prevOwner, newText, prevTextSize]
    
    myText = Text(RectList[len(TextQueue)].getCenter(), info[1])
    
    if (info[0] == 1):
        print("USER: " + str(info[1]))
    else:
        print("Dr. FlannaganBot: " + str(info[1]))
    
    TextQueue.append([info[0], myText, textSize])
    UpdateText()
    

def UpdateText():
    global RectList
    global TextQueue
    
    for i in RectList:
        i.undraw()
    
    for i in TextQueue:
        i[1].undraw()
    
    for i in range(len(TextQueue)):
        TextQueue[i][1].setSize(TextQueue[i][2])
        if (TextQueue[i][0] == 1): #User Speak
            RectList[i].setFill('white')
        elif (TextQueue[i][0] == 2): #Flanny Speak
            RectList[i].setFill('green2')
            
        RectList[i].draw(win)
        TextQueue[i][1].draw(win)

width = 1400
height = 1000
gap = 30
rectWidth = width - gap
rectHeight = 60
waitTime = 2.5
textSize = 20

win = GraphWin("Flannagan ChatBot", width, height)

background = Image(Point(width / 2, height / 2), 'Background.png')
background.draw(win)

Flanny = Image(Point(width / 2, 150), 'Flanny.png')
Flanny.draw(win)

DivPoint = Flanny.getAnchor().getY() + Flanny.getHeight() / 2
DivLine = Line(Point(0, DivPoint), Point(width, DivPoint))
DivLine.setWidth(10)
DivLine.setOutline('red')
DivLine.draw(win)

Rect1 = Rectangle(Point(gap, DivPoint + gap), Point(rectWidth, DivPoint + gap + rectHeight))
Rect2 = Rectangle(Point(gap, DivPoint + 2 * gap + rectHeight), Point(rectWidth, DivPoint + 2 * gap + 2 * rectHeight))
Rect3 = Rectangle(Point(gap, DivPoint + 3 * gap + 2 * rectHeight), Point(rectWidth, DivPoint + 3 * gap + 3 * rectHeight))
Rect4 = Rectangle(Point(gap, DivPoint + 4 * gap + 3 * rectHeight), Point(rectWidth, DivPoint + 4 * gap + 4 * rectHeight))
Rect5 = Rectangle(Point(gap, DivPoint + 5 * gap + 4 * rectHeight), Point(rectWidth, DivPoint + 5 * gap + 5 * rectHeight))
Rect6 = Rectangle(Point(gap, DivPoint + 6 * gap + 5 * rectHeight), Point(rectWidth, DivPoint + 6 * gap + 6 * rectHeight))

RectList = [Rect1, Rect2, Rect3, Rect4, Rect5, Rect6]
TextQueue = []

inputBox = Entry(Point(width / 2.5, (2 * DivPoint + 14 * gap + 13 * rectHeight) / 2), 50)
inputBox.setFill('gold')
inputBox.setSize(24)
inputBox.draw(win)

Enter = Rectangle(Point(width * 5 / 6.12, DivPoint + 6.5 * gap + 6 * rectHeight), Point(rectWidth, DivPoint + 7.5 * gap + 7 * rectHeight))
Enter.setFill('black')
Enter.draw(win)

EnterText = Text(Enter.getCenter(), 'Submit!')
EnterText.setStyle('bold')
EnterText.setTextColor('white')
EnterText.setSize(26)
EnterText.draw(win)

Exit = Rectangle(Point(gap, gap), Point(gap + 120,  2 * gap + rectHeight))
Exit.setFill('red4')
Exit.draw(win)

ExitText = Text(Exit.getCenter(), 'Exit!')
ExitText.setStyle('bold')
ExitText.setTextColor('white')
ExitText.setSize(26)
ExitText.draw(win)

print("CHAT HISTORY: ")
time.sleep(waitTime)
Enqueue([2, "My name is Dr. FlannaganBot. I am an English teacher at GSSM."])
time.sleep(waitTime)
Enqueue([2, "Ask me to summarize or analyze a few books/stories (Check README File)"])
time.sleep(waitTime)
Enqueue([2, "If I do not have a book in memory or my code malfunctions, talk to Rajat."])

while (True):
    NoOptionPicked = True
    ExitBot = False
    while (NoOptionPicked):
        CP = win.getMouse()
        if (CP.getX() >= Enter.getP1().getX() and CP.getX() <= Enter.getP2().getX() and CP.getY() >= Enter.getP1().getY() and CP.getY() <= Enter.getP2().getY()):
            inputText = inputBox.getText()
            inputBox.setText('')
            Enqueue([1, inputText])
            Respond(inputText)
            NoOptionPicked = False
        
        if (CP.getX() >= Exit.getP1().getX() and CP.getX() <= Exit.getP2().getX() and CP.getY() >= Exit.getP1().getY() and CP.getY() <= Exit.getP2().getY()):
            NoOptionPicked = False
            ExitBot = True
    
    if (ExitBot):
        win.close()
        break
        
        

    



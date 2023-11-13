# #CS 223 Final Project-First Draft.V1
# #Created by Caleb Brown on 3 March 2023
# #
# #  This project was built and inpired by 3 different versions for the same concept as follows:
# #
# #    https://www.geeksforgeeks.org/color-game-python/
# #    https://www.makeuseof.com/build-color-game-using-tkinter-python/?newsletter_popup=1 by SAI Ashish Konchada
# #    https://www.tutorialspoint.com/color-game-using-tkinter-in-python by Karthikeya Boyini
# #
# #    This program is a simple text and color type game where the player(single) attempts to correctly type
# #    the corresponding font color of the word presented and not the actual name of word. There will also be a
# #    separate class/module built as a scoreboard or list of high scores which are passed between the main and itself.
#======================================================================================================================
#======================================================================================================================

import tkinter
import random
from HighScore import HighScore

# Constants for program, colors is pretty self explained but will consist of a library of colors used in game.
colors = ['Red','Blue','Green','Pink','Black','Yellow','Cyan','Orange','Purple','White']

score = 0

timeleft = 25

# Calling on and assigning variable for high score from separate class/module 'HighScore'
high_score = HighScore()

# # This function(main) defines beginning of game, recognizes game timer as default setting, thus starts countdown function
# # followed by function for selecting next color.
def main(event):

    if timeleft == 25:

        countdown()

    next_color()
    

# # The next color function(next_color) uses global values for score and time remaing in game to know if and when it will
# # display the next color.
def next_color():


    global score
    global timeleft

    # As long as timer is greater than 0 than it will display teh next color.
    if timeleft > 0:

        # Activates the widget for text entry.
        e.focus_set()

        # This line is validating whether or not user input equals font color displayed, if correct then plus 1 score.
        if e.get().lower() == colors[1].lower():

            # Will tally score plus 1 for every correct answer, then adds it to high score list.
            score += 1
            high_score.add_score(score)
            
        # Clears current Text/Color
        e.delete(0, tkinter.END)
        
        # Randomly chooses next Text/Color
        random.shuffle(colors)

        # This line is swapping the color and text to a random value from [list]
        label.config(fg = str(colors[1]), text = str(colors[0]))

        # Updates and stores current Score
        scoreLabel.config(text = "Score: " + str(score))


# This function(countdown) is defining the rules for time allowed to play based on the global variable for time(timeleft).
def countdown():

    global timeleft

    # Simple counter(down) that tracks timer to 0. If statement decides whther game continues or not.
    if timeleft > 0:


        timeleft -= 1

        # Label that displays time that is remaining.
        timeLabel.config(text = "Time left: "
                            + str(timeleft))

        # This line uses 'after' method, which essentially loops this function every 1 second(1000 milliseconds)
        # until timer ends.
        timeLabel.after(1000, countdown)


# Assigns 'menu' as tkinter.Tk(), makes lines of code slightly shorter/easier to understand.
menu = tkinter.Tk()

# setting title of game.
menu.title("HIT OR MISS!")

# Setting size of window for which game is played in.
menu.geometry("600x400")

# Short description of rules for game. Using concatenation in formatting the text.
instructions = tkinter.Label(menu, text = "Type in the color"
                        " of the words, and not the word text, or else!",
                                    font = ('Helvetica', 12))
instructions.pack()

# Building score label, also prompts user on how to start game.
scoreLabel = tkinter.Label(menu, text = "Press enter to start",
                                    font = ('Helvetica', 12))
scoreLabel.pack()

# High score label
highScoreLabel = tkinter.Label(menu, text="High Scores: " + str(high_score.get_high_scores()), font=('Helvetica', 12))

highScoreLabel.pack()

# Building time label with alternate format using f-string with variables built into text string.
timeLabel = tkinter.Label(menu, text=f"Time left: {timeleft}", font=('Helvetica', 12))

timeLabel.pack()

# This portion displays the word for solving, in a bigger font of course.
label = tkinter.Label(menu, font = ('Helvetica', 60))
label.pack()

# This is the portion or entry box where the players input goes. Reassigning longer input to short simple 'e' variable.
e = tkinter.Entry(menu)

# Upon pressing 'Enter' to start game, this line will begin the (start_game) function
menu.bind('<Return>', main)
e.pack()

# This line allows us to set the 'e' widget as the focus, so once the player presses enter, it will
# set the focus of user input into the box where the player types in their answers instead of having to click on the box
# every time they enter in a guess.
e.focus_set()


menu.mainloop()

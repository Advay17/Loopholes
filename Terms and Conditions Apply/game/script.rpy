﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Saul Goodman")

# The game starts here.
label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    screen buttons():
        frame:
            xalign 0.5 yalign 1.0
            button:
                action Notify(_("You clicked the button."))
                text _("Click me.") style "button_text" ## TODO change style
            button:
                action Notify(_("You clicked the button."))
                text _("Click me.") style "button_text" ## TODO change style
            # button:
            #     action Notify(_("You clicked the button."))
            #     text _("Click me.") style "button_text" ## TODO change style
            # button:
            #     action Notify(_("You clicked the button."))
            #     text _("Click me.") style "button_text" ## TODO change style
    scene advay house
    show screen buttons
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show saul goodman

    # These display lines of dialogue.

    e "I'm Saul Goodman."

    e "Do you know that you have rights?" with vpunch

    # This ends the game.

    return

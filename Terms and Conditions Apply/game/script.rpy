# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Saul Goodman")
define j = Character("Justin Case", adv, image="Justin")
define p = Character("You", name_only)
define c = Character("Courtney Case", adv, image="Courtney")
define jc = Character("Justin Case", adv, image="JustinCourt")
define pc = Character("You", adv, image="Player")
define pr = Character("Prosecutor", adv, image="Prosecutor")
define d = Character("Detective", adv, image="Detective")
define r = Character("Ruby Stone", adv, image="Stone")
# The game starts here.
label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene advay house
    show screen under_menu
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show saul goodman

    s "I'm saul goodman."
    s "Do you know you have rights? {w=0.1}Well, the constitution says you do.§ 34-1"
    # These display lines of dialogue.



    return

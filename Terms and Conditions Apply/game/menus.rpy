##Screen containing all the buttons in the quick menu
screen under_menu():
    frame:
        xalign 0.5 
        yalign 1.0

        has hbox

        textbutton "Documents":
            style "quick_menu_button"
            action Notify("You clicked the button.")

        textbutton "Characters":
            style "quick_menu_button"
            action Notify("You clicked the other button.")
        textbutton "Loophole":
            style "quick_menu_button"
            action Notify("You clicked the other button.")
        textbutton "History":
            style "quick_menu_button"
            action ShowMenu("history")

style quick_menu_button:
    # idle_background Frame("slot idle background", 12, 12)
    # hover_background Frame("slot hover background", 12, 12)
    xpadding 20
    ypadding 10
    xmargin 5
    ymargin 5
    size_group "quick_menu_button"

style quick_menu_button_text:
    idle_color "#c0c0c0"
    hover_color "#ffffff"

screen documents():
    pass


# screen 
 
##Screen containing all the buttons in the quick menu
init python:
    class Document():
        def __init__(self, name, desc, img):
            self.name=name
            self.desc=desc
            self.img=img
    pass
define luggage = Document("Badge", "Proof that you are indeed a lawyer, even though you are in America, which doesn't use these.", "badge")
define knife = Document("Knife", "A butter knife, must be a slow death.", "saul goodman")
default document_list=[luggage, knife]
screen under_menu():
    frame:
        xalign 0.5 
        yalign 1.0

        has hbox

        textbutton "Documents":
            style "quick_menu_button"
            action Show("documents")
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
    frame:
        background "black"
        xalign 0.5
        yalign 0.5
        vpgrid:
            ysize 800
            scrollbars "vertical"
            spacing 5
            draggable True
            mousewheel True
            cols 1
            side_xalign 0.0
            for document in document_list:
                button:
                    hovered background "red"
                    action Notify("You clicked the other button.")
                    hbox:
                        add document.img
                        vbox:
                            text document.name
                            text document.desc
        pass


# screen 
 
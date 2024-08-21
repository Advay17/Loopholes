
##Screen containing all the buttons in the quick menu
default notepad_text=""
init python:
    class Document():
        def __init__(self, name, desc, sub_text, img):
            self.name=name
            self.desc=desc
            self.sub_text=sub_text
            self.img=img
    pass
    class CharacterData():
        def __init__(self, name, desc, img):
            self.name=name
            self.desc=desc
            self.img=img
    class RuleDocument(Document):
        def __init(self, name, desc, sub_text, img, rules):
            self.name=name
            self.desc=desc
            self.sub_text=sub_text
            self.img=img
            self.rules=rules
define pov = Character("[povname]")

define badge = Document("Badge", "Proof that you are indeed a lawyer, even though you are in America, which doesn't use these.", "Literally just a badge. You don't know why it's with the other documents.", "badge")
default document_list=[badge]
define saul_goodman = CharacterData("Saul Goodman", "Better, call, Saul. Better, call, Saul. Better, call, Saul.", "jimmy")
default character_list = [saul_goodman]
screen under_menu():
    zorder 50
    frame:
        xalign 0.5 
        yalign 1.0

        has hbox
        textbutton "Documents":
            style "quick_menu_button"
            action [Hide("under_menu"), Show("documents")]
        textbutton "Characters":
            style "quick_menu_button"
            action [Hide("under_menu"), Show("characters")]
        textbutton "Loophole":
            style "quick_menu_button"
            action [Hide("under_menu"), Show("loophole")]
        textbutton "History":
            style "quick_menu_button"
            action ShowMenu("history")
        textbutton "Notepad":
            style "quick_menu_button"
            action [Hide("under_menu"), Show("notepad")]

style quick_menu_button:
    # idle_background Frame("slot idle background", 12, 12)
    # hover_background Frame("slot hover background", 12, 12)
    xpadding 20
    ypadding 10
    xmargin 5
    ymargin 5
    size_group "quick_menu_button"
    idle_color "#c0c0c0"
    hover_color "#ffffff"
style gameplay_menu_button:
    # idle_background Frame("slot idle background", 12, 12)
    # hover_background Frame("slot hover background", 12, 12)
    xpadding 20
    ypadding 10
    xmargin 5
    ymargin 5
    size_group "quick_menu_button"
    idle_color "#c0c0c0"
    hover_color "#ffffff"
style quick_menu_button_text:
    idle_color "#c0c0c0"
    hover_color "#ffffff"
style gameplay_menu_button_text:
    idle_color "#c0c0c0"
    hover_color "#ffffff"
style gameplay_menu:
    background "black"
    xalign 0.5
    yalign 0.5
    xsize 1600
    ysize 890
    
    
screen documents():
    modal True
    zorder 50
    frame:
        style "gameplay_menu"
        vbox:

            hbox:
                frame:
                    xsize 1400
                    ysize 90
                    style "gameplay_menu_button"
                    text "Documents"
                    xalign 0.5
                frame:
                    # xalign -0.182 #don't know why this specific value makes it work, but it does.
                    xsize 200
                    xalign 0.9
                    textbutton "Exit":
                        ysize 90
                        style "gameplay_menu_button"
                        action [Hide("documents"), Show("under_menu")]
            frame:
                ysize 800
                vpgrid:
                    if len(document_list)>5:
                        scrollbars "vertical"
                    spacing 5
                    draggable True
                    mousewheel True
                    cols 1
                    side_xalign 0.0
                    for document in document_list:
                        button:
                            xsize 1600
                            background "#000000"
                            hover_background "#FF0000"
                            action Show("document_info", None, document.name, document.sub_text)
                            hbox:
                                add document.img
                                vbox:
                                    text document.name
                                    text document.desc
        pass
screen document_info(name, sub_text):
    modal True
    zorder 51
    frame:
        style "gameplay_menu"
        vbox:
            hbox:
                textbutton "Back":
                    xsize 200
                    ysize 90
                    style "gameplay_menu_button"
                    action Hide("document_info")
                frame:
                    xsize 1200
                    ysize 90
                    style "gameplay_menu_button"
                    text "Documents"
                    
                textbutton "Exit":
                    xsize 200
                    ysize 90
                    style "gameplay_menu_button"
                    action [Hide("documents"), Hide("document_info"), Show("under_menu")]
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                frame:
                    text sub_text
        pass
screen loophole():
    modal True
    zorder 50
    frame:
        style "gameplay_menu"
        vbox:
            xsize 1600
            hbox:
                frame:
                    xsize 1400
                    ysize 90
                    style "gameplay_menu_button"
                    text "Select a Document"
                    xalign 0.5
                frame:
                    # xalign -0.182 #don't know why this specific value makes it work, but it does.
                    xsize 200
                    xalign 0.9
                    textbutton "Exit":
                        ysize 90
                        style "gameplay_menu_button"
                        action [Hide("loophole"), Show("under_menu")]
            frame:
                ysize 720
                vpgrid:
                    if len(document_list)>5:
                        scrollbars "vertical"
                    spacing 5
                    draggable True
                    mousewheel True
                    cols 1
                    side_xalign 0.0
                    for document in document_list:
                        button:
                            xsize 1600
                            background "#000000"
                            hover_background "#FF0000"
                            action Notify("Document selected")
                            hbox:
                                add document.img
                                vbox:
                                    text document.name
                                    text document.desc
            textbutton "Confirm?":
                xalign 0.5
                style "gameplay_menu_button"
                action Notify("Document confirmed")
screen characters():
    modal True
    zorder 50
    frame:
        style "gameplay_menu"
        vbox:
            hbox:
                frame:
                    xsize 1400
                    ysize 90
                    style "gameplay_menu_button"
                    text "Documents"
                    xalign 0.5
                frame:
                    # xalign -0.182 #don't know why this specific value makes it work, but it does.
                    xsize 200
                    xalign 0.9
                    textbutton "Exit":
                        ysize 90
                        style "gameplay_menu_button"
                        action [Hide("characters"), Show("under_menu")]
            frame:
                vpgrid:
                    rows 1
                    if len(character_list)>5:
                        scrollbars "horizontal"
                    spacing 5
                    draggable True
                    mousewheel "horizontal"
                    for character in character_list:
                        vbox:
                            add character.img
                            frame:
                                yalign -0.6
                                xalign 0.5
                                text character.name
                            frame:
                                yalign -0.4
                                xalign 0.5
                                text character.desc
                            xsize 183
                            ysize 788
screen notepad():
    modal True
    zorder 50
    frame:
        style "gameplay_menu"
        vbox:
            hbox:
                frame:
                    xsize 1400
                    ysize 90
                    style "gameplay_menu_button"
                    text "Notepad"
                    xalign 0.5
                frame:
                    # xalign -0.182 #don't know why this specific value makes it work, but it does.
                    xsize 200
                    xalign 0.9
                    textbutton "Exit":
                        ysize 90
                        style "gameplay_menu_button"
                        action [Hide("notepad"), Show("under_menu"), Notify(notepad_text)]
            frame:
                xsize 1600
                ysize 980
                input:
                    idle_color "#c0c0c0"
                    hover_color "#ffffff"
                    value VariableInputValue("notepad_text", returnable=True)
                    copypaste True
                    multiline True
                    # layout "greedy"
                key "input_enter" action If(renpy.get_screen("documents"), true=NullAction() )
                    # python:
                    #     pass
                    

        




# screen 
 
screen buttons2():
    hbox:
        xalign 0.5 yalign 1.0
        button :
            action [Hide("button2s")]
            text _("Loophole Found") 
            style "button_text" ## TODO change style
        button:
            action [Hide("buttons2")]
            text _("Documents") 
            style "button_text" ## TODO change style
        button:
            action [Hide("buttons2")]
            text _("Characters") 
            style "button_text" ## TODO change style


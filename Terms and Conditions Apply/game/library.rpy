# init python:
#     pass
# define library_document_list=[Document("Badge", "Proof that you are indeed a lawyer, even though you are in America, which doesn't use these.", "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. ", "badge")]
# default search_term = ""
# label library:
#     scene library main
#     show library_interactives

# screen library_interactives:
#     frame:
#         background "library"
#         hbox:
#             #computer
#             vbox:
#                 input:
#                     idle_color "#c0c0c0"
#                     hover_color "#ffffff"
#                     copypaste True
#                     layout "greedy"
#                     pixel_width 1592 #need to test this
#                     value VariableInputValue("search_term", returnable=True)
#                 viewport:
#                     pass
#                     # rows 1
        


            
from ipy_lib import SnakeUserInterface

#add the following statement before any other statement relating to the input:
#x = file_input()




#create GUI object
WIDTH = 40
HEIGHT = 30
SCALE = 0.5
ui = SnakeUserInterface(WIDTH, HEIGHT, SCALE)




ui = SnakeUserInterface(5,5) # 5 by 5 grid for testing purposes
your_variable = ui.get_event() # code will block untill an event comes
# your_variable now points to an event
print your_variable.name, your_variable.data



while True : # infinite loop
    event = ui.get_event()
    #process_event(event)



#def process_event(event) :
    #if event.name == "click" :
        #process_click(event.data)
    #elif event1 : process_event1(event.data)
    #elif (event2) : process_event2(event.data)

while True : # infinite loop
    event = ui.get_event()
    #process_event(event)

















#keep window open after code finishes
ui.stay_open()
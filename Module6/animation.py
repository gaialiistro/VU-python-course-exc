from ipy_lib import SnakeUserInterface
import matplotlib
matplotlib.use('PS')


ui = SnakeUserInterface(5,5) # 5 by 5 grid for testing purposes
your_variable = ui.get_event() # code will block untill an event comes
# your_variable now points to an event
print your_variable.name, your_variable.data



while True : # infinite loop
    event = ui.get_event()
    #process_event(event)


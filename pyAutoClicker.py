# Imports nessecary modules
try: 
   import pyautogui
   import keyboard
   import threading
except:
   import pip
   pip.main(['install', 'pyautogui'])
   pip.main(['install', 'keyboard'])
   import pyautogui
   import keyboard

# Actual Program

def autoClick():
   while True:
      pyautogui.click()
      
      # Toggles the autoclicker once 'c' is pressed on the keyboard
      if keyboard.is_pressed('c'):
         break

   
if __name__ =="__main__":

   # Prepares threads for multi-threading
   t1 = threading.Thread(target=autoClick)
   t2 = threading.Thread(target=autoClick)
   t3 = threading.Thread(target=autoClick)
   t4 = threading.Thread(target=autoClick)
   t5 = threading.Thread(target=autoClick)
   
   while True:
      if keyboard.is_pressed('c'):

         # Toggles the autoclicker once 'c' is pressed on the keyboard
         t1.start()
         t2.start()
         t3.start()
         t4.start()
         t5.start()
         
         # Joins threads so the alert message only pops up after the threads are exited
         t1.join()
         t2.join()
         t3.join()
         t4.join()
         t5.join()
         pyautogui.alert('The autoclicker has been stopped.')
         
         # Redefines threads so they can be started a second time
         t1 = threading.Thread(target=autoClick)
         t2 = threading.Thread(target=autoClick)
         t3 = threading.Thread(target=autoClick)
         t4 = threading.Thread(target=autoClick)
         t5 = threading.Thread(target=autoClick)
# Imports nessecary modules
try: 
   import pyautogui
   import keyboard
except:
   import pip
   pip.main(['install', 'pyautogui'])
   pip.main(['install', 'keyboard'])
   import pyautogui
   import keyboard

# Actual Program

while True:
   if keyboard.is_pressed('c'):
      while True:
         pyautogui.click()
         
         if keyboard.is_pressed('c'):
            pyautogui.alert('The autoclicker has been stopped.')
            break       

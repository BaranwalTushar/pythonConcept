import pyautogui
import time
import pyperclip

# click on the chrome icon at coordinates (1639, 1412)
pyautogui.click(518, 258)
time.sleep(1)

# Drag the mouse from (1003,237) to (2187, 1258) to select the text 
pyautogui.moveTo(992,207)
pyautogui.dragTo(1290,872, duration=1.0, button='left') #drag for 1 second

#copy the selected text to clipboard
pyautogui.hotkey('ctrl','c')
time.sleep(1) #wait for 1 second to ensure the copy command is complete 

text = pyperclip.paste()

#print the copied text to verify
print(text)
import pyautogui, time

time.sleep(6)

workouts = [input("Enter the name of the workout") for i in range(5)]
print(workouts)
locations = [[634, 976], [765, 985], [902, 982], [1036, 986], [1158, 978]]
count = 0

for location in locations:
    pyautogui.moveTo(location[0], location[1])
    time.sleep(2)
    pyautogui.click(button="left")
    time.sleep(1)
    pyautogui.moveTo(830, 775)
    pyautogui.click(button='left')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey("ctrl", "x")

    pyautogui.click(button='left')
    pyautogui.moveTo(285, 434)
    time.sleep(1)
    pyautogui.click(button="left")
    time.sleep(1)
    pyautogui.moveTo(1087, 573)
    time.sleep(1)
    pyautogui.click(button="left")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite(workouts[count])
    count+=1


#download 
time.sleep(2)
pyautogui.moveTo(1805, 161)
pyautogui.click(button='left')
time.sleep(4)
pyautogui.moveTo(1600, 634)
pyautogui.click(button='left')
time.sleep(4)
pyautogui.moveTo(1650, 594)
pyautogui.click(button='left')



# time.sleep(4)
# print(pyautogui.position())
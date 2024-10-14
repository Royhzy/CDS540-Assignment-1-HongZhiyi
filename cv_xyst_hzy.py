import sys
import cv2
import numpy as np
import pytesseract
import pyautogui   #Script
import keyboard   #Detecting key execution events
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Administrator\AppData\Local\Tesseract-OCR\tesseract.exe'
not_found_count = 0

# Display image
#Due to the dynamic recognition of this program, this function is only used for testing purposes
def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Pyautogui screenshot
def capture_area():
    region = (1505, 245, 195, 85)  #（x,y,width,height）
    screenshot = pyautogui.screenshot(region=region)
    return np.array(screenshot)


#image processing
#Make the image easy to recognize through gray processing and binary processing, and then convert the image into an array using pyteseract.image_to_ststing
def image_processing(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #gray processing
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)   #Binarization processing
    text = pytesseract.image_to_string(thresh, config='--psm 6')   #Identifying Numbers
    numbers = [int(s) for s in text.split() if s.isdigit()]   #.isdigit()  is used to detect whether a string is composed only of numbers
    return numbers


#Compare numbers
#Output the result of '>' or '<' to the corresponding function
def comparison(numbers):
    global not_found_count
    origin_x, origin_y = 250, 650 # Mark the regional coordinates to prevent output to PyCharm
    size = 50

    if len(numbers) < 2:         #Determine whether the question has been identified
        not_found_count += 1
        print(str(not_found_count)+"Unrecognized question")
        if not_found_count >= 25:
            print("next round...")
            pyautogui.click(1620, 520)  # click“开心收下” button
            #exit()

            #If you want to automatically proceed to the next round, here we choose to recognize text to meet the requirements of the assignment
            time.sleep(2)
            pyautogui.click(1721, 974)  # click“继续”button
            time.sleep(2)
            pyautogui.click(1656, 836)  # click“继续PK”button
            time.sleep(13)
            print("restart process")
            not_found_count=0
            time.sleep(0.3)
            main()

        return

    first, second = numbers[0], numbers[1]
    if first > second:
        print(f"{first} > {second}")
        greater_than(origin_x, origin_y, size)
        not_found_count = 0
    elif first < second:
        print(f"{first} < {second}")
        less_than(origin_x, origin_y, size)
        not_found_count = 0


#The result is to input '.' into the simulator through pyautogui.press
def greater_than(origin_x, origin_y, size):
    pyautogui.press(".")  # BlueStacks Script Manager, When Greater Than Number print "."

#The result is to input ',' into the simulator through pyautogui.press
def less_than(origin_x, origin_y, size):
    pyautogui.press(",")  # BlueStacks Script Manager, When Less Than Number print ","


def main():
    while True:
        image = capture_area()
        numbers = image_processing(image)
        comparison(numbers)
        time.sleep(0.5)  # Delay 0.5s for each recognition


if __name__ == "__main__":     #Determine whether the current script has been directly executed. If the script is run directly, execute the main() function.
    main()
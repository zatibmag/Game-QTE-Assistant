import cv2
import pyautogui
import numpy as np

# Function to check the presence of a white 5x5 area
def find_white_area(image):
    height, width = image.shape[:2]  # Using the first two values
    for y in range(height - 4):
        for x in range(width - 4):
            area = image[y:y+5, x:x+5]
            if np.all(area == 255):
                return (x, y)
    return None

previous_white_area = None

while True:
    # Capture the screen screenshot
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_GRAY2BGR)

    screenshot = screenshot[450:600, 875:1030]

    # Check the presence of a white 5x5 area
    white_area = find_white_area(screenshot)
    print(white_area, "1")
    print(previous_white_area, "2 ")
    if white_area == None and previous_white_area != None:
        pyautogui.press('space')
    previous_white_area = white_area

    cv2.imshow("photo", screenshot)

    # Wait for 100 milliseconds
    if cv2.waitKey(10) == ord('q'):
        break

cv2.destroyAllWindows()

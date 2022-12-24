import pyautogui
import cv2
import pytesseract
import numpy as np

def ocr_text(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to perform OCR on the image
    text = pytesseract.image_to_string(gray_image, config='--psm 7')

    # Extract only the digits from the OCR result
    digits = ''.join(c for c in text if c.isdigit())

    return digits

# Take a screenshot of the current screen
image = pyautogui.screenshot()

# Convert the image to a numpy array
image = np.array(image)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use OpenCV's template matching function to find card images in the screenshot
template = cv2.imread('1.png', 0)
result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)

# Use a threshold to identify locations with a high match score
threshold = 0.95
locations = np.where(result >= threshold)

# Loop through the identified locations and print the coordinates and number of the matching card images
for pt in zip(*locations[::-1]):
    # Extract the card image from the screenshot
    x, y = pt
    card_image = image[y:y+template.shape[0], x:x+template.shape[1]]

    # Use OCR to extract the digits from the card image
    digits = ocr_text(card_image)

    # Print the coordinates and number of the card
    print(f'Card found at x={x}, y={y}: {digits}')
    pyautogui.click(x,y)


"""import pyautogui
import cv2
import numpy as np

# Take a screenshot of the current screen
image = pyautogui.screenshot()

# Convert the image to a numpy array
image = np.array(image)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use OpenCV's template matching function to find card images in the screenshot
template = cv2.imread('1.png', 0)
result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)

# Use a threshold to identify locations with a high match score
threshold = 0.8
locations = np.where(result >= threshold)

# Get the width and height of the template image
w, h = template.shape[::-1]

# Loop through the identified locations and draw a rectangle around the matching card images
for pt in zip(*locations[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

# Display the image
cv2.imshow('Cards', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Better version that gets the cord of the required card
import pyautogui
import cv2
import numpy as np
import time

# Take a screenshot of the current screen
image = pyautogui.screenshot()

# Convert the image to a numpy array
image = np.array(image)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
done = None
i = 1
while i != 3:# Use OpenCV's template matching function to find card images in the screenshot
  template = cv2.imread((str(i)+'.png'), 0)
  i+=1

  result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)

  # Use a threshold to identify locations with a high match score
  threshold = 0.95
  locations = np.where(result >= threshold)

  # Loop through the identified locations and print the coordinates of the matching card images
  for pt in zip(*locations[::-1]):
    print(f'Card found at x={pt[0]}, y={pt[1]}')
    time.sleep(0.25)
    pyautogui.click(pt[0],pt[1])

"""
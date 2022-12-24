import pyautogui
from PIL import Image
from pytesseract import pytesseract


# Set the coordinates of the area you want to capture
left = 200
top = 390
width = 420
height = 330

# Take a screenshot of the specified area
#screenshot = pyautogui.screenshot(region=(left, top, width, height))

# Save the screenshot to a file
#screenshot.save('1.png')
image = Image.open("card.png")
gray_image = image.convert("L")
gray_image.save("card.png")
text = pytesseract.image_to_string(gray_image, config="--psm 3")
# Opening the image & storing it in an image object
#img = '1.png'

#text = pytesseract.image_to_string(img)


# Displaying the extracted text
print(text[:-1])


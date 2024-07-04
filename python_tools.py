n = lambda input_path: [folder for folder in os.listdir(input_path)] # dirs and files names
n = lambda input_path: [file for file in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, file))] # files names
n = lambda input_path: [folder for folder in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, folder))] # dirs names

p = lambda input_path: [os.path.join(input_path, folder) for folder in os.listdir(input_path)] # dirs and files paths
p = lambda input_path: [os.path.join(input_path, folder) for folder in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, folder))] # files paths
p = lambda input_path: [os.path.join(input_path, folder) for folder in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, folder))] # dirs paths




###################################################################################
from PIL import Image
import os

def concatenate_images_vertically(folder_path):
    # Get all image file paths from the folder
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]
    
    # Open all images and store them in a list
    images = [Image.open(img_file) for img_file in image_files]
    
    # Calculate the total height and the max width of the concatenated image
    total_height = sum(img.height for img in images)
    max_width = max(img.width for img in images)
    
    # Create a new image with the calculated max width and total height
    concatenated_image = Image.new('RGB', (max_width, total_height))
    
    # Paste each image into the concatenated image
    current_y = 0
    for img in images:
        concatenated_image.paste(img, (0, current_y))
        current_y += img.height
    
    # Define the output path
    output_path = os.path.join(folder_path, 'concatenated_image_vertically.jpg')
    
    # Save the concatenated image
    concatenated_image.save(output_path)
    
    return output_path

cv = concatenate_images_vertically


###################################################################################
import webbrowser

def open_links():
    links = [
        "https://chat.openai.com",
        "https://www.bing.com/chat",
        "https://yiyan.baidu.com/"
    ]
    for link in links:
        webbrowser.open(link)

# Call the function to open the links
open_links()


###################################################################################
from PIL import Image, ImageDraw

def generate_background_image(size, color_str, output_path):
    # Parse the color string into RGB components
    color = tuple(int(color_str[i:i+2], 16) for i in (1, 3, 5))
    
    # Create a new image with the specified size and background color
    img = Image.new('RGB', size, color)
    
    # Save the image to the specified output path
    img.save(output_path)
    
    print(f"Generated background image with size {size} and color {color_str}. Saved to {output_path}")

# Example usage:
if __name__ == "__main__":
    size = (940, 348)  # Example size (width, height)
    color_str = "#EBE6E4"  # Example color string
    output_path = r"C:\Users\34950\Desktop\test\background_image.png"  # Example output path
    
    generate_background_image(size, color_str, output_path)
	
	
###################################################################################


#! python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch.\nPress Ctrl-C to quit.')
input()  # press Enter to begin
print('Started.')
startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f'Lap #{lapNum}: {totalTime} ({lapTime})', end='')
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')

###################################################################################


def cells_2_list(txt=''):
    '''still have bugs...'''
    import pyperclip as p
    # Check if the text contains double quotes
    if not txt:
        txt = p.paste()
    txt = txt.strip()
    if '"' in txt:
        # Replace new lines within quotes with whitespace
        cleaned_txt = ''
        in_quote = False
        for char in txt:
            if char == '"':
                in_quote = not in_quote
            if in_quote and char == '\n':
                cleaned_txt += ' '
            else:
                cleaned_txt += char
        # Remove double quotes
        # cleaned_txt = cleaned_txt.replace('"', '')
    else:
        cleaned_txt = txt.strip()  # Remove leading/trailing whitespace
    # Split text into a list based on newline separator
    result_list = cleaned_txt.split('\n')
    result_list = [i.strip() for i in result_list]
    print(f'Found {len(result_list)} item(s).')
    return result_list

c2l = cells_2_list


# import pyperclip; pyperclip.copy("\n".join



###################################################################################

import phonenumbers
from phonenumbers import geocoder

def guess_country(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        country = geocoder.country_name_for_number(parsed_number, "en")
        return country
    except phonenumbers.NumberParseException:
        return "Invalid phone number"

gc = guess_country

###################################################################################

import random
from PIL import Image, ImageDraw, ImageFont
import lorem

def generate_background_image(size, output_path, color_str=None, lorem_words=False):
    # Generate a random color if color_str isn't provided
    if color_str is None:
        color = tuple(random.randint(0, 255) for _ in range(3))
    else:
        # Parse the color string into RGB components
        color = tuple(int(color_str[i:i+2], 16) for i in (1, 3, 5))
    
    # Create a new image with the specified size and background color
    img = Image.new('RGB', size, color)
    
    # If lorem_words is True, add lorem text to the image
    if lorem_words:
        draw = ImageDraw.Draw(img)
        # Generate lorem text
        text = lorem.sentence()
        
        # Choose a font size that fits within the image size
        font_size = 30
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()
        
        # Determine the size of the text
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Calculate position to center the text
        text_x = (size[0] - text_width) // 2
        text_y = (size[1] - text_height) // 2
        
        # Draw the text on the image
        draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255))
    
    # Save the image to the specified output path
    img.save(output_path)
    
    print(f"Generated background image with size {size} and color {color}. Saved to {output_path}")

# Example usage:
# generate_background_image((800, 600), 'output.png', lorem_words=True)


t = generate_background_image

# Example usage:

output_path = r"C:\Users\34950\Desktop\test\background_image.png"
t((800, 600), output_path, lorem_words=True)
t((1920, 1080), output_path, lorem_words=True)


# generate_background_image((800, 600), 'output.png', lorem_words=True)

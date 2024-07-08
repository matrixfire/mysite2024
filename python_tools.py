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




################################################################################### 






import os
import re
import pyperclip

def get_folder_contents(folder_path, exclude_regex=[]):
    """
    Collects subfolders and files in a folder based on exclusion criteria.

    Parameters:
    - folder_path (str): Path to the folder to collect contents of.
    - exclude_regex (list): List of regex patterns. Folders or files matching any of these patterns will be excluded.

    Returns:
    - tuple: A tuple containing two lists: (subfolders, files)
      subfolders (list): List of subfolder paths.
      files (list): List of file names.
    """
    subfolders = []
    files = []

    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        return subfolders, files
    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            subfolders.append(item_path)
        elif os.path.isfile(item_path):
            files.append(item)

    # Filter out subfolders and files based on exclude_regex
    subfolders = [folder for folder in subfolders if not any(re.search(pattern, folder) for pattern in exclude_regex)]
    files = [file for file in files if not any(re.search(pattern, file) for pattern in exclude_regex)]

    return subfolders, files

def print_folder_contents(folder_path, indent=0, print_files=True, exclude_regex=[]):
    """
    Prints subfolders and files in a folder with hierarchical indentation.

    Parameters:
    - folder_path (str): Path to the folder to print contents of.
    - indent (int): Indentation level for subfolders and files.
    - print_files (bool): If True, prints both folders and files. If False, prints only subfolders.
    - exclude_regex (list): List of regex patterns. Folders or files matching any of these patterns will be excluded.

    Returns:
    - str: The formatted string of folder contents.
    """
    subfolders, files = get_folder_contents(folder_path, exclude_regex)

    folder_name = os.path.basename(folder_path)
    output = f"{' ' * indent}{folder_name}\n"

    if print_files:
        for file in files:
            output += f"{' ' * (indent + 4)}- {file}\n"

    for subfolder in subfolders:
        output += print_folder_contents(subfolder, indent + 4, print_files, exclude_regex)

    return output

# Example usage:
folder_path = r"C:\Users\34950\Desktop\work\mysite2024"
folder_path = r"C:\Users\34950\Desktop\work\mysite2024\shop\templates"


output = print_folder_contents(folder_path, print_files=True)
print(output)
pyperclip.copy(output)


######################################################################




import os
import re
import pyperclip

def get_folder_contents(folder_path, exclude_regex=[]):
    """
    Collects subfolders and files in a folder based on exclusion criteria.

    Parameters:
    - folder_path (str): Path to the folder to collect contents of.
    - exclude_regex (list): List of regex patterns. Folders or files matching any of these patterns will be excluded.

    Returns:
    - tuple: A tuple containing two lists: (subfolders, files)
      subfolders (list): List of subfolder paths.
      files (list): List of file names.
    """
    subfolders = []
    files = []

    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        return subfolders, files
    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            subfolders.append(item_path)
        elif os.path.isfile(item_path):
            files.append(item)

    # Filter out subfolders and files based on exclude_regex
    subfolders = [folder for folder in subfolders if not any(re.search(pattern, folder) for pattern in exclude_regex)]
    files = [file for file in files if not any(re.search(pattern, file) for pattern in exclude_regex)]

    return subfolders, files

def print_folder_contents(folder_path, indent=0, print_files=True, exclude_regex=[]):
    """
    Prints subfolders and files in a folder with hierarchical indentation.

    Parameters:
    - folder_path (str): Path to the folder to print contents of.
    - indent (int): Indentation level for subfolders and files.
    - print_files (bool): If True, prints both folders and files. If False, prints only subfolders.
    - exclude_regex (list): List of regex patterns. Folders or files matching any of these patterns will be excluded.

    Returns:
    - str: The formatted string of folder contents.
    """
    subfolders, files = get_folder_contents(folder_path, exclude_regex)

    folder_name = os.path.basename(folder_path)
    output = f"{' ' * indent}{folder_name}\n"

    if print_files:
        for file in files:
            output += f"{' ' * (indent + 4)}- {file}\n"

    for subfolder in subfolders:
        output += print_folder_contents(subfolder, indent + 4, print_files, exclude_regex)

    return output

# Example usage:
folder_path = r"C:\Users\34950\Desktop\work\mysite2024"
# folder_path = r"C:\Users\34950\Desktop\work\mysite2024\shop\templates"
exclude_regex = [
    r'(^|[\\/])\.git($|[\\/])',  # Exclude .git and its subfolders/files
    r'(^|[\\/])migrations($|[\\/])',  # Exclude migrations and its subfolders/files
    r'(^|[\\/])__pycache__($|[\\/])'  # Exclude __pycache__ and its subfolders/files
]

# output = print_folder_contents(folder_path, print_files=True)
output = print_folder_contents(folder_path, print_files=True, exclude_regex=exclude_regex)
print(output)
pyperclip.copy(output)


######################################################################

import os
import requests
from urllib.parse import urlparse

def download_image(image_url, save_path):
    """
    Downloads an image from a given URL and saves it to a specified path.
    
    :param image_url: str, URL of the image to be downloaded
    :param save_path: str, path where the image will be saved. If a directory is provided,
                      the image will be saved in the current working directory.
    :return: str, full path of the saved image
    """
    try:
        # Check if save_path is a directory
        if os.path.isdir(save_path):
            # Get the image name from the URL
            parsed_url = urlparse(image_url)
            image_name = os.path.basename(parsed_url.path)
            save_path = os.path.join(save_path, image_name)
        
        # Send a GET request to the image URL
        response = requests.get(image_url, stream=True)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Open the file in binary mode and write the content
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Image successfully downloaded: {save_path}")
            return save_path
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    image_url = "https://pantasy.com/cdn/shop/files/03_58872eac-0e01-4fbd-969d-680e070d84fd.jpg"
    save_path = r"C:\Users\Administrator\Desktop\work2024\reobrix_site\reobrix2\core\static\core\images\youtube.jpg"
    download_image(image_url, save_path)




















'''
You are going to act as a Django expert who understands both web development and e-commerce.

Here’s what I want to do: I am going to build a full-featured website using Django. This website will introduce my company and provide a shop for customers to buy products. The most important app, in my opinion, should be the shop, which will handle online sales, followed by a blog for product promotion and SEO. Ultimately, my goal is to create a website that can rival a Shopify store, allowing me to run my business independently.

Below is a brief introduction to the two apps, listing the minimum features the site should have:

The shop has the following features:

1. **Product Catalog and Shopping Cart:**- A catalog of products.- A shopping cart implemented using sessions.- A custom context processor to make the cart accessible across all templates.

2. **Order Placement:**- A form for placing orders.

3. **Asynchronous Task Management:**- Proficiency in employing asynchronous tasks with Celery and RabbitMQ for handling complex background operations.

4. **Payment Integration:**- Integration with the Stripe payment gateway.- A webhook endpoint for receiving payment notifications.

5. **Administrative Actions and Customization:**- Custom actions in the administration site to export orders to CSV.- Custom views and templates in Django's administration interface.

6. **PDF Generation and Email Integration:**- Generation of PDF files using WeasyPrint.- Integration of generated PDFs as email attachments.

7. **Coupon System:**- Implementation of a coupon system using Django sessions.- Integration of the coupon system with Stripe.

8. **Product Recommendation Engine:**- Development of a product recommendation engine powered by Redis to suggest products typically purchased together.

9. **Internationalization and Localization:**- Marking code and template strings for translation.- Generating and compiling translation files.- Managing translations with Rosetta via a web interface.- Translating URL patterns.- Implementing a language selector for users to switch site languages.- Using django-parler for model translations.- Validating localized form fields with django-localflavor.

The blog site has the following features:
1. **Basic Blog Functionality:**- A simple blog application with data models, views, templates, and URLs.

2. **SEO Optimization:**- Canonical URLs and SEO-friendly URLs for blog posts.

3. **Pagination:**- Posts are paginated to improve navigation and readability.

4. **User Interaction:**- Forms for users to recommend blog posts via email.- A comment system for readers to engage with posts.

5. **Tagging System:**- Tags to categorize posts and improve content organization.

6. **Advanced QuerySets:**- Functionality to recommend similar posts based on content similarity.

7. **Custom Template Tags and Filters:**- Specialized functionalities to enhance the templates.

8. **Sitemap and RSS Feed:**- A sitemap to help search engines index the site.- An RSS feed for users to subscribe to updates.

9. **Full-Text Search:**- A powerful search engine using PostgreSQL to find relevant content within the blog.


If you understand, simply say OK, I will later tell you what I want you to do.

'''
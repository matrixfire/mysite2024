n = lambda input_path: [folder for folder in os.listdir(input_path)] # dirs and files names
n = lambda input_path: [file for file in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, file))] # files names
n = lambda input_path: [folder for folder in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, folder))] # dirs names

p = lambda input_path: [os.path.join(input_path, folder) for folder in os.listdir(input_path)] # dirs and files paths
p = lambda input_path: [os.path.join(input_path, folder) for folder in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, folder))] # files paths
p = lambda input_path: [os.path.join(input_path, folder) for folder in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, folder))] # dirs paths


import pyperclip as p; cl=lambda lt: p.copy("\n".join(lt))
pl = lambda lt: print("\n".join(lt))


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




#############################################################################################

import chardet

def detect_file_encoding(file_path):
    """
    Detect the encoding of a given file.
    
    Parameters:
    file_path (str): The path to the file.
    
    Returns:
    str: The detected encoding of the file.
    """
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    encoding = result['encoding']     
    print(f"The encoding of the file is {encoding}")    
    return encoding

# Usage example
file_path = r"C:\Users\Administrator\Desktop\work2024\reobrix_site\reobrix2\p.csv"
encoding = detect_file_encoding(file_path)
print(f"The encoding of the file is {encoding}")
















'''
prompts:


You are going to act as a Django expert who understands both web development and e-commerce.

Here’s what I want to do: I am going to build a full-featured website using Django. This website will introduce my company and provide a shop for customers to buy products. The most important app, in my opinion, should be the shop, which will handle online sales, followed by a blog for product promotion and SEO. Ultimately, my goal is to create a website that can rival a Shopify store, allowing me to run my business independently.

Below is a brief introduction to the two apps, listing the minimum features the site should have:

The shop app has the following features:

1. **Product Catalog and Shopping Cart:**- A catalog of products.- A shopping cart implemented using sessions.- A custom context processor to make the cart accessible across all templates.

2. **Order Placement:**- A form for placing orders.

3. **Asynchronous Task Management:**- Proficiency in employing asynchronous tasks with Celery and RabbitMQ for handling complex background operations.

4. **Payment Integration:**- Integration with the Stripe payment gateway.- A webhook endpoint for receiving payment notifications.

5. **Administrative Actions and Customization:**- Custom actions in the administration site to export orders to CSV.- Custom views and templates in Django's administration interface.

6. **PDF Generation and Email Integration:**- Generation of PDF files using WeasyPrint.- Integration of generated PDFs as email attachments.

7. **Coupon System:**- Implementation of a coupon system using Django sessions.- Integration of the coupon system with Stripe.

8. **Product Recommendation Engine:**- Development of a product recommendation engine powered by Redis to suggest products typically purchased together.

9. **Internationalization and Localization:**- Marking code and template strings for translation.- Generating and compiling translation files.- Managing translations with Rosetta via a web interface.- Translating URL patterns.- Implementing a language selector for users to switch site languages.- Using django-parler for model translations.- Validating localized form fields with django-localflavor.

The blog app has the following features:
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




'''
1, Managing GitHub and Git
   - Sign up for a GitHub account and create a repository.
   - Initialize Git in the local project folder.
   - Add and commit project files to the repository.
   - Push the code to GitHub.
   
git init
git add .
git commit -m "first version"
git branch -M main
git remote add origin <your-origin-path>
git push -u origin main

2, Cloning our code onto PythonAnywhere
   - Create a free account on PythonAnywhere.
   - Open a Bash console on PythonAnywhere.
   - Clone the GitHub repository to PythonAnywhere.
---

**PythonAnywhere Bash Setup**

1. **Accessing Bash Console:**
   - Open PythonAnywhere.
   - Click **Dashboard** > **New console** > **$ Bash**.

2. **Cloning from GitHub:**
   - Go to your GitHub repository.
   - Click **Code** and copy the URL.
   - In PythonAnywhere Bash shell, run:
     ```
     git clone <repo-url>
     ```

---

git clone https://github.com/matrixfire/mysite2024.git



3, Configuring virtual environments
   - Create a virtual environment using `mkvirtualenv`.
   - Install required packages (Django, Pillow) in the virtual environment.
---

**Managing Virtual Environments on PythonAnywhere**

1. **Creating a Virtual Environment:**
   - To create using Python 3.8:
     ```
     mkvirtualenv -p python3.8 <environment name>
     ```
	 mkvirtualenv -p python3.10 reobrix_venv
	 

2. **Activating and Deactivating:**
   - To deactivate the virtual environment:
     ```
     deactivate
     ```
   - To activate a virtual environment:
     ```
     workon <virtualenv-name>
	 
	 workon reobrix_venv
	 
	 workon reobrix_venv && cd /home/reobrix/mysite2024 && celery -A reobrix worker
	 
	 workon your_virtualenv && cd /path/to/your_project && celery -A your_project worker

     ```

---



4, Setting up your web app
   - Gather information: project path, project name, virtual environment name.
   - Create a web app with manual configuration on PythonAnywhere.
   - Configure the WSGI file to point to the Django project.
   - Update `ALLOWED_HOSTS` in `settings.py` and reload the web app.

---

**Setting up Django Web App on PythonAnywhere**

1. **Prepare Information:**
   - "A": Get the path to your Django project's top folder using `pwd` in Bash, e.g., `/home/danielgara/moviereviews/`.(the folder that contains "manage.py")
   - "B": Note your project's name (folder containing `settings.py`), e.g., `moviereviews`.
   - "C": Remember your virtualenv name, e.g., `moviereviewsenv`.

A: /home/reobrix/mysite2024
B: reobrix
C: reobrix_venv



2. **PythonAnywhere Setup:**
   - Open PythonAnywhere dashboard.
   - Go to **Web** > **Add a new web app**.
   - Choose **Manual configuration** under Python Web framework.
   - Select Python version (e.g., Python 3.8) and click **Next**.
   - enter the name of your virtualenv（i.e. "C" info） in the Virtualenv section
   - Enter project folder path(i.e. "A" info) in **Source code** and **Working directory**.

3. **Configure WSGI File:**
   - Open `wsgi.py` and modify to:
     ```python
	# +++++++++++ DJANGO +++++++++++
	# To use your own django app use code like this:
     import os
     import sys

     path = '/home/danielgara/moviereviews' # "A" info
     if path not in sys.path:
         sys.path.append(path)

     os.environ['DJANGO_SETTINGS_MODULE'] = 'moviereviews.settings' # "B" info

     from django.core.wsgi import get_wsgi_application
     application = get_wsgi_application()
     ```

4. **Update ALLOWED_HOSTS:**
   - Navigate to **Files** > find `settings.py` in `moviereviews/`.
   - Modify `ALLOWED_HOSTS`:
     ```python
     DEBUG = True
     ALLOWED_HOSTS = ['*']
     ```

5. **Reload and Test:**
   - Go to **Web** tab, click **Reload** for your domain.
   - Visit your project's URL to see the home page.

---

mysql -u reobrix -h reobrix.mysql.pythonanywhere-services.com -p 'reobrix$default'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
		'TEST': {'NAME': config('TEST_DB_NAME'),}
    }
}



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<your_username>$<your_database_name>',
        'USER': '<your_username>',
        'PASSWORD': '<your_mysql_password>',
        'HOST': '<your_mysql_hostname>',
		'TEST': {
            'NAME': '<your username>$test_<your database name>',
        }
    }
}







reobrix
reobrix.mysql.pythonanywhere-services.com


5, Configuring static files
   - Define `STATIC_URL` and `STATIC_ROOT` in `settings.py`.
   - Run `python manage.py collectstatic` to gather static files.
   - Set up static file mappings on PythonAnywhere.

---

**Configuring Static Files in Django on PythonAnywhere**

1. **Update `settings.py`:**
   - Add the following line:
     ```python
     STATIC_ROOT = os.path.join(BASE_DIR, 'static')
     ```
   - This sets a central location (`STATIC_ROOT`) for collecting all static files.

2. **Collect Static Files:**
   - In the Bash console (inside virtualenv), navigate to your project folder:
     ```
     cd moviereviews/
     ```
   - Run the command to collect static files:
     ```
     python manage.py collectstatic
     ```
   - This gathers static files from app folders and admin, copying them to `STATIC_ROOT`.

3. **Configure Static Files on PythonAnywhere:**
   - Go to PythonAnywhere dashboard **Web** tab.
   - Under **Static files**:
     - Enter `STATIC_URL` (typically `/static/`) in the **URL** section.
     - Enter full path from `STATIC_ROOT` in the **Path** section (e.g., `/home/username/moviereviews/static`).

4. **Reload Web App:**
   - Click **Reload** on the **Web** tab in PythonAnywhere.
   - Your static images should now appear correctly on your site.

---


---

**Production Configuration and .gitignore Setup**

1. **Setting DEBUG for Production:**
   - Go to PythonAnywhere dashboard.
   - Open `settings.py` for your project.
   - Set `DEBUG = False`.
   - Save the file and reload the web app.

2. **Creating .gitignore:**
   - Create a `.gitignore` file in your project root folder.
   - Add the following lines to ignore specific files:
     ```
     __pycache__/
     db.sqlite3
     .DS_Store
     ```
   - These files include cached Python files, database storage, and macOS folder settings.

---




6, Changing db.sqlite3 to MySQL or PostgresSQL

   - Use MySQL or PostgreSQL for larger projects.
   - Follow PythonAnywhere's documentation for database setup.
   - Recreate superuser and run migrations for the new database.

---

**Switching Database to MySQL or PostgreSQL**

1. **Setting Up MySQL:**
   - Refer to PythonAnywhere's documentation for setting up MySQL:
     - Free MySQL setup: [PythonAnywhere MySQL Documentation](https://help.pythonanywhere.com/pages/UsingMySQL/)
     - PostgreSQL setup requires a paid account.

2. **After Database Setup:**
   - Once MySQL or PostgreSQL is set up:
     - Create a new superuser for the new database:
       ```
       python manage.py createsuperuser
       ```
     - Make migrations for database changes:
       ```
       python manage.py makemigrations
       ```
     - Apply migrations to the database:
       ```
       python manage.py migrate
       ```

---

This note provides a detailed guide on deploying a Django project to PythonAnywhere, covering GitHub management, virtual environment setup, web app configuration, static file management, and database migration.


'''
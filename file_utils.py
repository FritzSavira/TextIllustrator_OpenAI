import requests
import re
import os


def download_and_save_image(image_url, image_local_path):
    """
    Download an image from a URL and save it to a local path.

    Args:
        image_url (str): The URL of the image to download.
        image_local_path (str): The local path where the image will be saved.

    Raises:
        requests.exceptions.RequestException: If there's an error during the download.
    """
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        with open(image_local_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image successfully saved at '{image_local_path}'.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")


def save_text_to_file(text, file_path):
    """
    Save a text string to a file.

    Args:
        text (str): The text to be saved.
        file_path (str): The path where the text file will be saved.

    Raises:
        IOError: If there's an error during the file writing process.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text successfully saved at '{file_path}'.")
    except IOError as e:
        print(f"Error saving text: {e}")


def save_files(paragraph, dalle_prompt, image_url, title, index, output_folder):
    """
    Save a set of related files: an image, a scene description, and a DALL-E prompt.

    Args:
        paragraph (str): The scene description text.
        dalle_prompt (str): The DALL-E prompt text.
        image_url (str): The URL of the image to download.
        title (str): The title used for generating filenames.
        index (int): An index used for ordering the files.
        output_folder (str): The folder where all files will be saved.
    """
    # Clean the title to create valid filenames
    title_cleaned = re.sub(r'[<>:"/\\|?*]', '_', title)[:20]

    # Generate file paths
    image_local_path = os.path.join(output_folder, f"{index}pic_{title_cleaned}.jpg")
    scene_local_path = os.path.join(output_folder, f"{index}scene_{title_cleaned}.txt")
    prompt_local_path = os.path.join(output_folder, f"{index}prompt_{title_cleaned}.txt")

    # Save all files
    download_and_save_image(image_url, image_local_path)
    save_text_to_file(paragraph, scene_local_path)
    save_text_to_file(dalle_prompt, prompt_local_path)

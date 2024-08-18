import re
import os
import json
from story_viewer import create_and_open_html
from openai_utils import create_storyline, create_term, create_illustration, create_dalle_prompt, create_sketch
from file_utils import save_files
from UI import ui

# Configuration Variables
DOWNLOADS_DIR = os.path.expanduser("~/Downloads")
CONTENT_FILE_NAME = "TextillustratorContent.json"
OUTPUT_FOLDER = "c:/Users/Fried/Documents/TextIllustrieren/output"
INPUT_FILE_NAME = "input_text.txt"

def read_json_content(file_path):
    """
    Read and parse JSON content from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Parsed JSON content.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def process_paragraphs(paragraphs, output_folder):
    """
    Process each paragraph to create DALL-E prompts, generate images, and save files.

    Args:
        paragraphs (list): List of paragraph strings.
        output_folder (str): Path to the output folder.
    """
    for i, paragraph in enumerate(paragraphs):
        title = extract_title(paragraph, i)
        dalle_prompt = create_dalle_prompt(paragraph)
        image_url = create_sketch(dalle_prompt)
        save_files(paragraph, dalle_prompt, image_url, title, i, output_folder)

def extract_title(paragraph, index):
    """
    Extract a title from the paragraph or generate a default one.

    Args:
        paragraph (str): The paragraph text.
        index (int): The index of the paragraph.

    Returns:
        str: Extracted or generated title.
    """
    match = re.search(r"\s*(.*)", paragraph)
    return match.group(1) if match else f"paragraph_{index}"

def main():
    """
    Main function to orchestrate the text illustration process.
    """
    content_file_path = os.path.join(DOWNLOADS_DIR, CONTENT_FILE_NAME)
    input_file = os.path.join(OUTPUT_FOLDER, INPUT_FILE_NAME)

    ui()  # Display the user interface

    # Wait for the TextillustratorContent.json file to be saved in the Downloads directory
    while not os.path.exists(content_file_path):
        pass

    # Read the content from the JSON file
    content = read_json_content(content_file_path)

    # Extract the text and scene_select from the JSON content
    story = content.get("text", "")
    scene_select = content.get("scene_select", "")

    if not story:
        return

    # Create the output directory if it doesn't exist
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Write the content to the input_text.txt file in the output directory
    with open(input_file, "w", encoding='utf-8') as file:
        file.write(story)

    # Delete the TextillustratorContent.json file from the Downloads directory
    os.remove(content_file_path)

    # Process the story based on the selected scene type
    if scene_select == "storyline":
        scene = create_storyline(story)
    elif scene_select == "term":
        scene = create_term(story)
    elif scene_select == "illustration":
        scene = create_illustration(story)
    else:
        return

    # Split scene into paragraphs
    paragraphs = scene.split("####")

    # Process each paragraph
    process_paragraphs(paragraphs, OUTPUT_FOLDER)

    # Display the generated image and scene text in the browser and convert it to a docx file
    create_and_open_html(OUTPUT_FOLDER)

if __name__ == "__main__":
    main()

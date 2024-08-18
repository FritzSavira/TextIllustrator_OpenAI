# TextIllustrator_OpenAI

TextIllustrator is a Python-based tool that transforms text input into visual stories using AI-powered generation. This project leverages OpenAI's GPT for text processing and DALL-E for image creation.

Key Features

Text-to-Visual Conversion: Transforms user-provided text into illustrations, storylines, and sketches.
Multiple Generation Modes: Supports creation of storylines, term illustrations, and general illustrations.
User Interface: Includes a simple UI for text input and scene selection.
Automated Processing: Handles file management, content processing, and output generation.
Visual Output: Generates DALL-E images based on processed text.
Result Presentation: Displays results in both HTML and DOCX formats.

How It Works

The user inputs text through the UI.
The application processes the input based on the selected mode (storyline, term, or illustration).
It generates DALL-E prompts and creates corresponding images.
The results are saved as text and image files.
A final HTML and DOCX output is generated for easy viewing.

Main Components

main(): Orchestrates the overall process flow.
process_paragraphs(): Handles individual paragraph processing.
create_storyline(), create_term(), create_illustration(): Generate specific content types.
create_dalle_prompt(): Prepares prompts for DALL-E image generation.
save_files(): Manages file output and organization.
create_and_open_html(): Generates the final viewable output.

Dependencies

OpenAI API (for GPT and DALL-E)
Various Python libraries (re, os, json)
Custom modules (story_viewer, openai_utils, file_utils, UI)

This project showcases the integration of advanced AI models for creative content generation, providing a unique tool for transforming textual ideas into visual stories.

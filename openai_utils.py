from openai import OpenAI

def create_storyline(text):
    """
    Generate a storyline from the given text using OpenAI's GPT-4 model.
     Args:
        text (str): The input text to create a storyline from.

    Returns:
        str: The generated storyline or an error message.
    """
    client = OpenAI()
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": '''
                You are an experienced storyboard artist and you tell stories like Immanuel Kant.
                Create a storyline from the following text.
                Create one paragraph for each key statement.
                Create a maximum of 5 paragraphs.
                Each paragraph begins with the name of the key statement on a separate line.
                Paragraphs are separated from each other with "####\n".
                Avoid the following terms: Magic
                Return only the formulated storyline, without further explanation or commentary.
                Please follow these instructions as closely as possible.
                Start revising the following text now:
                '''},
                {"role": "user", "content": text}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return str(e)

def create_term(text):
        """
        Extract and define scientific terms from the given text using OpenAI's GPT-4 model.

        Args:
            text (str): The input text to extract terms from.

        Returns:
            str: The extracted and defined terms or an error message.
        """
        client = OpenAI()
        try:
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": '''
                    You are an experienced editor and create scientific documentation.
                    Find key scientifically relevant terms in the following text.
                    Create one paragraph for each scientifically relevant term.
                    Each paragraph begins with the name of the scientifically relevant term on a separate line.
                    Paragraphs are separated from each other with "####\n".
                    Describe the definition of the scientific term clearly:
                    1. Delimit the term.
                    2. if it is an object, then describe the term vividly.
                    3. if it is a non-material term, then describe it dialectically.
                    Return only the formulated paragraph, without further explanations or comments.
                    Please follow these instructions as closely as possible.
                    Now start revising the following text:
                    '''},
                    {"role": "user", "content": text}
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            return str(e)

def create_illustration(text):
        """
        Create an explanatory paragraph for the central statement in the given text using OpenAI's GPT-4 model.

        Args:
            text (str): The input text to create an illustration from.

        Returns:
            str: The explanatory paragraph or an error message.
        """
        client = OpenAI()
        try:
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": '''
                    You are an experienced proofreader.
                    Find a single central statement in the text.
                    Create an explanatory paragraph for the central statement.
                    The paragraph begins with a unique name from the original text.
                    Return only the text of the explanatory paragraph, without further explanation or commentary.
                    Please follow these instructions as closely as possible.
                    Now start revising the following text:
                    '''},
                    {"role": "user", "content": text}
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            return str(e)

def create_dalle_prompt(text):
        """
        Generate a DALL-E prompt from the given text using OpenAI's GPT-4 model.

        Args:
            text (str): The input text to create a DALL-E prompt from.

        Returns:
            str: The generated DALL-E prompt or an error message.
        """
        client = OpenAI()
        try:
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": '''
                    Create a prompt for dall-e-3 from the following text.
                    Describe the main message of the text as a pictorial representation:
                    '''},
                    {"role": "user", "content": text}
                ],
                top_p=0.1
            )
            return completion.choices[0].message.content
        except Exception as e:
            return str(e)

def create_sketch(dalle_prompt):
        """
        Generate a sketch image using DALL-E 3 based on the given prompt.

        Args:
            dalle_prompt (str): The DALL-E prompt to generate an image from.

        Returns:
            str: The URL of the generated image or an error message.
        """
        client = OpenAI()
        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt='''
                only pictorial representations,
                style: roughly structured sketch drawn in pencil'''+dalle_prompt+
                ''' only pictorial representations,
                 style: roughly structured sketch drawn in pencil''',
                size="1024x1024",
                quality="standard",
                n=1,
            )
            return response.data[0].url
        except Exception as e:
            return str(e)

import sys
import os
import openai
from dotenv import load_dotenv


def main():
    # Ensures that there must be only one argument passed to the alias
    if len(sys.argv) < 2:
        print("Usage: revise <filename>")
        return
    # TODO: Make sure to check for valid code files, make a list 
    #       of dot files that this command will support

    # Get file path of the file
    # Must exist in the current directory
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
            print(f"File '{file_path}' not found.")
            return
    
    # Set up ai
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    prime = os.getenv("PROMPT_PRIME")
    base_url = os.getenv("BASE_URL")

    # TODO: Refactor these if statements
    if not api_key:
        raise ValueError("API key is missing.")

    if not prime:
        raise ValueError("Prime is missing.")

    if not base_url:
        raise ValueError("Base URL is missing")

    client = openai.OpenAI(
        base_url=base_url,
        api_key=api_key
    )

    # Read the contents of the file
    with open(file_path, 'r') as f:
            contents = f.read()
            final_format = prime + "\n" + contents

    # NOTE: For debugging
    # print(final_format)

    try:
        message = [
            {"role": "user", "content": final_format}
        ]

        completion = client.chat.completions.create(
            model="google/gemini-2.5-pro-exp-03-25:free",
            messages=message
        )
        # TODO: for debugging, but change to a log
        print(completion.choices[0].message.content)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

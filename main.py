import sys
import os
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
    
    
    # TODO: Install the dotevn dependency
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    prime = os.getenv("PROMPT_PRIME")
    base_url = os.getenv("BASE_URL")

    # Read the contents of the file
    with open(file_path, 'r') as f:
            contents = f.read()


if __name__ == "__main__":
    main()

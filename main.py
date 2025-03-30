import sys
import os
import openai
from dotenv import load_dotenv

# TODO: Make sure to check for valid code files, make a list 
#       of dot files that this command will support

# TODO: Make the checkFilePath method more robust

def main():
    validateArguments(sys.argv)

    filePath = sys.argv[1]
    checkFilePath(filePath)
    
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    prime = os.getenv("PROMPT_PRIME")
    base_url = os.getenv("BASE_URL")
    model = os.getenv("MODEL")

    validateEnvVariables(api_key, prime, base_url, model)

    final_format = openSrcCode(filePath, prime)
    
    client = openai.OpenAI(
        base_url=base_url,
        api_key=api_key
    )
    aiCall(final_format, client, model, "feedback.txt")

def validateEnvVariables(api_key, base_url, prime, model):
    if not api_key:
        raise ValueError("API key is missing.")

    if not base_url:
        raise ValueError("Base URL is missing")

    if not prime:
        raise ValueError("Prime is missing.")

    if not model:
        raise ValueError("Model is missing.")

def validateArguments(args):
    if len(args) != 2:
        print("Usage: revise <filename>")
        sys.exit(1)


def checkFilePath(filePath):
    if not os.path.exists(filePath):
            print(f"File '{filePath}' not found.")
            sys.exit(1)


def openSrcCode(filePath, prime): 
    # Read the contents of the file
    with open(filePath, 'r') as f:
            contents = f.read()
           
            final_format = prime + "\n" + contents
    return final_format


def aiCall(prompt, client, model, filename):
    print("Loading...")
    try:
        # message = [
        #    {"role": "user", "content": final_format}
        # ]
        message = [
            {
                "role": "user",
                "content": prompt 
            }
        ]

        completion = client.chat.completions.create(
            model=model,
            messages=message
        )
        response = completion.choices[0].message.content

        with open(filename, "w", encoding="utf-8") as f:
            f.write(response)
        print("Done")
        
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

# pip freeze > requirements.txt
#* -- Imports
import os
from dotenv import load_dotenv
import openai

#* -- Variables
path = os.path.dirname(__file__) #? Directory path

load_dotenv(dotenv_path=".env") #? Load .env file

openai.organization = os.getenv("ORG_ID") #? Set OpenAI organization ID
openai.api_key = os.getenv("API_KEY") #? Set OpenAI API key

#* -- Functions
def clearConsole() -> None: #? Clear console
    os.system("cls" if os.name == "nt" else "clear")

def chat() -> None:
    print("[@] Welcome, Ask me anything! Type '/exit' to quit.")

    while True:
        message = input("\n[@] You: ")

        if message.lower() == "/exit":
            print("\n[@] Exiting...")
            break

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": message
            }]
        )

        print(f"\n[@] ChatGPT: {completion.choices[0].message.content}")

def main() -> None:
    clearConsole()
    chat()

#! Main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

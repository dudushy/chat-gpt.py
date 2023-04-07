# pip freeze > requirements.txt
#* -- Imports
import os
from dotenv import load_dotenv

#* -- Variables
path = os.path.dirname(__file__) #? Directory path

load_dotenv(dotenv_path=".env") #? Load .env file

#* -- Functions
def clearConsole() -> None: #? Clear console
    os.system("cls" if os.name == "nt" else "clear")

def main() -> None:
    print(os.getenv("API_KEY"))

#! Main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

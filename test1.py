import os
from dotenv import load_dotenv

load_dotenv() 
api_key = os.getenv("API_KEY")
name = os.getenv("myname")


print(f"Your API key is: {api_key}")
print(f"Your Name Is: {name}")


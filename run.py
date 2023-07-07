from dotenv import load_dotenv
import os



load_dotenv()

proxy = os.getenv("PROXY")
input_url = os.getenv("INPUT_URL")


print(proxy)
print(input_url)
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # reads variables from a .env file and sets them in os.environ

client = OpenAI()


content= \
    """
    Explain what is an LLM in 2-3 scentences.
    """

# simple usage
response = client.responses.create(
    model="gpt-4o-mini",
    input=content
)

print(f"Response \n {response.output_text}")

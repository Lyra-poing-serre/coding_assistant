import os
import sys
import config
from dotenv import load_dotenv
from google import genai
from google.genai import types


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise ValueError("No prompt found")
    user_prompt = sys.argv[1]
    args = sys.argv[2:]

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=config.SYSTEM_PROMPT),
    )

    print(response.text)

    if "--verbose" in args:
        print("User prompt: ", user_prompt)
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Response tokens: ", response.usage_metadata.candidates_token_count)

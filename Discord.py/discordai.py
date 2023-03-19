import openai

# config stores the sensitive data such as api keys
import config

openai.api_key = config.openai_apikey


def prompt(message: str, author: str) -> str:
    print("Generating prompt for: " + message)
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "system", "content": f"A man named {author} sent this message. Tell him why the message is incorrect, fix it, and then please tell him how he can improve his grammar in the future. Sign it off with the name 'Grammar Man'. Message: " + message}]
    )

    return response.choices[0].message.content
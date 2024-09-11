
from openai import OpenAI
import os

# Set your OpenAI API key
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("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"),
)

# Define the function to send a message
def send_message_to_chatgpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # You can use "gpt-3.5-turbo" or other models based on your access
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,  # Adjust as needed
        temperature=0  # Adjust for more creativity
    )
    return response.choices[0].message['content'].strip()

# Example usage
if __name__ == "__main__":
    user_message = "Say this is a test"
    response = send_message_to_chatgpt(user_message)
    print("ChatGPT response:", response)

import openai

# Set up API key and endpoint URL
openai.api_key = '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'


# Prompt user for input text
input_text = input("Enter text to summarize: ")


output = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user","content": "You are an artist. Write one sentence that generates a prompt for an AI art piece (including art style, colors, themes, characters, and setting). Here is the story: '/n:" + input_text}
    ]
)

print(output.choices[0].message)


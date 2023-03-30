from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set up API key and endpoint URL
openai.api_key = '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'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get user input from form
        input_text = request.form['input_text']

        # Call your existing code to generate output
        output = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                    "content": "Write a sentence that generates a prompt for an AI art piece based on a story I will share (be sure to mention art style, colors, themes, characters, and setting). Be concise. Here is the story: '/n:" + input_text}
            ]
        )

        # Extract the output message from the API response
        output_message = output.choices[0].message.content

        response = openai.Image.create(
            prompt="" + output_message,
            n=1,
            size="1024x1024"
        )

        image_url = response['data'][0]['url']

        return render_template('index.html', output_message=output_message, image_url=image_url)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

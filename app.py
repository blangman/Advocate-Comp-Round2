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
                {"role": "user", "content": "You are an artist. Write a 15 word sentence that generates a prompt for an AI art piece (including art style, colors, themes, characters, and setting). Here is the story: '/n:" + input_text}
            ]
        )

        # Extract the output message from the API response
        output_message = output.choices[0].text

        return render_template('index.html', output_message=output_message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
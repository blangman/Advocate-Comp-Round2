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

        if len(input_text) < 15000:
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

        elif len(input_text) > 15000:

            if len(input_text) > 30000:
                input_text = input_text[0:30000]

            input1 = input_text[:len(input_text)//2]
            input2 = input_text[len(input_text)//2:]

            output1 = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user",
                     "content": "Write a sentence that generates a prompt for an AI art piece based on the first half of a story I will share (be sure to mention art style, colors, themes, characters, and setting). Be concise. Here is the story: '/n:" + input1}
                ]
            )

            output2 = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user",
                     "content": "Write a sentence that generates a prompt for an AI art piece based on the second half of a story I will share (be sure to mention art style, colors, themes, characters, and setting). Be concise. Here is the story: '/n:" + input2}
                ]
            )

            output_message1 = output1.choices[0].message.content
            output_message2 = output2.choices[0].message.content

            output3 = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user",
                     "content": "Merge these two prompts for an AI art piece into one prompt that pulls from elements of both. Here is the first prompt:" + output_message1 + "Here is the second prompt:" + output_message2 + "keep it concise."}
                ]
            )

            output_message3 = output3.choices[0].message.content

            

            output = openai.Image.create(
                prompt="" + output_message3,
                n=1,
                size="512x512"
            )

            image_url1 = output['data'][0]['url']

            return render_template('index.html',  image_url1=image_url1, output_message3=output_message3)
        else:
            print("Input must be under 30,000 characters. Input is currently " + str(len(input_text)) + " characters")
            return render_template('index.html')
 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

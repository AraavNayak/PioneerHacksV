from openai import OpenAI
client = OpenAI(api_key="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")
file_path='output_files/output.txt'
with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
    transcript = file.read()
completion = client.chat.completions.create(
model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a expert with speeches and the correct term/vocabulary speeches. Go through the speech transcript and list the user's most used words and then suggest a variety of different words that can be used to deliver a stronger speech. Then, write out an example (could be short, similar to original length) which is enhanced by the vocabulary you are suggesting."},
        {"role": "user", "content": "Now here is the user's speech: " + transcript}
]
)

print(completion.choices[0].message)
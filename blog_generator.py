import openai

with open("secret.txt", "r") as f:
    secret_key = f.read().strip()

openai.api_key = secret_key

def generate_blog(paragraph_topic):
  response = openai.completions.create(
    model = 'gpt-4.o',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3
  )

  retrieve_blog = response.choices[0].text

  return retrieve_blog


print(generate_blog('Why London is better than your city.'))
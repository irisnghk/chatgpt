import openai_secret_manager

assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

# Now you can access your OpenAI API key
print(secrets)

import openai
openai.api_key = secrets["api_key"]

prompt = "Hello, how are you doing today?"
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=60,
    n=1,
    stop=None,
    temperature=0.5,
)
print(response.choices[0].text.strip())

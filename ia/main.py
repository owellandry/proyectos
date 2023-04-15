import openai
import pyttsx3

# Ingrese aquí su clave de API
openai.api_key = "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"

# Defina el motor de voz que utilizará
engine = pyttsx3.init()

# Haga una pregunta a ChatGPT
prompt = "¿Cuál es la capital de Francia?"
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)

# Obtenga la respuesta de ChatGPT y hágala hablar con el motor de voz
answer = response.choices[0].text.strip()
engine.say(answer)
engine.runAndWait()

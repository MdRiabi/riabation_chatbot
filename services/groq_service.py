import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

DEFAULT_MODEL = "llama3-8b-8192"

def ask_groq(prompt: str, model: str = DEFAULT_MODEL, temperature: float = 0.7) -> str:
    resp = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=model,
        temperature=temperature
    )
    return resp.choices[0].message.content

def summarize_text(text: str, model: str = DEFAULT_MODEL) -> str:
    prompt = (
        "Tu es un assistant. Voici un texte à résumer :\n\n"
        f"{text}\n\n"
        "Fais un résumé clair, concis et structuré."
    )
    return ask_groq(prompt, model=model)

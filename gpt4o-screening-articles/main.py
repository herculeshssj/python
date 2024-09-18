"""
Script para realizar o processo de screening de títulos e resumos de artigos
usando a API da OpenAI, e usando o modelo GPT-4o e GPT-4o-mini
"""
from openai import OpenAI

if __name__ == '__main__':

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
    )
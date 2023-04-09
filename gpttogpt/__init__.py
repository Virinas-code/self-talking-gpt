# -*- coding: utf-8 -*-
"""
ChatGPT to ChatGPT

Make it talk to itself
"""
import os

import openai

API_KEY: str = os.environ["GPT_API_KEY"]
openai.api_key = API_KEY


def answer(question: str) -> str:
    """
    Make ChatGPT answer a question.

    :param str question: Question.
    :return str: Answer.
    """
    return openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=1,
        max_tokens=100,
    )["choices"][0]["text"]


def broken() -> None:
    """
    Broken ChatGPT.

    Outputs random crap.
    """
    prompt: str = input("> ")
    question: str = (
        prompt
        if prompt
        else "What would you say to another instance of yourself? Output only what you would say without quotes."
    )
    while True:
        print("\nChatGPT:")
        print(question)
        question = answer(question)


def main() -> None:
    """
    Main function.

    Does not support initial prompt yet.
    """
    prompt: str = input("> ")
    question: str = answer(prompt)
    while True:
        print("\nChatGPT:")
        print(question)
        question = answer(
            f"{prompt} My friend said:\n{question}\nwhat do you think about that?"
        )

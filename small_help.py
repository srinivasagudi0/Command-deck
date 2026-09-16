import random

#jokes from web


def say_joke():
    jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the developer go broke? Because he used up all his cache.",
    "Why was the computer cold? It left its Windows open.",
    "Why don't programmers play hide and seek? Because they always get caught in loops.",
    "What did the Java code say to the C code? You’ve got no class.",
    "Why did the programmer quit his job? Because he didn't get arrays!"
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the developer go broke? Because he used up all his cache.",
    "Why was the computer cold? It left its Windows open.",
    "Why don't programmers play hide and seek? Because they always get caught in loops.",
    "What did the Java code say to the C code? You’ve got no class.",
    "Why did the programmer quit his job? Because he didn't get arrays!"
    ]

    joke = random.choice(jokes)
    return joke
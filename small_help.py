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

def motivate():
    quotes = [
    "First, solve the problem. Then write the code.",
    "Talk is cheap. Show me the code.",
    "Code is power. It can change the world.",
    "Simplicity is prerequisite for reliability.",
    "It’s not a bug, it’s an undocumented feature.",
    "Make it work, make it right, make it fast.",
    "The best error message is the one that never shows up.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Before software can be reusable it first has to be usable.",
    "The only way to go fast is to go well.",
    "Don’t comment bad code – rewrite it.",
    "One of my most productive days was throwing away 1000 lines of code.",
    "The best way to start fixing a bug is to make it reproducible.",
    "If you’re good at the debugger it means you spent a lot of time debugging.",
    "Coding is not just about creating software, it’s about solving problems.",
    "Clean code always looks like it was written by someone who cares.",
    "Controlling complexity is the essence of computer programming.",
    "Premature optimization is the root of all evil.",
    "The most dangerous phrase in the language is 'we’ve always done it this way'.",
    "A long descriptive name is better than a short enigmatic name.",
    "Code that communicates its purpose is very important.",
    "Quality is never an accident; it is always the result of intelligent effort.",
    "I'm not a great programmer. I'm just a good programmer with great habits.",
    "The function of good software is to make the complex appear to be simple.",
    "In the beginner’s mind, there are many possibilities.",
    "The best way to predict the future is to invent it.",
    "There are only two hard things in Computer Science: cache invalidation and naming things.",
    "If you have to spend effort looking at a fragment of code, extract it into a function.",
    "Perfection is achieved when there is nothing more to take away.",
    "Refactoring is like cleaning up the kitchen while you cook."
    ]
    quote = random.choice(quotes)
    return quote
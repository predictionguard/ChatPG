import predictionguard as pg

# Create a new client
client = pg.Client()

# Delete any existing proxy endpoints from previous
# configurations and recreate them.
chatGen = "chatpg-gen"
client.delete_proxy(chatGen)

# Create our generator proxy endpoint.
print("")
print("Creating generator proxy endpoint...")
print("----------------------------------")
gen_ex1 = {
    "input": {
        "prompt": """The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: Hello, who are you?
AI: I am an AI created with Prediction Guard. How can I help you today?
Human: I'd like to ask a question.
AI:"""
    },
    "output": {
        "text": "Great! Please ask your question."
    }
}

gen_ex2 = {
    "input": {
        "prompt": """The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: Hello, who are you?
AI: I am an AI created with Prediction Guard. How can I help you today?
Human: I'm wondering if you can help me with a problem.
AI:"""
    },
    "output": {
        "text": "Sure! What's the problem?"
    }
}

gen_ex3 = {
    "input": {
        "prompt": """The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: Hello, who are you?
AI: I am an AI created with Prediction Guard. How can I help you today?
Human: What is the capital of France?
AI:"""
    },
    "output": {
        "text": "The capital of France is Paris."
    }
}

gen_examples = [
    gen_ex1,
    gen_ex2,
    gen_ex3
]

client.create_proxy(task="text-gen", name=chatGen, examples=gen_examples)
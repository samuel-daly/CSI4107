import tensorflow_hub as hub

model = hub.load("universal-sentence-encoder_4")

def embed(input):
    return model(input)
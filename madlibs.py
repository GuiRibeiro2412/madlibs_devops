import random
from flask import Flask, render_template, request

app = Flask(__name__)

words = {
    'names': ["Mario", "Luigi", "James", "Ronald", "Carlos", "Roberto"],
    'adjectives': ["pretty", "strong", "tall", "tired", "lucky"],
    'nouns': ["potato", "building", "chair", "shoe", "truck"],
    'plural_nouns': ["potatoes", "buildings", "chairs", "shoes", "trucks"],
    'verbs': ["jump", "crouch", "skip", "stroll", "sprint", "crawl"],
    'places': ["moon", "theatre", "dungeon", "parliament", "bathroom"],
    'emotions': ["sad", "happy", "anxious", "depressed", "angry", "ashamed"],
    'silly_words': ["hullaballoo", "bumbershoot", "whippersnapper", "flabbergast"],
    'adverbs': ["quickly", "rarely", "happily", "here", "never"],
}

def get_word(word_type: str) -> str:
    return random.choice(words[word_type])

def create_story():
    name = get_word('names')
    adjective= get_word('adjectives')
    noun = get_word('nouns')
    plural_noun = get_word('plural_nouns')
    verb = get_word('verbs')
    place = get_word('places')
    emotion = get_word('emotions')
    silly_word = get_word('silly_words')
    adverb = get_word('adverbs')

    return f"Today I went to the {place} and I saw a very {adjective} {noun}. It was {adverb} {verb}ing around! I couldn't believe I was seeing so many {plural_noun}! What a {silly_word}! I felt such {emotion} I rushed home to tell {name} all about it."

@app.route("/")
def home():
    return create_story()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
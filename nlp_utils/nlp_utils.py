import spacy
from transformers import pipeline
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

# Load spaCy model
nlp = spacy.load("en_core_web_md")

# Load transformers model for summarization
summarizer = pipeline("summarization")

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def get_synonyms(word):
    synonyms = wordnet.synsets(word)
    return set(lemma.name() for synset in synonyms for lemma in synset.lemmas())

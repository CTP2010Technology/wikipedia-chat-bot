import wikipediaapi
from nlp_utils.nlp_utils import summarize_text

wiki_wiki = wikipediaapi.Wikipedia('en')

def get_wikipedia_summary(title):
    page = wiki_wiki.page(title)
    return page.summary[:1000]  # Limit the response length

def get_detailed_summary(title):
    summary = get_wikipedia_summary(title)
    return summarize_text(summary)

def safe_get_wikipedia_summary(title):
    try:
        summary = get_detailed_summary(title)
        return summary
    except wikipediaapi.exceptions.PageError:
        return "Sorry, I couldn't find information on that topic."
    except wikipediaapi.exceptions.DisambiguationError as e:
        return f"That query is ambiguous. Here are some suggestions: {e.options}"

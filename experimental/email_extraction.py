import re

import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nlp = spacy.load("de_core_news_sm")

nltk.download("stopwords")
nltk.download("punkt") # Added back punkt download


def clean_text(text):
    text = text.lower()
    stop_words = set(stopwords.words("german"))
    word_tokens = word_tokenize(text, language="german")
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return " ".join(filtered_text)


def remove_signature(email):
    parts = re.split(r"-{2,}|\*{2,}", email)
    main_body = parts[0]

    if len(parts) > 1:
        signature_candidate = parts[-1]
        signature_candidate = re.sub(
            r"(?i)(mit freundlichen grüßen|beste grüße|herzliche grüße|viele grüße|cheers|thank you|thanks)[^\n]*",
            "",
            signature_candidate,
        )
        signature_candidate = re.sub(
            r"(?i)\b(Tel|Telephone|Phone|Fax|E-Mail|Email|Web|Website|URL):.*", "", signature_candidate
        )
        signature_candidate = re.sub(
            r"(?i)\b(Address|Adresse|Location|Standort|Company|Firma|Position|Titel|Geschäftsführung):.*",
            "",
            signature_candidate,
        )
        signature_candidate = re.sub(r"[\n\r]+", " ", signature_candidate)

        doc = nlp(signature_candidate)
        for ent in doc.ents:
            if ent.label_ in ["PER", "ORG"]:
                signature_candidate = signature_candidate.replace(ent.text, "")

        main_body += " " + signature_candidate.strip()

    return main_body.strip()


if __name__ == "__main__":
    email_text = """
    Hallo Herr Müller,

hier ist der Bericht über die Ergebnisse der letzten Woche. Bitte lassen Sie mich wissen, ob Sie Fragen haben.

Mit freundlichen Grüßen
John Doe
John Doe
Position: Chefredakteur
Company: Beispiel GmbH
Tel: +49 123 456789
E-Mail: john.doe@beispiel.de
Web: www.beispiel.de
    """

    print(clean_text(remove_signature(email_text)))

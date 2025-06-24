# Installationen und Modelldownload (falls noch nicht geschehen)
import re

import phonenumbers
import spacy
from faker import Faker


# spaCy-German-Modell und Faker-Generator mit deutscher Lokalisierung
nlp = spacy.load("de_core_news_sm")
fake = Faker("de_DE")

def anonymize_text(text):
    doc = nlp(text)
    new_text = text
    # Ersetzungen für erkannte Named Entities (von hinten nach vorn, um Indexprobleme zu vermeiden)
    for ent in sorted(doc.ents, key=lambda e: e.start_char, reverse=True):
        start, end = ent.start_char, ent.end_char
        if ent.label_ == "PER":  # Personenname
            fake_name = fake.first_name() + " " + fake.last_name()
            new_text = new_text[:start] + fake_name + new_text[end:]
        elif ent.label_ == "ORG":  # Organisation/Firma
            fake_org = fake.company()
            new_text = new_text[:start] + fake_org + new_text[end:]
        elif ent.label_ == "LOC":  # Ort (Stadt, Land, etc.)
            fake_city = fake.city_name()
            new_text = new_text[:start] + fake_city + new_text[end:]
    # E-Mail-Adressen maskieren (Regex)
    new_text = re.sub(r'\b[\w.+-]+@[\w-]+\.\w+\b', lambda m: fake.ascii_email(), new_text)
    # Telefonnummern erkennen und ersetzen
    def replace_phone(match):
        num_str = match.group(0)
        try:
            num = phonenumbers.parse(num_str, "DE")
            if phonenumbers.is_valid_number(num):
                return fake.phone_number()
        except phonenumbers.NumberParseException:
            pass
        return num_str
    new_text = re.sub(r'\+?\d[\d\s\-\(\)]{7,}\d', replace_phone, new_text)
    # IBAN erkennen und ersetzen
    new_text = re.sub(
        r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b",
        lambda m: fake.iban(),
        new_text,
    )
    # (Optional) Einfache Erkennung von Adressen mit Straßenname und Nummer
    new_text = re.sub(
        r'\b[A-ZÄÖÜ][a-zäöüß]+(?:straße|Str\.|Weg|Platz)\s*\d+[a-zA-Z]?\b',
        lambda m: fake.street_address(),
        new_text
    )
    return new_text

# Beispieltext mit PII
text = (
    "Herr Dr. Max Mustermann wohnt in der Musterstraße 5 in 55122 Mainz. "
    "Er arbeitet bei der Musterfirma GmbH. Kontakt: max@mustermann.de, +49 170 1234567."
)
if __name__ == '__main__':

    print("Original:", text)
    print("Anonymisiert:", anonymize_text(text))

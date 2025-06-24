import pytest

from experimental.anonymize_data import anonymize_text

texts = [
    # kurze Beispiele
    "Hallo, ich heiße Max Mustermann und wohne in der Hauptstraße 5, 12345 Musterstadt.",
    "Meine E-Mail ist max.mustermann@example.com, bitte schreibe dorthin.",
    "Ruf mich an: +49 151 12345678 oder 0151-12345678.",
    "Meine IBAN lautet DE89370400440532013000 und BIC COBADEFFXXX.",
    "Ich habe eine Kreditkarte: 4111 1111 1111 1111, Ablauf 12/24, CVC 123.",
    # verschiedene Namensformate
    "Herr Meyer",
    "Frau Dr. Sarah Connor",
    "J. K. Rowling schrieb das Buch",
    "Anna Maria Schmidt besuchte uns gestern.",
    "Begrüßung an Thomas",
    "Kontakt: Müller, T.",
    "Dr. A. Einstein war ein Genie.",
    "Prof. Johann Wolfgang von Goethe war Dichter.",
    # längere Texte
    (
        "Guten Tag, mein Name ist Claudia Fischer. Ich lebe derzeit in der Blumenstraße 12, 80802 München. "
        "Letzte Woche habe ich eine E-Mail an c.fischer@mail.de geschickt und warte noch auf eine Antwort. "
        "Sie können mich unter 089 123456 und mobil unter 0171-7654321 erreichen. "
        "Meine neue Kreditkarte (Visa) endet auf 1234 und hat die Gültigkeit 08/25."
    ),
    (
        "Liebes Tagebuch, heute hatte ich ein Vorstellungsgespräch bei der Firma Tech Solutions GmbH. "
        "Mein Ansprechpartner war Herr Stefan Klein (st.klein@techsolutions.de). "
        "Er hat meine Kontonummer 9876543210 und meine IBAN DE75512108001245126199 erfragt. "
        "Telefonisch erreichen kann man mich unter +49 (0)30 44556677."
    ),
    (
        "SMS von +49 172 5556667: 'Hallo Tobi, deine Bestellung mit der Nummer 123-4567890 ist versandt. "
        "Bitte überweise 49,99 € auf das Konto DE44100900001234567890 unter dem Verwendungszweck Best-Nr. 987654'."
    ),
    (
        "Email: support@meinebank.de\nBetreff: Ihre Kreditkarte\nSehr geehrter Herr Bück,\n"
        "Ihre Visa-Karte mit der Nummer 5105 1051 0510 5100 wurde aktiviert. "
        "Bitte beachten Sie, dass Ihre PIN per Post an die Anschrift Roonstr. 32, 76131 Karlsruhe gesendet wurde."
    ),
    (
        "Meeting-Protokoll:\nTeilnehmer: Dr. med. Martina Hoffmann, Dipl.-Ing. Thomas Wagner, "
        "Prof. Dr. rer. nat. Hans-Peter Müller\nOrt: Universitätsklinikum Freiburg, "
        "Engelbergerstraße 21, 79106 Freiburg\n"
        "Kontakt: hans.mueller@uniklinik-freiburg.de, Telefon 0761-2700"
    ),
]


@pytest.mark.parametrize("text", texts)
def test_remove_personal_info(text):
    result = anonymize_text(text)

    # keine spezifischen Originaldaten
    forbidden = [
        "Max Mustermann",
        "Hauptstraße 5",
        "12345 Musterstadt",
        "max.mustermann@example.com",
        "+49 151 12345678",
        "0151-12345678",
        "DE89370400440532013000",
        "4111 1111 1111 1111",
        "12/24",
        "CVC 123",
        "Meyer",
        "Frau Dr. Sarah Connor",
        "J. K. Rowling",
        "Anna Maria Schmidt",
        "Thomas",
        "Müller, T.",
        "Dr. A. Einstein",
        "Johann Wolfgang von Goethe",
        "Claudia Fischer",
        "Blumenstraße 12",
        "80802 München",
        "c.fischer@mail.de",
        "089 123456",
        "0171-7654321",
        "Visa) endet auf 1234",
        "Interview bei der Firma Tech Solutions GmbH",
        "Stefan Klein",
        "st.klein@techsolutions.de",
        "9876543210",
        "DE75512108001245126199",
        "+49 (0)30 44556677",
        "+49 172 5556667",
        "Bestellung mit der Nummer 123-4567890",
        "49,99 €",
        "DE44100900001234567890",
        "support@meinebank.de",
        "Herr Bück",
        "5105 1051 0510 5100",
        "Roonstr. 32",
        "76131 Karlsruhe",
        "Martina Hoffmann",
        "Thomas Wagner",
        "Hans-Peter Müller",
        "Engelbergerstraße 21",
        "79106 Freiburg",
        "hans.mueller@uniklinik-freiburg.de",
        "0761-2700",
    ]
    for item in forbidden:
        assert item not in result, f"Persönliche Information '{item}' nicht entfernt"

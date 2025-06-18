from huggingface_hub import login

from src.ce.run.classification.ticket_classifier import TicketClassifier

# Pass your token directly
login(token="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")
if __name__ == '__main__':
    tc = TicketClassifier("Tobi-Bueck/atc-queue-model", "Tobi-Bueck/atc-priority-model")

    # Your dynamic (or manual) QUEUE_MAP & PRIORITY_MAP
    QUEUE_MAP = {
        'Arts & Entertainment/Movies': 0,
        'Arts & Entertainment/Music': 1,
        'Autos & Vehicles/Maintenance': 2,
        'Autos & Vehicles/Sales': 3,
        'Beauty & Fitness/Cosmetics': 4,
        'Beauty & Fitness/Fitness Training': 5,
        'Books & Literature/Fiction': 6,
        'Books & Literature/Non-Fiction': 7,
        'Business & Industrial/Manufacturing': 8,
        'Finance/Investments': 9,
        'Finance/Personal Finance': 10,
        'Food & Drink/Groceries': 11,
        'Food & Drink/Restaurants': 12,
        'Games': 13,
        'Health/Medical Services': 14,
        'Health/Mental Health': 15,
        'Hobbies & Leisure/Collectibles': 16,
        'Hobbies & Leisure/Crafts': 17,
        'Home & Garden/Home Improvement': 18,
        'Home & Garden/Landscaping': 19,
        'IT & Technology/Hardware Support': 20,
        'IT & Technology/Network Infrastructure': 21,
        'IT & Technology/Security Operations': 22,
        'IT & Technology/Software Development': 23,
        'Jobs & Education/Online Courses': 24,
        'Jobs & Education/Recruitment': 25,
        'Law & Government/Government Services': 26,
        'Law & Government/Legal Advice': 27,
        'News': 28,
        'Online Communities/Forums': 29,
        'Online Communities/Social Networks': 30,
        'People & Society/Culture & Society': 31,
        'Pets & Animals/Pet Services': 32,
        'Pets & Animals/Veterinary Care': 33,
        'Real Estate': 34,
        'Science/Environmental Science': 35,
        'Science/Research': 36,
        'Shopping/E-commerce': 37,
        'Shopping/Retail Stores': 38,
        'Sports': 39,
        'Travel & Transportation/Air Travel': 40,
        'Travel & Transportation/Land Travel': 41
    }

    PRIORITY_MAP = {"very_low": 0, "low": 1, "medium": 2, "high": 3, "critical": 4}


    def get_queue_name(queue_id: int) -> str:
        for name, id_ in QUEUE_MAP.items():
            if id_ == queue_id:
                return name
        return "Unknown Queue"


    def get_priority_name(prio_id: int) -> str:
        for name, id_ in PRIORITY_MAP.items():
            if id_ == prio_id:
                return name
        return "Unknown Priority"


    # 1) Initialize your classifier

    # 2) Prepare a richer set of German tickets
    examples = [
        {
            "subject": "Drucker druckt nicht",
            "body": "Mein Drucker ist offline und zeigt seit gestern den Fehlercode E7. "
                    "Habe schon Neustart probiert, war aber ohne Erfolg.",
            "target_queue_id": 20,  # IT & Technology/Hardware Support
            "target_priority_id": 3  # high
        },
        {
            "subject": "Rechnung für April 2025 nicht erhalten",
            "body": "Bitte senden Sie mir die Rechnung für April 2025 noch einmal per E-Mail "
                    "zu. Die letzte Rechnung kam problemlos, ich brauche diese dringend.",
            "target_queue_id": 10,  # Finance/Personal Finance
            "target_priority_id": 2  # medium
        },
        {
            "subject": "Allgemeine Frage zu Ihren Öffnungszeiten",
            "body": "Können Sie mir bitte Ihre aktuellen Öffnungszeiten für den Kundensupport "
                    "in der Berliner Niederlassung mitteilen?",
            "target_queue_id": 26,  # Law & Government/Government Services
            "target_priority_id": 1  # low
        },
        {
            "subject": "Bestellung stornieren",
            "body": "Ich habe gestern eine Bestellung im Online-Shop aufgegeben (Bestellnummer 12345). "
                    "Bitte stornieren Sie diese, da sich mein Bedarf geändert hat.",
            "target_queue_id": 37,  # Shopping/E-commerce
            "target_priority_id": 2  # medium
        },
        {
            "subject": "Neues Webinar zu Maschinellem Lernen",
            "body": "Ich interessiere mich für Ihr kommendes Online-Seminar zum Thema "
                    "'Einführung in Machine Learning'. Gibt es noch freie Plätze?",
            "target_queue_id": 24,  # Jobs & Education/Online Courses
            "target_priority_id": 1  # low
        },
        {
            "subject": "Reservierung für italienisches Restaurant",
            "body": "Ich würde gerne für morgen Abend einen Tisch für 4 Personen "
                    "im Restaurant ‚La Trattoria‘ reservieren.",
            "target_queue_id": 12,  # Food & Drink/Restaurants
            "target_priority_id": 1  # low
        },
    ]

    # 3) Run inference and print extended results
    for ex in examples:
        preds = tc.classify({"subject": ex["subject"], "body": ex["body"]})
        pred_q_id = preds["queue"]
        pred_p_id = preds["priority"]

        print("────────────────────────────────────────────────────────")
        print(f"Subject: {ex['subject']}")
        print(f"Body:    {ex['body']}\n")
        print(f" → Expected queue:    [{ex['target_queue_id']}] {get_queue_name(ex['target_queue_id'])}")
        print(f"   Predicted queue:   [{pred_q_id}] {get_queue_name(pred_q_id)}")
        print(f" → Expected priority: [{ex['target_priority_id']}] {get_priority_name(ex['target_priority_id'])}")
        print(f"   Predicted priority:[{pred_p_id}] {get_priority_name(pred_p_id)}\n")

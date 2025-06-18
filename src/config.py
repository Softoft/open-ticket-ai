# Copyright (c) 2024 by Softoft, Tobias Bueck Einzelunternehmen
# This code is part of the "OTOBO - AI Ticket Classification - Basic" and is governed 
# by its license agreement. Full license in LICENSE_DE.md / LICENSE_EN.md. This code cannot be copied and/or distributed
# without the express permission of Softoft, Tobias Bueck Einzelunternehmen.
import datetime
import os

# region Environment Variables
MAX_RAM = os.getenv("MAX_RAM", 2)

DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = os.getenv("DATABASE_PORT", 3306)
DATABASE_USER = os.getenv("DATABASE_USER", "root")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
assert DATABASE_PASSWORD is not None, "DATABASE_PASSWORD must be set"

MIN_PREDICTION_CONFIDENCE = float(os.getenv("MIN_PREDICTION_CONFIDENCE", 0.7))
assert 0 <= MIN_PREDICTION_CONFIDENCE <= 1, "MIN_PREDICTION_CONFIDENCE must be between 0 and 1"
UNCLASSIFIED_QUEUE_NAME = os.getenv("UNCLASSIFIED_QUEUE_NAME", "Unclassified")

# endregion

# region Data Scraping
SUBJECT_LABEL = "subject"
TEXT_LABEL = "text"
COMBINED_TEXT_LABEL = "combined_text"
QUEUE_LABEL = "queue"
PRIORITY_LABEL = "priority"

TRAIN_DATA_FILE_DIRECTORY = "/app/data/training_data/dataset.json"
TRAIN_DATA_FILE_BASE = "ticket_training_data"
TRAIN_DATA_FILE_ENDING = "json"


def get_train_data_file():
    file_save_german_date = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")
    return f"{TRAIN_DATA_FILE_DIRECTORY}/{TRAIN_DATA_FILE_BASE}_{file_save_german_date}.{TRAIN_DATA_FILE_ENDING}"


# endregion

# region Training
DISTILBERT_GERMAN = "distilbert/distilbert-base-german-cased"
BERT_GERMAN = "dbmdz/bert-base-german-uncased"
TEST_SIZE = 1 / 4
MAX_LENGTH = 512
DISTILBERT_RAM = 1
BERT_RAM = 2
EARLY_STOPPING_PATIENCE = 3
BERT_RAM_REQUIRED = 8
# endregion

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class BaseClassifier:
    """
    Shared logic for combining text, tokenizing, and running a HF sequence-classifier.
    Subclasses only need to pass in their own model name.
    """
    def __init__(
        self,
        model_name: str,
        subject_times: int = 3,
        max_length: int = 512,
    ):
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name
        )
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name
        )
        self.subject_times = subject_times
        self.max_length = max_length
        self.model.eval()

    def _combine_text(self, ticket: dict) -> str:
        subject = ticket.get("subject", "")
        body = ticket.get("body", "")
        # repeat subject exactly as during training
        return ((subject.lower() + " ") * self.subject_times) + body.lower()

    def _encode(self, combined_text: str) -> dict:
        return self.tokenizer(
            combined_text,
            return_tensors="pt",
            truncation=True,
            padding="max_length",
            max_length=self.max_length,
        )

    def classify(self, ticket: dict) -> int:
        """
        Returns the predicted class ID (an integer).
        """
        text = self._combine_text(ticket)
        inputs = self._encode(text)
        with torch.no_grad():
            logits = self.model(**inputs).logits
        return int(torch.argmax(logits, dim=-1))
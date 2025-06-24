from open_ticket_ai.ce.run.preparers.data_preparer import DataPreparer


class SubjectBodyPreparer(DataPreparer):
    """Extract and concatenate the ticket subject and body."""

    @staticmethod
    def get_description() -> str:
        return "Prepares the subject and body of a ticket for processing by extracting relevant information."

    def prepare(self) -> str:
        """Prepare the subject and body string."""

        pass

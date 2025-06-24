from open_ticket_ai.ce.run.preparers.data_preparer import DataPreparer


class SubjectBodyPreparer(DataPreparer):
    @staticmethod
    def get_description() -> str:
        return "Prepares the subject and body of a ticket for processing by extracting relevant information."

    def prepare(self) -> str:
        pass


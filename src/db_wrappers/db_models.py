"""Separating out the models here helps in isolating the database so that changing to
another database in future is easy. A new database wrapper has only to conform to below
Pydantic models and everything will easily fall into place"""


from datetime import datetime


class StackOverflowQuestionAnswer:
    """Pydantic model for stack_overflow table"""

    ques_no: int
    ques_text: str
    ques_comments: str | None = None
    ans_text: str
    ans_accepted: bool
    created: datetime

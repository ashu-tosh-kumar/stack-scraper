from pydantic import BaseModel


class StackOverflowQuestion(BaseModel):
    """Represents a Stack Overflow question"""

    no: int
    text: str
    comments: str | None = None


class StackOverflowAnswer(BaseModel):
    """Represents a Stack Overflow answer"""

    text: str
    accepted: bool

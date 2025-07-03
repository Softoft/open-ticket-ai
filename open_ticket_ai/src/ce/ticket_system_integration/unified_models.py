from __future__ import annotations

from datetime import datetime
from typing import Optional, Dict, List

from pydantic import BaseModel


class UnifiedEntity(BaseModel):
    """Base entity with optional ID and name.

    Attributes:
        id (Optional[int]): Unique identifier for the entity. Defaults to None.
        name (Optional[str]): Display name of the entity. Defaults to None.
    """

    id: Optional[int] = None
    name: Optional[str] = None


class UnifiedUser(UnifiedEntity):
    """Represents a user within the system.

    Inherits attributes from `UnifiedEntity` and adds:

    Attributes:
        email (Optional[str]): Email address of the user. Defaults to None.
    """

    email: Optional[str] = None


class UnifiedQueue(UnifiedEntity):
    """Represents a ticket queue.

    Inherits attributes from `UnifiedEntity`.
    """


class UnifiedPriority(UnifiedEntity):
    """Represents a ticket priority level.

    Inherits attributes from `UnifiedEntity`.
    """


class UnifiedStatus(UnifiedEntity):
    """Represents a ticket status.

    Inherits attributes from `UnifiedEntity`.
    """


class UnifiedNote(BaseModel):
    """Represents a note attached to a ticket.

    Attributes:
        id (Optional[str]): Unique identifier for the note. Defaults to None.
        body (str): Content of the note.
        created_at (datetime): Timestamp when the note was created.
        is_internal (bool): Indicates if the note is internal (not visible to customers).
        author (UnifiedUser): User who created the note.
    """

    id: Optional[str] = None
    body: str
    created_at: datetime
    is_internal: bool
    author: UnifiedUser


class UnifiedTicket(BaseModel):
    """Unified representation of a support ticket.

    Attributes:
        id (str): Unique identifier for the ticket.
        subject (str): Subject line of the ticket.
        body (str): Main content/description of the ticket.
        custom_fields (Dict): Additional custom field data associated with the ticket.
        queue (UnifiedQueue): Queue to which the ticket belongs.
        priority (UnifiedPriority): Priority level of the ticket.
        status (UnifiedStatus): Current status of the ticket.
        owner (UnifiedUser): User currently assigned to the ticket.
        notes (List[UnifiedNote]): List of notes attached to the ticket. Defaults to empty list.
    """

    id: str
    subject: str
    body: str
    custom_fields: Dict
    queue: UnifiedQueue
    priority: UnifiedPriority
    status: UnifiedStatus
    owner: UnifiedUser
    notes: List[UnifiedNote] = []


class SearchCriteria(BaseModel):
    """Criteria for searching/filtering tickets.

    Attributes:
        id (Optional[str]): Ticket ID to search for. Defaults to None.
        subject (Optional[str]): Text to search in ticket subjects. Defaults to None.
        queue (Optional[UnifiedQueue]): Queue to filter by. Defaults to None.
        user (Optional[UnifiedUser]): User to filter by (e.g., owner). Defaults to None.
    """

    id: Optional[str] = None
    subject: Optional[str] = None
    queue: Optional[UnifiedQueue] = None
    user: Optional[UnifiedUser] = None
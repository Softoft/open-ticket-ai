from __future__ import annotations

from datetime import datetime
from typing import Optional, Dict, List

from pydantic import BaseModel


class UnifiedEntity(BaseModel):
    """Base entity with optional ID and name."""

    id: Optional[int] = None
    name: Optional[str] = None


class UnifiedUser(UnifiedEntity):
    """User representation."""

    email: Optional[str] = None


class UnifiedQueue(UnifiedEntity):
    """Ticket queue."""


class UnifiedPriority(UnifiedEntity):
    """Ticket priority."""


class UnifiedStatus(UnifiedEntity):
    """Ticket status."""


class UnifiedNote(BaseModel):
    """Representation of a ticket note."""

    id: Optional[str] = None
    body: str
    created_at: datetime
    is_internal: bool
    author: UnifiedUser


class UnifiedTicket(BaseModel):
    """Unified ticket model used throughout the application."""

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
    """Criteria for ticket searches."""

    id: Optional[str] = None
    subject: Optional[str] = None
    queue: Optional[UnifiedQueue] = None
    user: Optional[UnifiedUser] = None
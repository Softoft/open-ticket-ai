from datetime import datetime

from open_ticket_ai.src.ce.ticket_system_integration.unified_models import (
    UnifiedUser,
    UnifiedQueue,
    UnifiedPriority,
    UnifiedStatus,
    UnifiedNote,
    UnifiedTicket,
    SearchCriteria,
)


def test_unified_ticket_construction():
    user = UnifiedUser(id=1, name="Bob", email="bob@example.com")
    queue = UnifiedQueue(id=2, name="Support")
    prio = UnifiedPriority(id=3, name="High")
    status = UnifiedStatus(id=4, name="Open")
    note = UnifiedNote(
        id="n1",
        body="Hello",
        created_at=datetime.utcnow(),
        is_internal=False,
        author=user,
    )
    ticket = UnifiedTicket(
        id="t1",
        subject="Issue",
        body="Body",
        custom_fields={},
        queue=queue,
        priority=prio,
        status=status,
        owner=user,
        notes=[note],
    )
    assert ticket.owner.email == "bob@example.com"
    assert ticket.notes[0].author is user


def test_search_criteria():
    user = UnifiedUser(id=1, name="Bob")
    queue = UnifiedQueue(id=2, name="Support")
    criteria = SearchCriteria(id="1", subject="hi", queue=queue, user=user)
    assert criteria.queue.name == "Support"

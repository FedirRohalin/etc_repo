import heapq
from datetime import date
import functools

_note_counter = 0

@functools.total_ordering
class Note:
    def __init__(self, event_date, description):
        global _note_counter
        
        if not isinstance(event_date, date):
            raise TypeError("event_date має бути об'єктом datetime.date")
            
        self.event_date = event_date
        self.description = description
        
        self.creation_order = _note_counter
        _note_counter += 1

    def __lt__(self, other):
        if not isinstance(other, Note):
             return NotImplemented
        
        if self.event_date != other.event_date:
            return self.event_date < other.event_date
        
        return self.creation_order < other.creation_order

    def __eq__(self, other):
        """
        Метод "дорівнює" (==).
        """
        if not isinstance(other, Note):
            return NotImplemented
        
        return (self.event_date == other.event_date and
                self.creation_order == other.creation_order)

    def __repr__(self):
        return (f"Note(Дата: {self.event_date.strftime('%Y-%m-%d')}, "
                f"Опис: '{self.description}')")

class PriorityNoteQueue:
    def __init__(self):
        self.heap = []

    def add_note(self, event_date, description):
        note = Note(event_date, description)
        heapq.heappush(self.heap, note)

    def get_next_note(self):
        if self.is_empty():
            return None
        
        return heapq.heappop(self.heap)

    def peek_next_note(self):
        if self.is_empty():
            return None
        
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)
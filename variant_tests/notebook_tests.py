import unittest
from datetime import date
from notebook import Note, PriorityNoteQueue, _note_counter

class TestPriorityNoteQueue(unittest.TestCase):
    
    def setUp(self):
        self.notebook = PriorityNoteQueue()
        global _note_counter
        _note_counter = 0

    def test_01_add_note_and_size(self):
        self.assertTrue(self.notebook.is_empty())
        self.assertEqual(self.notebook.size(), 0)
        
        self.notebook.add_note(date(2025, 1, 1), "Новий рік")
        
        self.assertFalse(self.notebook.is_empty())
        self.assertEqual(self.notebook.size(), 1)

    def test_02_get_next_note_order(self):
        date_mid = date(2025, 10, 20)
        date_last = date(2025, 11, 1)
        date_first = date(2025, 10, 10)

        self.notebook.add_note(date_mid, "Середня подія")
        self.notebook.add_note(date_last, "Остання подія")
        self.notebook.add_note(date_first, "Перша подія")
        
        self.assertEqual(self.notebook.size(), 3)
        
        note1 = self.notebook.get_next_note()
        self.assertEqual(note1.description, "Перша подія")
        self.assertEqual(note1.event_date, date_first)
        
        note2 = self.notebook.get_next_note()
        self.assertEqual(note2.description, "Середня подія")
        
        note3 = self.notebook.get_next_note()
        self.assertEqual(note3.description, "Остання подія")
        
        self.assertTrue(self.notebook.is_empty())

    def test_03_peek_next_note(self):
        self.notebook.add_note(date(2025, 1, 10), "Подія 2")
        self.notebook.add_note(date(2025, 1, 5), "Подія 1")
        
        self.assertEqual(self.notebook.size(), 2)
        
        peeked_note = self.notebook.peek_next_note()
        
        self.assertEqual(peeked_note.description, "Подія 1")
        self.assertEqual(self.notebook.size(), 2)
        
        next_note = self.notebook.get_next_note()
        self.assertEqual(next_note.description, "Подія 1")
        #self.assertEqual(self.notebook.size(), 1)

    def test_04_get_from_empty_queue(self):
        self.assertIsNone(self.notebook.get_next_note())
        self.assertIsNone(self.notebook.peek_next_note())

    def test_05_priority_tie_breaker_fifo(self):
        same_date = date(2025, 5, 5)
        
        self.notebook.add_note(same_date, "Подія A (створена першою)")
        self.notebook.add_note(same_date, "Подія B (створена другою)")
        self.notebook.add_note(same_date, "Подія C (створена третьою)")
        
        note_a = self.notebook.get_next_note()
        self.assertEqual(note_a.description, "Подія A (створена першою)")
        
        note_b = self.notebook.get_next_note()
        self.assertEqual(note_b.description, "Подія B (створена другою)")
        
        note_c = self.notebook.get_next_note()
        self.assertEqual(note_c.description, "Подія C (створена третьою)")

    def test_06_note_constructor_validation(self):
        with self.assertRaises(TypeError):
            Note("2025-01-01", "Це рядок, а не дата")
            
        with self.assertRaises(TypeError):
            Note(12345, "Це число, а не дата")

if __name__ == '__main__':
    import xmlrunner 
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
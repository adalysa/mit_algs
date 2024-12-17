import unittest

class Array_Seq:
    def __init__(self): # O(1)
        self.A = []
        self.size = 0

    def __len__(self): return self.size # O(1)
    def __iter__(self): yield from self.A # O(n) iter_seq

    def build(self, X): # O(n)
        self.A = [a for a in X] # pretend this builds a static array
        self.size = len(self.A)

    def get_at(self, i): return self.A[i] # O(1)
    def set_at(self, i, x): self.A[i] = x # O(1)

    def _copy_forward(self, i, n, A, j): # O(n)
        for k in range(n):
            A[j + k] = self.A[i + k]

    def _copy_backward(self, i, n, A, j): # O(n)
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    def insert_at(self, i, x): # O(n)
        n = len(self)
        A = [None] * (n + 1)
        self._copy_forward(0, i, A, 0)
        A[i] = x
        self._copy_forward(i, n - i, A, i + 1)
        self.build(A)

    def delete_at(self, i): # O(n)
        n = len(self)
        A = [None] * (n - 1)
        self._copy_forward(0, i, A, 0)
        x = self.A[i]
        self._copy_forward(i + 1, n - i - 1, A, i)
        self.build(A)
        return x
                                                    # O(n)
    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self): return self.delete_at(0)
    def insert_last(self, x): self.insert_at(len(self), x)
    def delete_last(self): return self.delete_at(len(self) - 1)

    #write: swap ends(D): Swap the first and last items in the sequence in D in O(1) time.
    def swap_ends(self, D):
        if self.size < 2:
            return
        last_position = len(D)-1
        first = D.get_at(0)
        last = D.get_at(last_position)
        D.set_at(0, last)
        D.set_at(last_position, first)

    '''Correct ans:
    def swap_ends(D):
        x_first = D.delete_first()
        x_last = D.delete_last()
        D.insert_first(x_last)
        D.insert_last(x_first)'''

    #write: shift left(D, k): Move the first k items in order to the end of the sequence n D
    #in O(k) time. (After, the kth item should be last and the (k + 1)st item should be first.)
    def shift_left(self, D, k):
        if k > len(D):  # If k is greater than the size, return without changes.
            raise ValueError("k cannot be greater than the size of the sequence.")

        # Extract the first k elements
        first_k = [D.get_at(i) for i in range(k)]

        # Append these k elements to the end
        for x in first_k:
            D.insert_last(x)

        # Remove the first k elements
        for _ in range(k):
            D.delete_first()

    '''Correct ans:
    def shift_left(D, k):
        if (k < 1) or (k > len(D) - 1):
            return
        x = D.delete_first()
        D.insert_last(x)
        shift_left(D, k - 1)'''

class TestArraySeq(unittest.TestCase):
    def test_swap_ends(self):
        seq = Array_Seq()
        seq.build([1, 2, 3, 4, 5])  # Initial sequence
        
        # Call swap_ends
        seq.swap_ends(seq)

        print("Sequence after swap_ends:", seq.A)

        # Assertions to check correctness
        self.assertEqual(seq.get_at(0), 5, "First element should be swapped to 5.")
        self.assertEqual(seq.get_at(len(seq) - 1), 1, "Last element should be swapped to 1.")
        self.assertEqual(seq.A[1:-1], [2, 3, 4], "Middle elements should remain unchanged.")

    def test_shift_left(self):
        seq = Array_Seq()
        seq.build([1, 2, 3, 4, 5])  # Initial sequence

        # Shift the first 2 elements to the end
        seq.shift_left(seq, 2)

        print("Sequence after shift_left:", seq.A)

        # Assertions to check correctness
        self.assertEqual(seq.A, [3, 4, 5, 1, 2], "The sequence should be shifted correctly.")


if __name__ == "__main__":
    unittest.main()

class Sequence:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __iter__(self):
        return iter(self.items)

    def append(self, value):
        self.items.append(value)

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return f"Sequence({self.items})"


# Create a new sequence
seq = Sequence()

# Append some items
seq.append(10)
seq.append(20)
seq.append(30)

# Print the sequence
print(seq)  # Output: [10, 20, 30]

# Access items using indexing
print(seq[1])  # Output: 20

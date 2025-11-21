class QueueFullException(Exception):
    """Raised when enqueue is attempted on a full queue."""
    pass

class QueueEmptyException(Exception):
    """Raised when dequeue or front is attempted on an empty queue."""
    pass

class Queue:
    """
    A simple queue implementation with a maximum (bounded) size.

    Methods:
        - enqueue(item): Add item to the end of the queue. Raises QueueFullException if full.
        - dequeue(): Remove and return the item from the front. Raises QueueEmptyException if empty.
        - front(): Return the item at the front without removing it. Raises QueueEmptyException if empty.
        - is_empty(): Returns True if queue is empty.
        - is_full(): Returns True if queue is full.
    """

    def __init__(self, max_size):
        """
        Initialize the queue with a maximum size.
        :param max_size: int, the maximum number of items the queue can hold.
        """
        self._items = []
        self._max_size = max_size

    def enqueue(self, item):
        """
        Add an item to the back of the queue.

        :param item: The item to add.
        :raises QueueFullException: If the queue is already full.
        """
        if self.is_full():
            raise QueueFullException("Queue is full")
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.

        :raises QueueEmptyException: If the queue is empty.
        :return: The item removed from the queue.
        """
        if self.is_empty():
            raise QueueEmptyException("Queue is empty")
        return self._items.pop(0)

    def front(self):
        """
        Return the item at the front of the queue without removing it.

        :raises QueueEmptyException: If the queue is empty.
        :return: The item at the front of the queue.
        """
        if self.is_empty():
            raise QueueEmptyException("Queue is empty")
        return self._items[0]

    def is_empty(self):
        """Returns True if the queue is empty, False otherwise."""
        return len(self._items) == 0

    def is_full(self):
        """Returns True if the queue is full, False otherwise."""
        return len(self._items) >= self._max_size

    def __len__(self):
        """Returns the current number of items in the queue."""
        return len(self._items)

def run_user_defined_tests():
    """
    Interactive harness that lets the user supply their own test cases.

    Workflow:
        1. Prompt for maximum queue size.
        2. Prompt for number of test cases (operations) to run.
        3. For each test case, read an operation such as:
               enqueue <value>
               dequeue
               front
               is_empty
               is_full
               len
        4. Execute the operation, printing the outcome (or any exception encountered).
    """
    print("Queue Test Harness (User-Driven)")
    print("--------------------------------")

    # Step 1: queue capacity
    while True:
        try:
            max_size = int(input("Enter maximum queue size: "))
            if max_size <= 0:
                raise ValueError("Max size must be positive.")
            break
        except ValueError as exc:
            print(f"Invalid max size. {exc}")

    queue = Queue(max_size=max_size)

    # Step 2: number of operations
    while True:
        try:
            total_cases = int(input("Enter number of test cases (operations): "))
            if total_cases <= 0:
                raise ValueError("Number of test cases must be positive.")
            break
        except ValueError as exc:
            print(f"Invalid count. {exc}")

    print(
        "\nSupported commands:\n"
        "  enqueue <value>  -> enqueue a string payload\n"
        "  dequeue          -> dequeue and print the removed value\n"
        "  front            -> show the value at the front without removing it\n"
        "  is_empty         -> prints True/False\n"
        "  is_full          -> prints True/False\n"
        "  len              -> prints the current queue length\n"
    )

    # Step 3: process user-supplied operations
    for idx in range(1, total_cases + 1):
        raw = input(f"Test case {idx}: ").strip()
        if not raw:
            print(f"[{idx}] Skipped (blank input).")
            continue

        parts = raw.split(maxsplit=1)
        command = parts[0].lower()
        payload = parts[1] if len(parts) > 1 else None

        try:
            if command == "enqueue":
                if payload is None:
                    raise ValueError("enqueue requires a value, e.g., 'enqueue apple'.")
                queue.enqueue(payload)
                print(f"[{idx}] enqueue -> '{payload}' inserted.")

            elif command == "dequeue":
                removed = queue.dequeue()
                print(f"[{idx}] dequeue -> '{removed}' removed.")

            elif command == "front":
                front_val = queue.front()
                print(f"[{idx}] front -> '{front_val}'.")

            elif command == "is_empty":
                print(f"[{idx}] is_empty -> {queue.is_empty()}.")

            elif command == "is_full":
                print(f"[{idx}] is_full -> {queue.is_full()}.")

            elif command == "len":
                print(f"[{idx}] len -> {len(queue)}.")

            else:
                raise ValueError(
                    f"Unknown command '{command}'. "
                    "Use enqueue/dequeue/front/is_empty/is_full/len."
                )

        except (QueueFullException, QueueEmptyException, ValueError) as exc:
            print(f"[{idx}] Error: {exc}")

    print("\nAll user-supplied test cases processed.")


if __name__ == "__main__":
    run_user_defined_tests()


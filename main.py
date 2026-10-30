from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def check_balanced_parentheses(expression):
    """Return True when (), [], and {} are correctly balanced."""
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    opening = set(pairs.values())

    for character in expression:
        if character in opening:
            stack.append(character)
        elif character in pairs:
            if not stack or stack.pop() != pairs[character]:
                return False
    return len(stack) == 0


def print_queue_exercise():
    """Demonstrate print jobs being processed in FIFO order."""
    queue = LinkedQueue()
    print("\\nPRINT QUEUE SIMULATION")
    print("Enter print jobs. Leave the Job ID blank to stop adding jobs.")

    while True:
        job_id = input("Job ID: ").strip()
        if not job_id:
            break
        try:
            pages = int(input("Number of pages: "))
            if pages <= 0:
                print("Page count must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a whole number for pages.")
            continue
        queue.enqueue({"id": job_id, "pages": pages})
        print("Job added. Current queue:", queue)

    if queue.is_empty():
        print("No print jobs were added.")
        return

    print("\\nPrinting in FIFO order (first added, first printed):")
    order = 1
    while not queue.is_empty():
        job = queue.dequeue()
        print(f"{order}. Job {job['id']} - {job['pages']} page(s)")
        order += 1


def choose_structure():
    print("\\nChoose an implementation:")
    print("1. ArrayStack")
    print("2. LinkedStack")
    print("3. Circular ArrayQueue")
    print("4. LinkedQueue")
    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        capacity = read_capacity()
        return ArrayStack(capacity), "stack"
    if choice == "2":
        return LinkedStack(), "stack"
    if choice == "3":
        capacity = read_capacity()
        return ArrayQueue(capacity), "queue"
    if choice == "4":
        return LinkedQueue(), "queue"

    print("Invalid implementation choice.")
    return None, None


def read_capacity():
    while True:
        try:
            capacity = int(input("Enter capacity (positive whole number): "))
            if capacity > 0:
                return capacity
            print("Capacity must be greater than zero.")
        except ValueError:
            print("Please enter a whole number.")


def operate_structure(structure, kind):
    while True:
        print("\\nCurrent state:", structure)
        if kind == "stack":
            print("1. Push")
            print("2. Pop")
            print("3. Peek")
            print("4. Check if empty")
            print("5. Check if full")
        else:
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek front")
            print("4. Check if empty")
            print("5. Check if full")
        print("0. Return to main menu")
        choice = input("Choose operation: ").strip()

        try:
            if choice == "0":
                break
            elif choice == "1":
                value = input("Enter value: ")
                if kind == "stack":
                    structure.push(value)
                    print("Pushed:", value)
                else:
                    structure.enqueue(value)
                    print("Enqueued:", value)
            elif choice == "2":
                print("Removed:", structure.pop() if kind == "stack"
                      else structure.dequeue())
            elif choice == "3":
                print("Top element:" if kind == "stack" else "Front element:",
                      structure.peek() if kind == "stack"
                      else structure.peek_front())
            elif choice == "4":
                print("Is empty?", structure.is_empty())
            elif choice == "5":
                print("Is full?", structure.is_full())
            else:
                print("Invalid operation choice.")
        except (IndexError, OverflowError, ValueError) as error:
            print("ERROR:", error)

        print("State after operation:", structure)


def main():
    while True:
        print("\\n===== STACKS AND QUEUES LAB =====")
        print("1. Use a stack or queue implementation")
        print("2. Check balanced parentheses")
        print("3. Simulate a print queue")
        print("4. Demonstrate underflow and overflow")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            structure, kind = choose_structure()
            if structure is not None:
                operate_structure(structure, kind)
        elif choice == "2":
            expression = input("Enter an expression using (), [], or {}: ")
            if check_balanced_parentheses(expression):
                print("Result: Balanced parentheses.")
            else:
                print("Result: Not balanced.")
        elif choice == "3":
            print_queue_exercise()
        elif choice == "4":
            print("\\nTesting ArrayStack errors:")
            stack = ArrayStack(1)
            try:
                stack.pop()
            except IndexError as error:
                print("Underflow test:", error)
            stack.push("A")
            try:
                stack.push("B")
            except OverflowError as error:
                print("Overflow test:", error)

            print("\\nTesting ArrayQueue errors:")
            queue = ArrayQueue(1)
            try:
                queue.dequeue()
            except IndexError as error:
                print("Underflow test:", error)
            queue.enqueue("Job A")
            try:
                queue.enqueue("Job B")
            except OverflowError as error:
                print("Overflow test:", error)
        elif choice == "0":
            print("Program ended. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

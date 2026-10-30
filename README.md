# Stacks and Queues: Array vs. Linked List

## Description
This Python program demonstrates four data structures:
- `ArrayStack`: a fixed-size stack that follows LIFO.
- `LinkedStack`: a linked-list stack that follows LIFO.
- `ArrayQueue`: a fixed-size circular queue that follows FIFO.
- `LinkedQueue`: a linked-list queue that follows FIFO.

The program also checks balanced parentheses and simulates a print queue.

## Files
- `node.py` — shared node class.
- `array_stack.py` — array-based stack.
- `linked_stack.py` — linked-list stack.
- `array_queue.py` — circular array queue.
- `linked_queue.py` — linked-list queue.
- `main.py` — menu and test driver.
- `analysis.md` — written analysis answer.

## How to Run
1. Save all the Python files in the same folder.
2. Open a terminal or command prompt in that folder.
3. Run `python main.py` (on some computers, use `python3 main.py`).
4. Follow the menu instructions.

## Error Handling
The program reports stack/queue underflow when removing from an empty structure and overflow when adding to a full fixed-size array structure.

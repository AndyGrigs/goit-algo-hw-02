# Завдання 2
from collections import deque

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    deque_text = deque(text)
    while len(deque_text) > 1:
        if deque_text.popleft() != deque_text.pop():
            return False
    return True

print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("race a car"))  # False
print(is_palindrome("Was it a car or a cat I saw"))  # True

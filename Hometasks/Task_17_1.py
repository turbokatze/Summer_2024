import re
def duplicate_rem(sent):
    regex = r'\b(\w+)(?:\W+\1\b)+'; return re.sub(regex, r'\1', sent, flags=re.IGNORECASE)
print('Введите текст: ', end=""); print(f'Удалены повторения слов: {duplicate_rem(input())}')
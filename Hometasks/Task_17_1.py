from re import sub, IGNORECASE
def duplicate_rem(sent):
    re = r'\b(\w+)(?:\W+\1\b)+'; return sub(re, r'\1', sent, flags=IGNORECASE)
print('Введите текст: ', end=""); print(f'Удалены повторения слов: {duplicate_rem(input())}')
from pathlib import Path
path_common_words = Path('10/siddhartha.txt')
common_words = path_common_words.read_text(encoding='utf-8')
print(common_words.count('the'))
print(common_words.lower().count('the'))


text = input()
vowels = {'a','o', 'u', 'e', 'i', 'O', 'U', 'E', 'I', 'A'}
no_vowels = [ch for ch in text if ch not in vowels]
print(''.join(no_vowels))
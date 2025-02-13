from audioop import reverse
from zipfile import stringEndArchive64Locator

str = "My name is tanvin"
str=str.split()

reverse_word =[s[::-1] for s in str]

result_reverse= " ".join(reverse_word)

print(result_reverse)
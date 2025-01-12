# Имеется строка вида: AABABBAABBBAB. Необходимо написать функцию, которая заменит буквы A на B, и B,
# соответственно, на A. Замену можно производить ТОЛЬКО используя функцию replace(). В результате применения
# функции к исходной строке, функция должна вернуть строку: BBABAABBAAABA
# Использовать циклы и оператор IF запрещено.

line_original = 'AABABBAABBBAB'
replacements = {'A':'B', 'B':'A'}
result = "".join(replacements.get(char, char) for char in line_original)

print(result)

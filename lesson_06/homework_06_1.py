checked_string = input("Введите необходимую строку: \n")
uniq_chars = set(checked_string)
for i in (checked_string):
    if i not in uniq_chars:
        uniq_chars.append(i)
if len(uniq_chars) > 10:
    print('True')
else:
    print('False')



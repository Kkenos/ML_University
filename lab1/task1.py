
s = 'Pyth1abch2hon'


first_h = s.find('h')
last_h = s.rfind('h')

print(first_h)
print(last_h)


result = s[:first_h + 1] + s[first_h + 1:last_h][::-1] + s[last_h:]


print(result)
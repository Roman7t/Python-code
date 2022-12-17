17 lines (16 sloc)  335 Bytes

#menurestorana cristal: group
person = {}
s = "menurestorana cristal pate"
s = s.split()
person['lastName'] = s[0]
person['Restoran'] = s[1]
person['Coldappetizer'] = s[2]
person['marks'] = []
for i in s [2:]:
    person['marks'] .append (i)
print(person)

#d = {
        #key:value
#1: 'one',
#2: 'two',
#3: 'three',

import pprint
message = 'it was a bright cold day in April, and the clock was thirteen'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

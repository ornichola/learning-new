phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist = plist[1:8] # on't pa
plist.remove('\'') # ont pa
plist.insert(2, plist.pop(3)) # on tpa
plist.extend([plist.pop(), plist.pop()]) # on tap
new_phrase = ''.join(plist)

print(plist)
print(new_phrase) # on tap

'''
# authors solution
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])
'''

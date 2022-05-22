s = {}
a = input('please enter your language name: ')
b = input ('Please enter your second language name: ')
c = input ('Please enter your third  language name: ')
d = input ('Please enter your fourth language name: ')

#one way to approach
supdate = {      
 'surya': a,
 'kairav': b,
 'om': c,
 'shankar': d,
}
s.update(supdate)

#second way to approach
s['surya'] = a
s['kairav'] = b
s['om'] = c
s['shankar'] = d

print (s)
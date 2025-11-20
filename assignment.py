guest=['Vitanuel','Dani','Alma']

print(guest)

print('Hi', guest[0],'i am inviting you over for dinner.')

print('Hi', guest[1],'i am inviting you over for dinner.')

print('Hi', guest[2],'i am inviting you over for dinner.')

people=['Vitanuel','Dani','Alma']#original list of guest invited

print('unfortunately', {guest[1]}, 'cant make it.')#printing a guest cant make it

guest[1]='Andriana'

print(guest)#printing the new guest list
print('\nHi', guest[0],'you are still invited over for dinner.')
print('Hi', guest[1],'you are still invited over for dinner.')
print('Hi', guest[2],'you are still invited over for dinner.')#printing another invite letter
print('\ngoodnews i found a bigger table')
guest.insert(0,'Sintich')#adds the neme at index position 0
guest.insert(2,'Thierry')#adds the name at index position 2
guest.append('Api')#adding the name at the end of th list
print(guest)
print('\nHi', guest[0],'you are invited over for the expanded dinner.')
print('Hi', guest[2],'you are invited over for the expanded dinner.')
print('Hi', guest[3],'you are invited over for the expanded dinner.')
print('Hi', guest[4],'you are invited over for the expanded dinner.')
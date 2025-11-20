locations=['Korea','Canada','USA','Japan','Italy']
print('original order:',locations)#prints list in original order
locations.sort()#arranges the list in alphabetical order
print('alphabetical order:',locations)
locations=['Korea','Canada','USA','Japan','Italy']
print('original order:',locations)#prints the original list again
locations.sort(reverse=True)
print('reverse order:',locations)#reverses the list
locations.reverse()
print('reversed again:',locations)#reverses the list again which now goes back to the original form

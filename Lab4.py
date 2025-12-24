#7.8
sandwich_orders=['chicken sandwich','veggie sandwich','beef sandwich','cheese sandwich','egg sandwich']
finished_sandwiches=[]
while sandwich_orders:
    current_sandwich=sandwich_orders.pop(0)
    print(f"- I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
print("\nsandwiches made: ")
for sandwich in finished_sandwiches:
    print("-",sandwich)



#7.9
sandwich_orders=['chicken sandwich','pastrami sandwich','veggie sandwich','cheese sandwich','pastrami sandwich']
finished_sandwiches=[]
print("\n * sorry,the deli has run out of pastrami sandwich.\n")
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
while sandwich_orders:
    current_sandwich=sandwich_orders.pop(0)
    print(f"- I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
print("\nfinished sandwiches:")
for sandwich in finished_sandwiches:
    print("-",sandwich)
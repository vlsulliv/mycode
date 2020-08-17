#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Monk Temple' : { 
                  'south' : 'Training Room',
                  'east'  : 'Dining Room',
                  'item'  : 'manuscript'
                },

          'Training Room' : {
                  'north' : 'Monk Temple',
                  'item'  : 'demon',
                },
            'Dining Room' : {
                  'west' : 'Monk Temple',
                  'south': 'War Camp',
                  'item' : 'potion'
               },
            'War Camp' : {
                  'north' : 'Dining Room',
                  'south' : 'Forest'
               },
            'Forest' : {
                  'north' : 'Garden',
                  'item'  : 'scroll'
               },
         }  


#start the player in the Hall
currentRoom = 'Monk Temple'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
  
  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  
  #read manuscript
  if move[0] == 'get' :
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      print("Once upon a time, gods walked the earth. These powerful beings, ruled by a godking, are at constant war with demons. The god kind was framed as a traitor and banished, allowing the demons to strike and overpower the gods. To resurrect the the god king you need to find 6 scrolls scattered around the earth.")

## If a player enters a room with a monster
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break

## Define how a player can win
  if currentRoom == 'Forest' and 'key' in inventory and 'potion' in inventory and 'scroll'   in inventory:
    print('You escaped the house with the ultra rare key and magic potion and a scroll... YOU WIN!')
    break


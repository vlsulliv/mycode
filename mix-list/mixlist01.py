#!/usr/bin/env python3


 # create a list with 3 items
my_list = [ "192.168.0.5", 5060, "UP"]

 # display item 1 
print("The first item in the list (IP): " + my_list[0] )

 # display item 2 
print("The second item in the list (port): " + str(my_list[1]) )

 
 # display item 3
print("The last item in the list (state): " + my_list[2] )

 # insert new list with 6 elements 
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]



print("when I" +  new_list[5] +  " into IP addresses " + new_list[3])
print("or " + new_list[4] +  " I am unable to ping ports")
print(str(new_list[0]) + ", " + new_list[1] + ", or" + str(new_list[2]))


# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to _______"

#youtuber = "" # some string varible

# a few ways to do this
#print("Subscribe to " + youtuber)
#print("Subscribe to {}".format(youtuber))
#print(f"Subscribe to {youtuber}")

twice_mem = input("Member of Twice: ")
what = input("What?: ")
action = input("Action: ")

madlib = f"No {twice_mem} No {what}, Shy shy shy oppa ah unnie ah you can't {action} without {twice_mem}"

print(madlib)
from start import *

print("Battle!")
answer = input("Start Game? [Y/n]")
if answer == "n":
    print("closing...")
else:
    print("\nIf you see this symbol: [ > ], press ENTER to continue.")
    print("------------------------------------------------------\n")
    start()

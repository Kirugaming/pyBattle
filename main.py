from start import start

print("Battle!")
answer = input("Start Game? [Y/n]")
if answer == "n":
    print("closing...")
else:
    print("start")
    start()

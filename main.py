import time
import pyjokes

# IT GENERATES NUMBERS OF JOKE YOU WANT
# DEVELOPED BY RITURAJ
print("JOKE GENERATOR DEVELOPED BY RITURAJ")

def generate_joke():
    rituraj = int(input("Number of jokes you want: "))
    for i in range(rituraj):
        print(pyjokes.get_joke())
        print()
        time.sleep(1)

generate_joke()

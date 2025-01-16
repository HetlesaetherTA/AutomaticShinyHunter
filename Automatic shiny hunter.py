import keyboard
import time
from PIL import ImageGrab

with open("C:/Users/Norsk/Documents/Coding/Coding/Portfolio/Python/Automatic shiny hunter/mewtwo.txt", "r") as counter:
    line = counter.readline()
    lines = line.split(" ")

srs = lines[0]
srs = int(srs)
mewtwo_cordinate = 495, 149
trainer_cordinate = 127, 210
mewtwo = (182, 77, 239)
shiny_mewtwo = (166, 231, 93)
in_battle = False
shiny = False
b = 10
print("Prepping")
time.sleep(2)
lol = 100
repeat = 15
print("Start")

while True:
    while True:
        image = ImageGrab.grab(bbox=(650, 100, 1200, 500))
        keyboard.press("e")
        time.sleep(0.1)
        keyboard.release("e")
        time.sleep(0.1)
        repeat -= 1
        pixeldata = image.getpixel(mewtwo_cordinate)
        if pixeldata == mewtwo:
            break
        if pixeldata == shiny_mewtwo:
            with open("C:/Users/Norsk/Documents/Coding/Coding/Portfolio/Python/Automatic shiny hunter/mewtwo.txt", "w") as counter_with_shiny:
                counter_with_shiny.write(f"You found a shiny after {srs}!")
            print(f"""
------------------

You found a shiny after {srs} encounters!!""")
            shiny = True
            time.sleep(12)
            keyboard.press("s")
            time.sleep(0.4)
            keyboard.release("s")
            time.sleep(0.4)
            keyboard.press("s")
            time.sleep(0.4)
            keyboard.release("s")
            time.sleep(0.4)
            keyboard.press("e")
            time.sleep(0.4)
            keyboard.release("e")
            time.sleep(0.4)
            keyboard.press("d")
            time.sleep(0.4)
            keyboard.release("d")
            time.sleep(0.4)
            keyboard.press("e")
            time.sleep(0.4)
            keyboard.release("e")
            time.sleep(0.4)
            keyboard.press("e")
            time.sleep(0.4)
            keyboard.release("e")
            time.sleep(0.4)
            keyboard.press("e")
            time.sleep(0.4)
            keyboard.release("e")
            time.sleep(14)
            print("Mewtwo was caught")
            time.sleep(10)
            time.sleep(0.4)
            keyboard.press("e")
            time.sleep(0.4)
            keyboard.release("e")
            time.sleep(2)
            keyboard.press("s")
            time.sleep(0.4)
            keyboard.release("s")
            time.sleep(0.4)
            keyboard.press("e")
            time.sleep(0.4)
            keyboard.release("e")
            time.sleep(3)
            keyboard.press("q")
            time.sleep(0.4)
            keyboard.release("q")
            time.sleep(0.4)
            keyboard.press("d")
            time.sleep(0.4)
            keyboard.release("d")
            time.sleep(0.4)
            keyboard.press("s")
            time.sleep(0.4)
            keyboard.release("s")
            time.sleep(0.4)
            keyboard.press("e")
            time.sleep(0.4)
            keyboard.release("e")
            time.sleep(0.4)
            keyboard.press("e")
            time.sleep(0.4)
            keyboard.release("e")
            time.sleep(2)
            keyboard.press("e")
            time.sleep(0.4)
            keyboard.release("e")
            time.sleep(2)
            keyboard.press("e")
            time.sleep(0.4)
            keyboard.release("e")
            print("-- saving --")
            time.sleep(25)
            keyboard.press("q")
            time.sleep(0.4)
            keyboard.release("q")
            print("Saved")
            break
    if shiny is True:
        break
    else:
        srs += 1
        keyboard.press("u")
        keyboard.press("i")
        keyboard.press("o")
        keyboard.press("p")
        time.sleep(1)

        keyboard.release("u")
        keyboard.release("i")
        keyboard.release("o")
        keyboard.release("p")
        with open("C:/Users/Norsk/Documents/Coding/Coding/Portfolio/Python/Automatic shiny hunter/mewtwo.txt", "w") as counter_no_shiny:
            counter_no_shiny.write(f"{srs} Soft resets done!")

        print(f"{srs} Soft resets done!")
print(input("""

------------------
Press enter to end
------------------"""))

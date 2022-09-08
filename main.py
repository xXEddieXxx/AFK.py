import mouse
import time


class Main:
    print("20 min Afk Script")

    for i in range(20):
        mouse.move(100, 100, 100, 0.2)
        mouse.move(50, 50, 50, 0.2)
        time.sleep(60)

        print(i, " minutes over")

    input("Time is Over, press enter to exit")

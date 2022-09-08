import mouse
import time


class Main:
    print("20 min Afk Script")

    for i in range(20):
        mouse.move(1000, 500, 1000, 0.2)
        mouse.move(900, 500, 1000, 0.2)
        mouse.move(1000, 600, 1000, 0.2)
        mouse.move(1000, 500, 900, 0.2)
        mouse.move(1000, 400, 1000, 0.2)
        time.sleep(60)

        print(i, " minutes over")

    input("Time is Over, press enter to exit")

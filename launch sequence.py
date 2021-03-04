import time

def main():
    print("Falcon 9 start up")
    time.sleep(3)
    print("Systems Check: ")
    time.sleep(3)
    print("All systems nominal. Go for Launch")
    time.sleep(2)
    print("System has control. Countdown sequence commence")
    time.sleep(1)
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)

    print("Ignition")
    time.sleep(2)
    print ("Lift Off")
    time.sleep(2)
    print("Falcon has cleared the tower")
    time.sleep(3)
    print ("Falcon 9 is supersonic")
    time.sleep(3)
    print ("Falcon 9 is experiencing maximum aerodynamic pressure")
    time.sleep(3)
    print ("Main engine cut off")
    time.sleep(1)
    print ("Stage separation confirmed")

if __name__ == "__main__": main()
from multiprocessing import Process
import time

def brew_coffe(flavour):
    print(f"Started brewing {flavour} coffe")
    time.sleep(3)
    print(f"Finished brewing {flavour} coffe")


def main():
    coffe_brewer = [
        Process(target=brew_coffe, args=(f"Coffe maker #{i + 1}", ))
        for i in range(3)
    ]

    for brewer in coffe_brewer:
        brewer.start()

    for brewer in coffe_brewer:
        brewer.join()

    print("All Coffe Served!!")


if __name__ == "__main__":
    main()


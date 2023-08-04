import server
import model
import pandas as pd


def spinUp():
    print("Spinned up")


def main():
    model.runModel()

    spinUp()
    server.init_server()

    print("\nMain run\n")


if __name__ == "__main__":
    main()
else:
    print("\nApp Not Runneed Correctly\n")
    exit(0)

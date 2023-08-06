import src.server as ser
import src.model as mod
import src.model2 as mod2
import settings
settings


# The main function where execution takes place
def main():
    # Models
    s = mod.valueString()
    c = mod2.valueString()
    print(s, c)

    # Server
    ser.init_server()

    # Shutdown cleanup
    print("\nGracefully shutting down...\n")
    print("\nRunning cleanup tasks\n")


if __name__ == "__main__":
    main()
else:
    print("\nApp Not Runneed Correctly\n")
    exit(0)

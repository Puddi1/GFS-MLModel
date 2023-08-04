import server
import model
import model2

# The main function where execution takes place


def main():
    # Models
    s = model.valueString()
    c = model2.valueString()
    # Server
    server.init_server()

    print("Gracefully shutting down...")
    print(s, c)


if __name__ == "__main__":
    main()
else:
    print("\nApp Not Runneed Correctly\n")
    exit(0)

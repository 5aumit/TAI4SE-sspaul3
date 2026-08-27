from src.MultiValueDictApp import MultiValueDictApp

def main():
    app = MultiValueDictApp()
    print("Welcome to Multivalue Dictionary App")
    print("COMMANDS and format:")
    print("KEYS")
    print("MEMBERS key")
    print("ADD key value")
    print("REMOVE key value")
    print("REMOVEALL key")
    print("CLEAR")
    print("KEYEXISTS key")
    print("VALUEEXISTS key value")
    print("ALLMEMBERS")
    print("ITEMS")
    print("EXIT")
    print("Enter COMMAND key value below")
    print("---------------------------------------")
    print("")

    while True:
        command, *args = input().split(' ')
        app.run(command, args)

if __name__ == "__main__":
    main()
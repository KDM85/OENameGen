import OENameGen
import OEPlaceNameGen


def main():
    print("Generate name or place name?")
    choice = input("1 for name, 2 for place name: ")
    if choice == "1":
        keepGoing = "y"
        while keepGoing == "y":
            gender = input("\nSelect a gender (M/F or Q to quit): ")
            if gender.upper() in ("M", "F"):
                print(OENameGen.GetName(gender))
            elif gender.upper() == "Q":
                keepGoing = "n"
                quit()
    elif choice == "2":
        keepGoing = "y"
        while keepGoing == "y":
            print(OEPlaceNameGen.GetPlaceName())
            cont = input("\nGet another place name? (Y/N): ")
            if cont.upper() != "Y":
                keepGoing = "n"
                quit()


if __name__ == "__main__":
    main()

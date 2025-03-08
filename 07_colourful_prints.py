from colorama import Fore, Style

def print_christmas_tree():
    print(Fore.GREEN + "   *   ")
    print("  ###  ")
    print(" ##### ")
    print("#######" + Style.RESET_ALL)
    print(Fore.RED + "   |   " + Style.RESET_ALL)

print_christmas_tree()

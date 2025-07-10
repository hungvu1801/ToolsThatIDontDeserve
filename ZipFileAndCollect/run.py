from src.menu import clear_console, display_menu, run_command

def main() -> None:
    while True:
        clear_console()
        display_menu()
        user_input = input("Please choose options: ")
        res = run_command(user_input)
        if not res:
            break

if __name__ == '__main__':
    main()
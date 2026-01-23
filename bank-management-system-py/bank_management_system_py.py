import os
import time
from typing import Dict, Union, Optional

# ────────────────────────────────────────────────
# Data
# ────────────────────────────────────────────────

accounts: Dict[int, Dict[str, Union[str, float]]] = {}
current_account_number: Optional[int] = None


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def next_account_number() -> int:
    return len(accounts) + 1


def create_account(name: str, initial_balance: float) -> int:
    name = name.strip()
    if not name:
        raise ValueError("Please enter a name")
    if initial_balance < 0:
        raise ValueError("Initial deposit cannot be negative")

    number = next_account_number()
    accounts[number] = {
        'name': name,
        'balance': float(initial_balance)
    }
    return number


def get_account(number: int) -> Dict[str, Union[str, float]]:
    if number not in accounts:
        raise KeyError(f"Account #{number} not found")
    return accounts[number]


def deposit(number: int, amount: float) -> float:
    if amount <= 0:
        raise ValueError("Please enter an amount greater than zero")
    account = get_account(number)
    account['balance'] += amount
    return account['balance']


def withdraw(number: int, amount: float) -> float:
    if amount <= 0:
        raise ValueError("Please enter an amount greater than zero")
    account = get_account(number)
    if account['balance'] < amount:
        raise ValueError(f"Insufficient funds • Available: {account['balance']:,.2f}")
    account['balance'] -= amount
    return account['balance']


# ────────────────────────────────────────────────
# UI Helpers
# ────────────────────────────────────────────────

def print_header() -> None:
    clear_screen()
    print("")

    if current_account_number and current_account_number in accounts:
        acc = accounts[current_account_number]
        print("  " + "─" * 46)
        print(f"  Account #{current_account_number}")
        print(f"  {acc['name']}")
        print(f"  Balance  {acc['balance']:,.2f}")
        print("  " + "─" * 46)
    else:
        print("  " + "─" * 46)
        print("  No account selected")
        print("  " + "─" * 46)

    print("")


def print_menu() -> None:
    print("  1. Create new account")
    print("  2. Switch account")
    print("  3. Deposit")
    print("  4. Withdraw")
    print("  5. View balance details")
    print("  6. Quit")
    print("")


def pause(seconds: float = 1.8) -> None:
    time.sleep(seconds)


# ────────────────────────────────────────────────
# Actions
# ────────────────────────────────────────────────

def action_create_account() -> None:
    print_header()
    print("  New Account\n")
    name = input("  Full name: ").strip()

    try:
        initial = float(input("  Initial deposit: "))
        number = create_account(name, initial)
        global current_account_number
        current_account_number = number

        print_header()
        print("  Account created successfully\n")
        print(f"  Number     {number}")
        print(f"  Holder     {name}")
        print(f"  Balance    {initial:,.2f}\n")
        pause(2.8)

    except ValueError as e:
        print(f"\n  {e}\n")
        pause()


def action_select_account() -> None:
    print_header()

    if not accounts:
        print("  No accounts yet. Create one first.\n")
        pause()
        return

    print("  Existing accounts\n")
    for num, data in sorted(accounts.items()):
        print(f"  {num:3d}   {data['name']:<24} {data['balance']:>12,.2f}")

    print("")
    try:
        num = int(input("  Account number: "))
        get_account(num)  # validate
        global current_account_number
        current_account_number = num
        print_header()
        print("  Account switched\n")
        pause(1.4)
    except (ValueError, KeyError) as e:
        print(f"\n  {e}\n")
        pause()


def action_deposit() -> None:
    print_header()
    print("  Deposit\n")
    try:
        amount = float(input("  Amount: "))
        new_balance = deposit(current_account_number, amount)  # type: ignore
        print(f"\n  Deposited {amount:,.2f}")
        print(f"  New balance {new_balance:,.2f}\n")
        pause()
    except ValueError as e:
        print(f"\n  {e}\n")
        pause()


def action_withdraw() -> None:
    print_header()
    print("  Withdraw\n")
    try:
        amount = float(input("  Amount: "))
        new_balance = withdraw(current_account_number, amount)  # type: ignore
        print(f"\n  Withdrew {amount:,.2f}")
        print(f"  New balance {new_balance:,.2f}\n")
        pause()
    except ValueError as e:
        print(f"\n  {e}\n")
        pause()


def action_show_details() -> None:
    print_header()
    acc = get_account(current_account_number)  # type: ignore
    print("  Account Details\n")
    print(f"  Number     {current_account_number}")
    print(f"  Holder     {acc['name']}")
    print(f"  Balance    {acc['balance']:,.2f}\n")
    input("  Press Enter to continue ")


# ────────────────────────────────────────────────
# Main Loop
# ────────────────────────────────────────────────

def main() -> None:
    global current_account_number

    while True:
        print_header()
        print_menu()

        choice = input("  → ").strip()

        if choice == "1":
            action_create_account()

        elif choice == "2":
            action_select_account()

        elif choice in ("3", "4", "5"):
            if current_account_number is None:
                print_header()
                print("  Please select an account first\n")
                pause(2)
                continue

            if choice == "3":
                action_deposit()
            elif choice == "4":
                action_withdraw()
            elif choice == "5":
                action_show_details()

        elif choice == "6":
            clear_screen()
            print("\n  Thank you for using Simple Banking.\n")
            print("  Goodbye.\n")
            break

        else:
            print_header()
            print("  Please choose 1–6\n")
            pause(1.4)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("\n  Goodbye.\n")
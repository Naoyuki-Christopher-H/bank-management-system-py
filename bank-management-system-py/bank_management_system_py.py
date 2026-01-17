import os
import time
from typing import Dict, Union, Optional

# Global storage for all accounts
accounts: Dict[int, Dict[str, Union[str, float]]] = {}

# Currently selected / working account (for nicer UX)
current_account_number: Optional[int] = None


def clear_screen() -> None:
    """Clear the terminal screen (works on Windows, macOS, Linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_account_number() -> int:
    """Generate next sequential account number."""
    return len(accounts) + 1


def create_account(name: str, initial_balance: float) -> int:
    """Create new account. Returns account number."""
    if not name.strip():
        raise ValueError("Name cannot be empty")
    if initial_balance < 0:
        raise ValueError("Initial balance cannot be negative")

    acc_num = generate_account_number()
    accounts[acc_num] = {
        'name': name.strip(),
        'balance': float(initial_balance)
    }
    return acc_num


def get_account(acc_num: int) -> Dict[str, Union[str, float]]:
    """Get account data or raise KeyError if not found."""
    if acc_num not in accounts:
        raise KeyError(f"Account #{acc_num} does not exist")
    return accounts[acc_num]


def deposit(acc_num: int, amount: float) -> float:
    """Deposit money. Returns new balance."""
    if amount <= 0:
        raise ValueError("Deposit amount must be positive")
    acc = get_account(acc_num)
    acc['balance'] += amount
    return acc['balance']


def withdraw(acc_num: int, amount: float) -> float:
    """Withdraw money. Returns new balance."""
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    acc = get_account(acc_num)
    if acc['balance'] < amount:
        raise ValueError(f"Insufficient funds (available: {acc['balance']:.2f})")
    acc['balance'] -= amount
    return acc['balance']


def show_header() -> None:
    """Display program title and current account (if selected)."""
    print("═" * 50)
    print("          SIMPLE BANKING SYSTEM          ")
    print("═" * 50)

    if current_account_number and current_account_number in accounts:
        acc = accounts[current_account_number]
        print(f"Current account: #{current_account_number}")
        print(f"  Holder : {acc['name']}")
        print(f"  Balance: {acc['balance']:,.2f}")
    else:
        print("No account selected")
    print("═" * 50)
    print()


def show_menu() -> None:
    """Display main menu options."""
    print("  1. Create new account")
    print("  2. Select / switch account")
    print("  3. Deposit money")
    print("  4. Withdraw money")
    print("  5. Check balance (detailed)")
    print("  6. Exit")
    print("-" * 50)


def main():
    global current_account_number

    while True:
        clear_screen()
        show_header()
        show_menu()

        try:
            choice = input("Enter choice (1-6): ").strip()

            if choice == '1':
                clear_screen()
                show_header()
                name = input("Full name: ").strip()
                try:
                    initial = float(input("Initial deposit amount: "))
                    acc_num = create_account(name, initial)
                    current_account_number = acc_num   # auto-select new account
                    clear_screen()
                    show_header()
                    print("╔════════════════════════════════════╗")
                    print("║         ACCOUNT CREATED            ║")
                    print("╚════════════════════════════════════╝")
                    print(f"  Account number : {acc_num}")
                    print(f"  Holder          : {name}")
                    print(f"  Balance         : {initial:,.2f}")
                    print()
                except ValueError as e:
                    print(f"Error: {e}")
                time.sleep(2.5)

            elif choice == '2':
                clear_screen()
                show_header()
                if not accounts:
                    print("No accounts exist yet. Create one first.")
                else:
                    print("Existing accounts:")
                    for num, data in sorted(accounts.items()):
                        print(f"  #{num:3d}  {data['name']:<20}  {data['balance']:>12,.2f}")
                    print()
                    try:
                        num = int(input("Enter account number to select: "))
                        get_account(num)  # validate
                        current_account_number = num
                        clear_screen()
                        show_header()
                        print("Account switched successfully.")
                    except (ValueError, KeyError) as e:
                        print(f"Error: {e}")
                time.sleep(2)

            elif choice in ('3', '4', '5'):
                if current_account_number is None:
                    clear_screen()
                    show_header()
                    print("No account selected! Please select an account first (option 2).")
                    time.sleep(2.5)
                    continue

                clear_screen()
                show_header()

                if choice == '3':
                    try:
                        amt = float(input("Amount to deposit: "))
                        new_bal = deposit(current_account_number, amt)
                        print(f"Successfully deposited {amt:,.2f}")
                        print(f"New balance: {new_bal:,.2f}")
                    except ValueError as e:
                        print(f"Error: {e}")
                    time.sleep(2)

                elif choice == '4':
                    try:
                        amt = float(input("Amount to withdraw: "))
                        new_bal = withdraw(current_account_number, amt)
                        print(f"Successfully withdrew {amt:,.2f}")
                        print(f"New balance: {new_bal:,.2f}")
                    except ValueError as e:
                        print(f"Error: {e}")
                    time.sleep(2)

                elif choice == '5':
                    acc = get_account(current_account_number)
                    print("Balance details:")
                    print(f"  Account  : #{current_account_number}")
                    print(f"  Holder   : {acc['name']}")
                    print(f"  Balance  : {acc['balance']:,.2f}")
                    print()
                    input("Press Enter to continue...")

            elif choice == '6':
                clear_screen()
                print("Thank you for using Simple Banking System.")
                print("Goodbye!\n")
                break

            else:
                print("Invalid choice. Please enter 1–6.")
                time.sleep(1.8)

        except KeyboardInterrupt:
            clear_screen()
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            clear_screen()
            show_header()
            print(f"Unexpected error: {e}")
            time.sleep(3)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("Goodbye.")
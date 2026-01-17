from typing import Dict, Union

# Global dictionary to store all accounts
# Key: account number (int), Value: {'name': str, 'balance': float}
accounts: Dict[int, Dict[str, Union[str, float]]] = {}


def generate_account_number() -> int:
    """Generate a simple sequential account number."""
    return len(accounts) + 1


def create_account(name: str, initial_balance: float) -> int:
    """
    Create a new bank account and return the assigned account number.
    Raises ValueError if initial balance is negative.
    """
    if initial_balance < 0:
        raise ValueError("Initial balance cannot be negative")

    account_number = generate_account_number()
    accounts[account_number] = {'name': name.strip(), 'balance': initial_balance}
    return account_number


def get_account(account_number: int) -> Dict[str, Union[str, float]]:
    """
    Retrieve account by number.
    Raises KeyError if account does not exist.
    """
    if account_number not in accounts:
        raise KeyError(f"Account {account_number} does not exist")
    return accounts[account_number]


def deposit(account_number: int, amount: float) -> float:
    """Deposit money into an account. Returns new balance."""
    if amount <= 0:
        raise ValueError("Deposit amount must be positive")

    account = get_account(account_number)
    account['balance'] += amount
    return account['balance']


def withdraw(account_number: int, amount: float) -> float:
    """
    Withdraw money from an account.
    Returns new balance on success.
    Raises ValueError on insufficient funds or invalid amount.
    """
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")

    account = get_account(account_number)

    if account['balance'] < amount:
        raise ValueError("Insufficient funds")

    account['balance'] -= amount
    return account['balance']


def check_balance(account_number: int) -> float:
    """Return the current balance of the specified account."""
    return get_account(account_number)['balance']


def main():
    """Main program loop with menu-driven interface."""
    while True:
        print("\n" + "="*40)
        print("          Simple Banking System")
        print("="*40)
        print("1. Create new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Exit")
        print("-"*40)

        try:
            choice = input("Enter your choice (1-5): ").strip()

            if choice == '1':
                name = input("Enter account holder's name: ").strip()
                if not name:
                    print("Name cannot be empty!")
                    continue

                initial = float(input("Enter initial balance: "))
                acc_num = create_account(name, initial)
                print(f"\nSUCCESS: Account created!")
                print(f"  Account Number : {acc_num}")
                print(f"  Holder         : {name}")
                print(f"  Initial Balance: {initial:.2f}\n")

            elif choice == '2':
                acc_num = int(input("Enter account number: "))
                amount = float(input("Enter deposit amount: "))
                new_balance = deposit(acc_num, amount)
                name = get_account(acc_num)['name']
                print(f"\nSUCCESS: Deposited {amount:.2f}")
                print(f"  Account: {acc_num} - {name}")
                print(f"  New balance: {new_balance:.2f}\n")

            elif choice == '3':
                acc_num = int(input("Enter account number: "))
                amount = float(input("Enter withdrawal amount: "))
                new_balance = withdraw(acc_num, amount)
                name = get_account(acc_num)['name']
                print(f"\nSUCCESS: Withdrew {amount:.2f}")
                print(f"  Account: {acc_num} - {name}")
                print(f"  New balance: {new_balance:.2f}\n")

            elif choice == '4':
                acc_num = int(input("Enter account number: "))
                balance = check_balance(acc_num)
                name = get_account(acc_num)['name']
                print(f"\nAccount: {acc_num} - {name}")
                print(f"Current balance: {balance:.2f}\n")

            elif choice == '5':
                print("\nThank you for using the banking system. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.\n")

        except ValueError as e:
            print(f"\nError: {e}\n")
        except KeyError as e:
            print(f"\nError: {e}\n")
        except Exception as e:
            print(f"\nUnexpected error: {e}\nPlease try again.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Goodbye!")

# Bank Management System (Python)

A simple console-based banking application written in Python that demonstrates core banking operations using in-memory storage.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Program Flow and Navigation](#program-flow-and-navigation)
- [Data Structure](#data-structure)
- [Design Decisions and Improvements](#design-decisions-and-improvements)
- [Limitations](#limitations)
- [Possible Future Enhancements](#possible-future-enhancements)

## Overview

This project implements a basic banking system with account 
creation, deposit, withdrawal, balance inquiry, and account 
selection features.  All data is stored in memory (in a Python 
dictionary) and is lost when the program terminates.  

The interface uses a clean, refreshing terminal layout 
(screen is cleared between operations) rather than continuous 
scrolling output, providing a more app-like experience in the console.

## Features

- Create new bank accounts with name and initial deposit
- Select/switch between existing accounts
- Deposit funds
- Withdraw funds (with sufficient balance validation)
- Check current balance with account details
- Persistent display of currently selected account information
- Input validation and meaningful error messages
- Clean screen refresh after each major action
- Graceful handling of Ctrl+C termination

## Requirements

- Python 3.6+
- No external packages required (only uses built-in modules: `os`, `time`, `typing`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Naoyuki-Christopher-H/bank-management-system-py.git
   cd bank-management-system-py
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```

No further dependencies need to be installed.

## Usage

Run the program with:

```bash
python main.py
```

(or `python3 main.py` on some systems)

The application starts immediately with a refreshed menu interface.

## Program Flow and Navigation

1. **Main Menu** options:
   - 1. Create new account
   - 2. Select / switch account
   - 3. Deposit money
   - 4. Withdraw money
   - 5. Check balance (detailed)
   - 6. Exit

2. **Behavior highlights**:
   - After creating an account, it is automatically selected
   - Deposit, withdraw, and balance check require an account to be selected first
   - Invalid inputs (negative amounts, non-existent accounts, insufficient funds) show clear error messages
   - Screen is cleared before showing success/error results or returning to menu
   - Current account details (number, name, balance) are shown at the top of every screen

## Data Structure

Accounts are stored in a global dictionary:

```python
accounts: Dict[int, Dict[str, Union[str, float]]] = {}
# Example entry:
# 1: {'name': 'John Doe', 'balance': 1500.75}
```

Account numbers are simple sequential integers starting from 1.

## Design Decisions and Improvements

Compared to a basic version, this implementation includes:

- Separation of concerns (helper functions: `get_account`, `deposit`, `withdraw`, etc.)
- Comprehensive exception handling (ValueError, KeyError)
- Type hints for better readability and IDE support
- Screen clearing (`os.system('cls' if os.name == 'nt' else 'clear')`) for improved UX
- Current account tracking to avoid repeated account number entry
- Formatted currency output (`:,.2f`)
- Short pauses after feedback messages so users can read them
- Graceful Ctrl+C handling

## Limitations

- Data is **not persistent** — all accounts disappear when the program closes
- No authentication (PIN, password)
- No transaction history or audit trail
- Simple sequential account numbering (not realistic banking format)
- Single-user / in-memory only — not suitable for concurrent access
- No overdraft protection or negative balance support

## Possible Future Enhancements

- Save/load accounts to/from JSON or SQLite file
- Add transaction history logging per account
- Implement account PIN or password protection
- Support transfers between accounts
- Generate more realistic account numbers (e.g., 10-digit random)
- Add overdraft facility with configurable limit
- Export account statement to text/CSV
- Basic search/filter accounts by name
- Unit tests using `unittest` or `pytest`

---

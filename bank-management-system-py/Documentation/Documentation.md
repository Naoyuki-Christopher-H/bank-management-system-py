# Simple Banking System

A clean, console-based banking application written in Python.

Minimal interface. Clear feedback. Focused on core banking operations.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Available Operations](#available-operations)
- [Data Storage](#data-storage)
- [Error Handling](#error-handling)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

## Overview

Simple Banking System is a terminal application that lets users:

- Create accounts
- Switch between accounts
- Deposit and withdraw money
- View current balance and account details

The interface follows calm, focused design principles with clear prompts  
and helpful feedback messages.

## Features

- Sequential account numbering
- Automatic selection of newly created account
- Positive-only transaction amounts
- Balance protection (cannot withdraw more than available)
- Clean screen clearing between views
- Persistent in-memory storage during runtime
- Graceful keyboard interrupt handling (Ctrl+C)

## Requirements

- Python 3.8 or newer
- No external packages required

## Installation

1. Clone or download the project
2. Navigate to the project folder
3. Run the program:

```bash
python banking.py
```

(or `python3 banking.py` on some systems)

## Usage

After starting the program you will see:

- A header showing current account (if selected)
- A numbered menu
- A prompt (→) to enter your choice

All inputs are validated. Invalid entries show a calm error message  
and return to the menu.

## Available Operations

1. **Create new account**  
   Enter full name and initial deposit amount.

2. **Switch account**  
   List all existing accounts and select one by number.

3. **Deposit**  
   Add money to the currently selected account.

4. **Withdraw**  
   Remove money (only if sufficient balance exists).

5. **View balance details**  
   Show account number, holder name and current balance.

6. **Quit**  
   Exit the application cleanly.

## Data Storage

All account data is stored in memory (Python dictionary)  
for the duration of the program run.

→ Data is **not** saved when the program exits.  
→ Every restart begins with zero accounts.

## Error Handling

The program handles the following cases gracefully:

- Empty or invalid name
- Negative initial deposit
- Negative or zero transaction amounts
- Withdrawal exceeding balance
- Non-existent account selection
- Invalid menu choice
- Non-numeric input where numbers are expected
- Keyboard interrupt (Ctrl+C)

## Limitations

- No persistent storage (data lost on exit)
- Single currency (no multi-currency support)
- No transaction history
- No overdraft facility
- No user authentication or passwords
- In-memory only — not suitable for production use

## Contributing

Found a bug or have an improvement idea?

1. Fork the repository
2. Create a descriptively named branch
3. Make your changes
4. Submit a pull request

Please include clear steps to reproduce any bug you are reporting.

## Disclaimer

UNDER NO CIRCUMSTANCES SHOULD IMAGES OR EMOJIS BE INCLUDED DIRECTLY IN THE README FILE. 
ALL VISUAL MEDIA, INCLUDING SCREENSHOTS AND IMAGES OF THE APPLICATION, MUST BE STORED IN 
A DEDICATED FOLDER WITHIN THE PROJECT DIRECTORY. THIS FOLDER SHOULD BE CLEARLY STRUCTURED 
AND NAMED ACCORDINGLY TO INDICATE THAT IT CONTAINS ALL VISUAL CONTENT RELATED TO THE 
APPLICATION (FOR EXAMPLE, A FOLDER NAMED IMAGES, SCREENSHOTS, OR MEDIA).

I AM NOT LIABLE OR RESPONSIBLE FOR ANY MALFUNCTIONS, DEFECTS, OR ISSUES THAT MAY OCCUR AS 
A RESULT OF COPYING, MODIFYING, OR USING THIS SOFTWARE. IF YOU ENCOUNTER ANY PROBLEMS OR 
ERRORS, PLEASE DO NOT ATTEMPT TO FIX THEM SILENTLY OR OUTSIDE THE PROJECT. INSTEAD, KINDLY 
SUBMIT A PULL REQUEST OR OPEN AN ISSUE ON THE CORRESPONDING GITHUB REPOSITORY, SO THAT IT 
CAN BE ADDRESSED APPROPRIATELY BY THE MAINTAINERS OR CONTRIBUTORS.

---
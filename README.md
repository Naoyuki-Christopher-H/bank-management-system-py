# Simple Banking System

A minimal, console-based banking application written in Python.  
Clear prompts. Focused functionality. Elegant simplicity.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Available Commands](#available-commands)
- [Design Notes](#design-notes)
- [Data Persistence](#data-persistence)
- [Error Handling](#error-handling)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License & Disclaimer](#license--disclaimer)

## Overview

Simple Banking System is a terminal application designed to simulate basic  
bank account operations with a calm, distraction-free interface.

It demonstrates clean code structure, thoughtful user feedback,  
and careful input validation — while keeping the experience intentionally simple.

## Features

- Create accounts with holder name and initial deposit
- Switch between multiple accounts
- Deposit and withdraw funds
- View detailed account information
- Automatic selection of newly created accounts
- Consistent screen clearing for focused interaction
- Graceful handling of Ctrl+C (KeyboardInterrupt)

## Requirements

- Python 3.8+
- No external dependencies

## Installation

1. Clone or download the repository  
2. Open a terminal in the project directory  
3. Run:

```bash
python bank_management_system_py.py
```

## Usage

After launching, you will see:

- A compact header showing the current account (if selected)
- A numbered menu of actions
- A simple prompt (→) for input

Follow the on-screen instructions. All inputs are validated.  
Meaningful feedback appears for every action and error.

## Available Commands

1. Create new account  
2. Switch account  
3. Deposit  
4. Withdraw  
5. View balance details  
6. Quit

## Design Notes

- Interface stays calm and spacious  
- Messages are written in plain, polite English  
- Errors are presented helpfully without alarm  
- Navigation feels intuitive and predictable  
- Visual hierarchy uses light rules and consistent indentation

## Data Persistence

All account data is stored **only in memory** (Python dictionary).  

When the program exits — intentionally or unexpectedly —  
all accounts and balances are lost.

This is by design for simplicity and clarity of scope.

## Error Handling

Gracefully manages:

- Empty or invalid names
- Negative amounts or balances
- Insufficient funds on withdrawal
- Non-numeric input
- Invalid menu choices
- Non-existent account numbers
- Keyboard interrupts (Ctrl+C)

## Limitations

- No data is saved between sessions
- Single currency only
- No transaction history
- No overdraft support
- No passwords or authentication
- Not intended for real financial use

## Contributing

Bug reports, suggestions, and pull requests are welcome.

1. Fork the repository  
2. Create a branch for your change  
3. Submit a clear pull request  

Please include steps to reproduce any issue you report.

## License & Disclaimer

This project is provided as-is for learning and demonstration purposes.

**Disclaimer**  

UNDER NO CIRCUMSTANCES SHOULD IMAGES OR EMOJIS BE INCLUDED DIRECTLY IN THE README FILE. 
ALL VISUAL MEDIA, INCLUDING SCREENSHOTS AND IMAGES OF THE APPLICATION, MUST BE STORED IN 
A DEDICATED FOLDER WITHIN THE PROJECT DIRECTORY. THIS FOLDER SHOULD BE CLEARLY STRUCTURED 
AND NAMED ACCORDINGLY TO INDICATE THAT IT CONTAINS ALL VISUAL CONTENT RELATED TO THE 
APPLICATION (FOR EXAMPLE, A FOLDER NAMED IMAGES, SCREENSHOTS, OR MEDIA). I AM NOT LIABLE OR 
RESPONSIBLE FOR ANY MALFUNCTIONS, DEFECTS, OR ISSUES THAT MAY OCCUR AS A RESULT OF COPYING, 
MODIFYING, OR USING THIS SOFTWARE. IF YOU ENCOUNTER ANY PROBLEMS OR ERRORS, PLEASE DO NOT 
ATTEMPT TO FIX THEM SILENTLY OR OUTSIDE THE PROJECT. INSTEAD, KINDLY SUBMIT A PULL REQUEST 
OR OPEN AN ISSUE ON THE CORRESPONDING GITHUB REPOSITORY, SO THAT IT CAN BE ADDRESSED 
APPROPRIATELY BY THE MAINTAINERS OR CONTRIBUTORS.

---

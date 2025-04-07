# Telegram Group Selector

A Python tool to list Telegram groups and selectively leave them.

## Features
- Lists all joined groups.
- Selects groups to leave by number.
- Batch leaves the selected groups.

## Installation
1. Ensure Python 3 is installed.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install telethon
   ```
4. Configure API:
   - Visit [my.telegram.org](https://my.telegram.org) to get your `api_id` and `api_hash`.
   - Edit `telegram_group_selector.py` and enter your credentials and phone number.

## Usage
1. Run:
   ```bash
   python telegram_group_selector.py
   ```
2. Enter the login verification code.
3. Follow the prompts to select the groups to leave.
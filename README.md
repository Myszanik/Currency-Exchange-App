# Currency Exchange App

This repository contains a simple Currency Exchange application built using Python, `tkinter`, and live exchange rate data. The app lets you enter two countries (or currency codes) and an amount, then it displays the converted amount, exchange rate, and country flags.

## Overview

The Currency Exchange App provides a GUI where you can:
- Enter a country name (example, United Kingdom, Czechia, United States)
- Enter an amount to convert
- Convert to another country currency
- View the converted result and exchange rate
- Display flags for the selected countries

## Features

- **Currency Conversion**
  - Live exchange rates
  - Shows original amount and converted amount
  - Shows the exchange rate

- **Country Input**
  - Enter country names, the app maps country to currency code automatically
  - You can also type currency codes directly (example, GBP, USD, CZK)

- **Flags**
  - Displays country flags using Rest Countries API data

## APIs Used

- ExchangeRate-API, for exchange rate data
- Rest Countries API, for country data, currency mapping, and flags

## Requirements

- Python 3.x
- `tkinter` (usually comes pre-installed with Python)

Python packages (installed via `requirements.txt`):
- `requests`
- `python-dotenv`
- `Pillow`

## Setup (Windows)

1. **Clone the repository**
   ```bash
   git clone https://github.com/Myszanik/CurrencyExchangeApp.git
2. **Navigate to the Project Directory**
   ```bash
   cd CurrencyExchangeApp
3. **Create a virtual environment (recommended)**
   ```bash
   python -m venv .venv
4. **Activate the virtual environment**
   ```bash
   .\.venv\Scripts\activate.bat
5. **Install Dependencies**
   ```bash
   python -m pip install -r requirements.txt
6. **Add your ExchangeRate-API key**  
	- Create a file named `.env` in the project root (same folder as `CurrencyExchangeApp.py`)
   ```bash
   EXCHANGE_RATE_API_KEY=YOUR_API_KEY_HERE
7. **Run the Application**
   ```bash
   python CurrencyExchangeApp.py

## Notes
- The `.env` file is intentionally not included in the repository, each user must create their own to run the app.
- Do not commit your API key to GitHub.
- The logo image is loaded from `assets/exchange_app_logo.jpeg`.

## Screenshots
Coming soon.

## Acknowledgements
- `tkinter`, for the GUI
- ExchangeRate-API, for exchange rate data
- Rest Countries API, for country and flag data
- `requests`, for HTTP requests
- `python-dotenv`, for loading environment variables from `.env`
- `Pillow`, for images

## Status
This project is for learning and practice. Improvements and clean-ups are welcome.
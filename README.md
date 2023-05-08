# Birthday Wisher Project

## Overview

The Birthday Wisher Project is a Python program that automatically sends birthday wishes to your colleagues via email. The program uses the SMTP library to connect to your email account and sends a personalized birthday message to each colleague whose birthday falls on the current day. The program is designed to run every day automatically, so you don't have to worry about remembering to send birthday wishes to your colleagues.

## Features

The Birthday Wisher Project has the following features:

- Sends personalized birthday wishes to your colleagues via email
- Automatically runs every day to check for birthdays
- Uses Pandas and NumPy libraries to read and manipulate CSV data
- Uses SMTP library to connect to your email account and send emails

## Requirements

To run the Birthday Wisher Project, you need to have the following:

- Python 3 installed on your computer
- Access to an email account that supports SMTP
- A CSV file containing the birthdays of your colleagues
-installed virtual enviornment in your computer

## Getting Started

To get started with the Birthday Wisher Project, follow these steps:

1. Clone the project repository to your computer.
2. Install the required Python libraries (Pandas and NumPy) using `pip install pandas numpy`.
3. Update the `config.py` file with your email account details (SMTP server, email address, and password).
4. Update the `birthdays.csv` file with the birthdays of your colleagues.
5. Run the `main.py` file to send birthday wishes to your colleagues.

## Limitations

The Birthday Wisher Project has the following limitations:

- It only supports CSV files for storing colleague birthdays.
- It requires the program to be running on the current day to send birthday wishes.

## Conclusion

The Birthday Wisher Project is a useful Python program that automates the process of sending birthday wishes to your colleagues. By using the Pandas, NumPy, and SMTP libraries, the program is able to read and manipulate CSV data and send personalized birthday messages via email. With a few simple updates to the `config.py` and `birthdays.csv` files, you can customize the program to meet your specific needs.

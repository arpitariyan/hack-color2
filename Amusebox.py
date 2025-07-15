#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from os import system, name
import itertools
import time
import sys
import datetime
# Removed unused base64 imports to reduce load time and memory footprint
from datetime import date

# ---------------------------------------------------------------------------
# Utility helpers (faster than the original thread-based + 20 s sleep design)
# ---------------------------------------------------------------------------


def spinner(message: str = "Processing", duration: float = 0.0, interval: float = 0.1):
    """CLI spinner that blocks the current thread for *duration* seconds.

    This replaces the previous 20-second sleep + extra thread approach, reducing
    runtime overhead to near-zero when *duration* is left at its default of 0.
    """

    if duration <= 0:
        return

    start = time.time()
    for c in itertools.cycle(["|", "/", "-", "\\"]):
        if time.time() - start >= duration:
            break
        sys.stdout.write(f"\r{message} {c}")
        sys.stdout.flush()
        time.sleep(interval)

    # Clear spinner line
    sys.stdout.write("\rDone!            \n")


def digit_sum(n: int) -> int:
    """Return the sum of digits of *n* (extracted for reuse)."""

    return sum(int(d) for d in str(n))
 
expirydate = datetime.date(2025, 12, 30)
#expirydate = datetime.date(2021, 8, 30)
today=date.today()
def hero(delay: float = 0.0, show_spinner: bool = False):
    """Core gameplay loop.

    Parameters
    ----------
    delay
        Seconds to delay the optional spinner. Keeping this at 0 disables any
        blocking sleep and keeps each round nearly instantaneous.
    show_spinner
        If *True*, a spinner will be rendered for *delay* seconds before the
        server-response messages.
    """

    def clear():
        # Windows vs POSIX
        system('cls' if name == 'nt' else 'clear')

    clear()

    newperiod = period
    banner = 'figlet AMUSEBOX'
    clear()
    system(banner)
    print("Contact me on telegram Ariyan")

    i = 1
    thisway = {1, 2, 4, 6, 7, 8, 15, 14, 16, 17, 18}
    thatway = {3, 5, 9, 10, 11, 12, 13, 19, 20}
    numbers: set[int] = set()

    playing = True
    while playing:
        clear()
        print("Contact me on telegram Ariyan")
        print("Enter", newperiod, "Parity Price :")

        try:
            current = int(input())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if show_spinner and delay > 0:
            spinner("Processing", delay)

        print("\n---------Successfully hacked the server-----------")
        print("\n---------Successfully got the colour -------------\n")

        sum_digits = digit_sum(current)
        last_digit = current % 10

        # Determine m based on the sequence position
        m = sum_digits + 1 if i in thatway else sum_digits

        same_parity = ((m % 2 == 0 and last_digit % 2 == 0) or
                       (m % 2 == 1 and last_digit % 2 == 1))

        colour = ('RED' if current in numbers else 'GREEN') if same_parity else (
            'GREEN' if current in numbers else 'RED')

        print(newperiod + 1, ':', colour)

        i += 1
        newperiod += 1
        numbers.add(current)

        user_choice = input("Do you want to play : Press 1 and 0 to exit \n")
        playing = user_choice != '0'

        if len(numbers) > 21:
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram Ariyan")
 
 
# ---------------------------------------------------------------------------
# Main entry-point
# ---------------------------------------------------------------------------


parser = argparse.ArgumentParser(description="AMUSEBOX – Parity predictor")
parser.add_argument('--delay', type=float, default=0.0, help='Delay in seconds for the optional spinner')
parser.add_argument('--spinner', action='store_true', help='Enable spinner animation before results')

args = parser.parse_args()


if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=0, minute=0, second=0, microsecond=0)
    Firstend = now.replace(hour=0, minute=0, second=0, microsecond=0)
    Second = now.replace(hour=0, minute=0, second=0, microsecond=0)
    Secondend = now.replace(hour=0, minute=0, second=0, microsecond=0)
    Third = now.replace(hour=0, minute=0, second=0, microsecond=0)
    Thirdend = now.replace(hour=0, minute=0, second=0, microsecond=0)
    Final = now.replace(hour=0, minute=0, second=0, microsecond=0)
    Finalend = now.replace(hour=0, minute=0, second=0, microsecond=0)
 
    if (True):
            period = 385
            hero(delay=args.delay, show_spinner=args.spinner)
    elif(False):
            period = 342
            hero(delay=args.delay, show_spinner=args.spinner)
    elif(False):
            period = 343
            hero(delay=args.delay, show_spinner=args.spinner)
    elif(now>Final and now<Finalend):
            period = 400
            hero(delay=args.delay, show_spinner=args.spinner)
 
 
 
else:
    banner='figlet AMUSEBOX'
    system(banner)
    print("Your hack has expired--- Please contact")
    print(" on telegram -----------Ariyan")
 

    









import os
from datetime import datetime
import logging
from .config import config

def read_last_run(state_file):
    """Reads the last run date from the state file."""
    if os.path.exists(state_file):
        with open(state_file, 'r') as f:
            last_run_str = f.read().strip()
        last_run = datetime.strptime(last_run_str, '%Y-%m-%d')
    else:
        last_run = None
    return last_run

def write_last_run(state_file):
    """Writes the current date as the last run date in the state file."""
    with open(state_file, 'w') as f:
        f.write(datetime.now().strftime('%Y-%m-%d'))

def main_program():
    """Main logic of the program to run when scheduled."""
    logging.info("Main program is running...")

def programmed_run(program):
    """Runs the scheduler logic to check if it's time to run the main program."""
    output_folder = config.output_folder

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        logging.info(f"Created output folder: {output_folder}")

    # State file in the output folder
    state_file = os.path.join(output_folder, 'last_run')

    # Read the last run date
    last_run = read_last_run(state_file)

    # Get the current date
    current_date = datetime.now()

    if last_run is None or (current_date - last_run).days >= config.periodicity:
        # If periodicity has passed or if no last run date, run the program
        program()
        write_last_run(state_file)
    else:
        print(state_file)
        logging.info(f"No need to run the program. Next run in {config.periodicity - (current_date - last_run).days} days.")


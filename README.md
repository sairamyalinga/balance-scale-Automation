# Balance Scale Automation Script

## Overview

This script automates the process of solving the puzzle on this [website](http://sdetchallenge.fetch.com/). The puzzle involves identifying the fake gold bar that has different weight from the rest of the bars using balance scale.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Install dependencies:

    ```bash
    pip3 install selenium
    ```

3. Ensure you have Google Chrome installed, as the script uses Chrome WebDriver.

## Usage

1. Open Terminal and Navigate to the project directory:

    ```bash
    cd /path/to/project
    ```

2. Run the script:

    ```bash
    python3 main.py
    ```

3. The script will launch a Chrome browser, navigate to the  [website](http://sdetchallenge.fetch.com/), and solve the balancing scale puzzle automatically.

## Script Structure

- `main.py`: Main script file containing the automation logic.
- `README.md`: Documentation file providing an overview of the script, installation instructions, and usage guidelines.

## Script Details

### Execution Flow

1. The script launches a Chrome browser and navigates to the  [website](http://sdetchallenge.fetch.com/).
2. It enters the initial gold bars of 3 each on the left and right of the balance scale input fields.
3. The script clicks the "Weigh" button to perform the initial weighing.
4. It retrieves the equation displayed on the webpage after the weighing to identify the relation to proceed next.
5. Based on the equation result, the script performs appropriate actions to solve the puzzle.
6. Once the puzzle is solved, the script terminates and write the output to a output.txt file.



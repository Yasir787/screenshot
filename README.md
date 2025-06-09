# Screenshot Taker

A lightweight Python application with a Tkinter GUI that captures screenshots after a 5-second delay and saves them as PNG files in a specified directory.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Description

This application provides a simple graphical interface to take screenshots. Clicking the "Take Screenshot" button triggers a 5-second delay, after which a screenshot is captured, saved with a timestamp-based filename, and displayed. A "Close" button allows exiting the application.

## Features

- Tkinter GUI with buttons for capturing screenshots and closing the app.
- Screenshots saved as PNG files with unique timestamp names.
- 5-second delay before capturing to prepare the screen.
- Displays the screenshot immediately after capture.

## Requirements

- Python 3.x
- Libraries:
  - `pyautogui`
  - `tkinter` (typically included with Python)
- Windows OS (due to the hardcoded file path).

## Installation

1. **Clone or download the repository**:

   ```bash
   git clone <repository-url>
   cd screenshot
   ```

2. **Install dependencies**:
   Install PyAutoGUI via pip:

   ```bash
   pip install pyautogui
   ```

3. **Set up the screenshot directory**:
   Ensure the directory `C:/Users/YASIR787/Downloads/python learning/New folder/screenshot/screenshot/screenshots data/` exists. Modify the path in the code if using a different location.

## Usage

1. Run the script:
   ```bash
   python ss.py
   ```
2. A window appears with two buttons:
   - **Take Screenshot**: Waits 5 seconds, captures the screen, saves it as a PNG, and displays it.
   - **Close**: Exits the application.
3. Verify the save directory exists to prevent errors.

## Directory Structure

```
screenshot/
│
├── ss.py          # Main Python script
├── screenshots data/            # Directory for saved screenshots
└── README.md                    # This README file
```

## Notes

- The script assumes the directory `C:/Users/YASIR787/Downloads/python learning/New folder/screenshot/screenshot/screenshots data/` exists. Update the path in the code for portability.
- The `time.sleep()` function in the code lacks a duration (should be `time.sleep(5)`). Fix this to ensure the 5-second delay works.
- Consider making the file path relative (e.g., using `os.path`) for cross-platform compatibility.

## Contributing

To contribute:

1. Fork the repository.
2. Create a branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Follow PEP 8 guidelines and include clear comments.

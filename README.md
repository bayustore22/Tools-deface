
# T-DEF - TOOLS DEFACE

![Logo T-DEF](https://raw.githubusercontent.com/wanzxploit/Tools-deface/refs/heads/main/banner.png)

## Description

**T-DEF** is a Python-based tool designed for efficient website defacing with ease. Developed by **Wanz Xploit**, this tool offers two main operation modes:

1. **Single Deface**: Uploads a script file to a single target directly.
2. **Multi Deface**: Uploads a script file to multiple targets listed in the `target.txt` file.

This tool is equipped with an attractive UI, dynamic banners, loading effects, and a deface result table.

---

## Key Features

- **URL Validation**: Ensures the target URL starts with `http://` or `https://`.
- **Automatic File Check**: Verifies the existence of the HTML file to upload.
- **Remove Duplicates**: In multi-mode, automatically removes duplicate targets from the list.
- **Loading Animation**: Provides a more interactive user experience.
- **Result Table**: Displays upload status for each target (successful/failed).
- **Local IP Address**: Displayed for network identification assistance.

---

## Installation Instructions

Follow the steps below to install and use this tool:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/wanzxploit/Tools-deface
   cd Tools-deface
   ```

2. **Install Dependencies**:
   If `make` is available on your system, you can run:
   ```bash
   make install
   ```

   This will install all necessary dependencies, including Python packages.

3. **Run the Tool**:
   After installation, run the tool using the following command:
   ```bash
   make run
   ```

4. **Prepare the Files**:
   - **File `target.txt`**: Create the `target.txt` file for multi-mode with a list of URLs (one per line). This file should be in the tool's directory.
   - **HTML Script File**: Place the HTML script file you want to upload (e.g., `deface.html`) in the same directory as the tool. The file name should match the input given when running the tool.

---

## Usage Guide

1. **Run the Tool**:
   ```bash
   make run
   ```

2. **Select the Operation Mode**:
   - Type **1** for Single Deface.
   - Type **2** for Multi Deface.

3. **Enter the Input**:
   - For single mode:
     - Enter the HTML script file name (e.g., `deface.html`).
     - Enter the target URL.
   - For multi mode:
     - Ensure the target URLs are listed in `target.txt`.
     - Enter the HTML script file to upload.

4. **Review the Results**:
   The tool will display a table with the results, showing the status of each target (successful/failed).

---

## How the System Works

1. **Single Deface**:
   - Validates the entered URL.
   - Checks for the existence of the HTML file.
   - Uploads the file to the target and provides a status report.

2. **Multi Deface**:
   - Reads target URLs from the `target.txt` file.
   - Automatically removes duplicates.
   - Uploads the file to each target and records the results.

3. **Result Table**:
   - Displays the status of each URL's upload, formatted neatly (successful/failed).

---

## Important Warning

- **Responsible Usage**:
  This tool is intended for educational purposes. The misuse of this tool is the sole responsibility of the user.
- **Backup Data**:
  If you have authorized access to the target, ensure that you back up the data before using this tool.
- **Legality**:
  Using this tool to attack without permission is illegal and against the law.

---

## Credits and Contact

Developed by **Wanz Xploit**.

- **Instagram**: [reyzroam](https://www.instagram.com/reyzroam/)
- **YouTube**: [Wanz Xploit](https://www.youtube.com/c/wanzxploit/)
- **GitHub**: [wanzxploit](https://github.com/wanzxploit)

---

## License

This tool is released under the **MIT License**. You are free to use it for educational purposes, but please adhere to all applicable laws and regulations.

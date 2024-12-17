# T-DEF - TOOLS DEFACE

![Logo T-DEF](https://raw.githubusercontent.com/wanzxploit/Tools-deface/refs/heads/main/banner.png)

## Description

**T-DEF** is a Python-based tool designed to deface websites with efficiency and ease. Developed by **Wanz Xploit**, this tool offers two main operating modes:

1. **Single Deface**: Uploading a script file to a single target directly.
2. **Multi Deface**: Uploading a script file to multiple targets at once, listed in the `target.txt` file.

This tool is equipped with an attractive interface, dynamic banners, loading effects, and a result table for the deface report.

---

## Main Features

- **URL Validation**: Ensures the target URL starts with `http://` or `https://`.
- **Automatic File Check**: Verifies the existence of the HTML file to be uploaded.
- **Remove Duplicates**: In multi-mode, the tool automatically removes duplicate targets from the list.
- **Loading Animation**: Provides a more interactive user experience.
- **Result Table**: Displays the upload status for each target (success/failed).
- **Local IP Address**: Displayed to help identify the network.

---

## Installation Guide for Termux

Follow these steps to install and use this tool on Termux:

1. **Update and Upgrade Termux Packages**:
   ```bash
   pkg update && pkg upgrade

2. Install Git and Python:

pkg install git python -y


3. Clone the Tools Deface Repository:

git clone https://github.com/wanzxploit/Tools-deface


4. Navigate to the Tools Directory:

cd Tools-deface


5. Install Python Dependencies:

pip install -r requirements.txt


6. Prepare Files:

target.txt File: Create a target.txt file for multi-mode with a list of URLs (one URL per line). This file should be placed in the tools directory.

HTML Script File: Place the HTML script file you wish to upload (e.g., deface.html) in the same directory as the tools. The file name should match the input you will enter when running the tool.





---

Usage Guide

1. Run the Tool:

make install
make run


2. Select the Operating Mode:

Type 1 for Single Deface.

Type 2 for Multi Deface.



3. Enter Input:

For single mode:

Enter the name of the HTML file (e.g., deface.html).

Enter the target URL.


For multi mode:

Ensure the target URLs are listed in the target.txt.

Enter the name of the HTML file to be uploaded.




4. Review the Results: The tool will display a result table with the status of each target upload (success/failed).




---

System Workflow Explanation

1. Single Deface:

Validates the entered URL.

Checks the existence of the HTML file.

Uploads the file to the target and provides the status report.



2. Multi Deface:

Reads the list of URLs from the target.txt file.

Automatically removes duplicate URLs.

Uploads the file to each target and records the result.



3. Result Table:

Displays a neatly formatted report of the upload status for each URL (success/failed).





---

Important Warning

Responsible Usage: This tool is designed for educational purposes. Any misuse of this tool is the sole responsibility of the user.

Data Backup: If you have authorized access to the target, please back up any data before using this tool.

Legality: Using this tool to attack without permission is illegal and violates the law.

Warning about target.txt: The target.txt file provided has been available since 2019 and has not been updated. Therefore, many URLs in it may no longer function or be relevant. I only update the script periodically and have never updated the target.txt file. It is recommended to verify and update the file as needed.



---

Credits and Contact

Developed by Wanz Xploit.

Instagram: reyzroam

YouTube: Wanz Xploit

GitHub: wanzxploit



---

License

This tool is released under the MIT License. You are free to use it for educational purposes, but please adhere to the rules and regulations.




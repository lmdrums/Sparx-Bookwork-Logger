<div align="center">
  <img src="readme_images/logo.svg" alt="Sparx Bookwork Logger" width="200">
  <h1>Sparx Bookwork Logger</h1>
  <img alt="Stars" src="https://img.shields.io/github/stars/lmdrums/Sparx-Bookwork-Logger.svg">
  <img alt="Downloads" src="https://img.shields.io/github/downloads/lmdrums/Sparx-Bookwork-Logger/total.svg">

</div>

# Tired of bookwork checks? ✅

### This project was designed to minimise the effort you have to put in to your Sparx homework ✍

Getting simple questions and having to write them down question after question can get annoying. This program **automatically** takes a screenshot after every question and saves it to a folder. </br> Whenever a bookwork check comes up, it retrieves that image and displays it in the GUI.

Follow the quick and easy setup below to get started...

# Installation and Setup 🔧

This project currently only works on [Windows](https://www.microsoft.com/en-gb/windows) but a [Linux](https://en.wikipedia.org/wiki/Linux) application will be coming in the future.

## Installation (.msi)

### Important: If you have Antivirus software, you will need to add an exception to the destination folder (more steps below)

**Some useful links:**
- [Avast Antivirus Exception](https://support.avast.com/en-gb/article/antivirus-scan-exclusions/#pc)
- [Norton Antivirus Exception](https://support.norton.com/sp/en/us/home/current/solutions/v3672136)
- [Bitdefender Antivirus Exception](https://www.bitdefender.co.uk/consumer/support/answer/88779/)
- [TotalAV Antivirus Exception](https://help.bethesda.net/#en/answer/46189)
- [McAfee Antivirus Exception](https://www.mcafee.com/support/?articleId=TS102056&page=shell&shell=article-view)

**Main Installation:**
- Navigate to the [**latest release**](https://github.com/lmdrums/sparx-bookwork-logger/releases/latest)
- Download the **'Sparx_Bookwork_Logger_Installer.msi'** file
- Open the file and click next
- Once you get to the second page where it asks for a folder to store the installed application, copy that file path for later
  - **For users with Antivirus Software only**: It is recommended you add your exception before installing, if your antivirus allows it (see above)
  - Add the exception as the path you copied in the previous step. For example: `C:\Users\YourUsername\AppData\Roaming\lmprogramming\Sparx Bookwork Logger\*`
  - You may alternatively disable your antivirus software and add an exception after installation
- Make sure you agree to the License T&C's (checkbox)
- Install the application
- A shortcut will be added to your Start Menu and Desktop
- Follow setup instructions below ⬇
- **Do your maths homework!**

## Installation (Python)

### Ignore this section if you have installed and will use the .msi file (recommended for general purpose)

If you don't want the hassle of adding exceptions for .msi files and have a version of [Python 3.10+](https://www.python.org/), you can run a standalone .py file for this application

Firstly, clone the repository - if you haven't already, install [Git](https://git-scm.com/downloads) (alternatively download and extract the source code)

`git clone https://github.com/lmdrums/Sparx-Bookwork-Logger.git`

Now, change directories to the newly cloned repo

`cd Sparx-Bookwork-Logger`

Install all dependencies (using [pip](https://pip.pypa.io/en/stable/))

`pip3 install -r requirements.txt`

To run the application, run the command

`python3 run.py`

Alternatively, setup a [virtual environment](https://docs.python.org/3/library/venv.html) in your IDE and run from there

## Setup
- **Web Setup:**
  - Go to [Sparx Maths](https://selectschool.sparxmaths.uk/)
  - Enter your school and click Continue:
    </br>
    ![Add school](readme_images/school.png)
  - You should now be at a login page:
    </br>
    ![Login page](readme_images/login.png)
  - Copy the link of this page and keep hold of it for later:
    </br>
    ![Link copy](readme_images/link_copy.png)

- **App Setup:**

  - Navigate to the newly downloaded application (see above)
  - Open the application
  - Go into 'Settings'
    </br>
    ![Settings window](readme_images/settings.png)
  - Type in your Sparx Username and Password in the corresponding boxes (these will be stored locally on your machine in a .ini file)
  - Paste the URL you copied from earlier in the URL box
    </br>
    ![Settings inputs](readme_images/settings_entry.png)
  - **Click Save to save your settings**

### Now you're good to go! 🟢

In the application, press **Launch Sparx** to begin *(Warning: this may take a while on the first launch if Chrome isn't already installed - a Chrome driver will be installed to your machine)*

You will be logged in automatically and you can begin your homework.

## Important Notes! (Please read) 📜

- If you start **XP Boost** questions, be warned that if you're **still running** Sparx Bookwork Logger, the answers of these questions will **overwrite** previous images with the same code
  - Therefore, whenever you **finish** a homework session and **no more** bookwork checks can be asked about that session, it is recommended you click the *'Clear Homework Session'* button in the **application**
- If you have completed a question and got it **correct**, please make sure you **leave enough time** to let the application get a **screenshot** of your answer, if not you may get a screenshot which looks like this:
  </br>
  ![Bad screenshot](readme_images/bad_screenshot.png)
  - The application **will automatically** click the Continue button for you after a correct answer so you don't even need to press continue

---

# Credits ❤️

- A massive thank you to [Aritra (aritra-codes)](https://github.com/aritra-codes) for helping with some errors
- We would greatly appreciate it if you could support us by following us on GitHub and other socials

<img src="https://github.com/lmdrums.png" alt="Profile picture of lmdrums" height="200" width="200"/> | <img src="https://github.com/aritra-codes.png" alt="Profile picture of aritra-codes" height="200" width="200"/>
---|---
[Lewis M (lmdrums)](https://github.com/lmdrums) | [Aritra (aritra-codes)](https://github.com/aritra-codes)

- Another big thanks to [Tom Schimansky](https://github.com/TomSchimansky) with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for making the UI possible as always

---

### [Latest Release Notes](https://lmdrums.github.io/sparx-bookwork-logger-release-notes/)

#### Any problems with this project, just let me know. 📪

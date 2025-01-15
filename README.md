# 🚀 Discord Update Script

This project automates the process of installing the latest `.deb` package from the Downloads folder, simplifying updates for applications like Discord on Linux. 🐧

## ✨ Features

- 🔍 Scans the `Downloads` folder for files.
- 🕒 Identifies the most recently downloaded file.
- 🛠️ Executes the installation command using `dpkg`.

## 📋 Requirements

- 🐍 Python 3.x
- 🖥️ Linux (tested on Ubuntu)
- 🔑 `sudo` privileges for running `dpkg`

## ⚙️ Installation

1. 📥 Clone or download this repository.
2. 💾 Save the script (e.g., `discord_update.py`) to a convenient location, such as `~/Desktop/python/discord_update/`.

## 🚀 Usage

1. Add the following alias to your `.zshrc` file:
   ```zsh
   alias discord.update="python3 ~/Desktop/python/discord_update/main.py"
Replace the path with the location of your script.

##  🔄 Reload your .zshrc file:

```bash
source ~/.zshrc
```

🏃 Run the script:
```bash
discord.update
```
## 🔧 How It Works
- The script scans the Downloads directory for files. 📂
- It determines the most recently modified file. 🕒
- It runs the dpkg -i command to install the .deb package. 🛠️

## 📦 Example Output
```bash
Latest file found: /home/user/Downloads/discord-0.0.80.deb
Executing command: sudo dpkg -i '/home/user/Downloads/discord-0.0.80.deb'
```

## 💡 Notes
- 🛑 Ensure that .deb files are being downloaded to the Downloads folder.
- ❗ The script assumes that the most recently modified file is the correct .deb package. Double-check your downloads if necessary.
- 🔒 The sudo command may prompt you for your password.

### 💬 Comments and Suggestions
If you have any feedback, suggestions, or improvements for this script, feel free to:

- Reach out via email: taixcode@gmail.com ✉️
  
Your contributions are welcome and appreciated! 🙌


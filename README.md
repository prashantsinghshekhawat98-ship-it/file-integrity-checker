# 🔐 File Integrity Checker

A simple Python-based cybersecurity project that detects file modifications using **SHA-256 hashing**.

## 📌 About the Project

The File Integrity Checker calculates the SHA-256 hash of a file and stores it as a baseline in a JSON file. Whenever the program runs again, it compares the current hash with the saved hash to detect whether the file has been modified.

This project demonstrates the basics of file integrity monitoring and cryptographic hashing.

## ✨ Features

- Generates SHA-256 hashes for files.
- Stores baseline hashes in a JSON file.
- Detects changes in file contents.
- Displays a warning when a file is modified.
- Uses Python's built-in libraries.

## 🛠️ Technologies Used

- **Python 3**
- `hashlib` — for SHA-256 hashing
- `json` — for storing baseline hashes
- `os` — for checking file existence

## 📂 Project Structure

```text
file-integrity-checker/
├── checker.py
├── test.txt
├── baseline.json
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/prashantsinghshekhawat98-ship-it/file-integrity-checker.git
```

### 2. Open the project directory

```bash
cd file-integrity-checker
```

### 3. Run the program

```bash
python3 checker.py
```

## 🧪 How It Works

1. The program checks whether a baseline file exists.
2. If no baseline exists, it calculates and saves the file's SHA-256 hash.
3. On subsequent runs, it calculates the hash again.
4. It compares the current hash with the saved hash.
5. It displays whether the file is unchanged or has been modified.

### Example Output

**First Run**
```text
Baseline saved!
```

**File Unchanged**
```text
File is unchanged.
```

**File Modified**
```text
WARNING: File has changed!
```

## 🎯 Learning Outcomes

- Understanding cryptographic hashing.
- Learning basic file integrity monitoring.
- Working with JSON files in Python.
- Practicing cybersecurity fundamentals.
- Using Git and GitHub for version control.

## ⚠️ Limitations

This is a beginner-level project that monitors a single file named `test.txt`. The baseline is stored locally, so an attacker who can modify both the file and its baseline could bypass detection. For stronger protection, store the baseline securely and consider monitoring multiple files.

## 👩‍💻 Author


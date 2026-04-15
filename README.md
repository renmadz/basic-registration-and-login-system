# 🧾 Simple Login & Registration System (Python)

## 📌 Overview

This is a basic **Login and Registration system** built in Python using **file handling**.
Instead of storing user data temporarily (like in arrays or dictionaries), this program saves user credentials in a text file (`users.txt`) so they persist even after the program closes.

---

## ⚙️ Features

* User Registration
* User Login
* Persistent storage using a text file
* Simple command-line interface

---

## 🛠️ How It Works

### 🔹 Registration

* The user enters a username and password.
* The credentials are saved in `users.txt` in this format:

  ```
  username,password
  ```

### 🔹 Login

* The program reads each line from `users.txt`.
* It compares the input credentials with stored data.
* If a match is found → login successful.
* If not → invalid credentials.

---

## 📂 File Structure

```
project_folder/
│
├── main.py
└── users.txt   (created automatically after registration)
```

---

## ▶️ How to Run

1. Make sure you have Python installed.
2. Run the script:

   ```
   python main.py
   ```
3. Choose an option:

   * `[1] Register`
   * `[2] Login`
   * `[3] Exit`

---

## ⚠️ Important Notes

* The file name **must match exactly** (`users.txt`) in both registration and login.
* If the file name is wrong, login will not work properly.
* The program does **not handle errors** like:

  * Invalid input (e.g., letters instead of numbers in menu)
  * Missing file (first-time run edge cases)

---

## 🔐 Security Warning

⚠️ This system stores passwords in **plain text**, which is **not secure**.
In real applications, passwords should be encrypted or hashed.

---

## 📘 What I Learned

* How to use file handling in Python:

  * `open()`
  * `.write()`
  * reading files line-by-line
* The importance of consistent file naming
* How persistent storage works compared to temporary variables

---

## ✍️ Author Notes

This project was written with the help of AI (specifically for file handling).
The goal was to understand how saving and reading data externally works, and to apply it in a simple login system.

---

## 🚀 Possible Improvements

* Use **JSON** instead of plain text
* Add **password hashing**
* Add **input validation**
* Improve UI (loop handling, retry system)
* Handle file errors safely

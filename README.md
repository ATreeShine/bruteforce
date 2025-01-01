# Real-Time Brute-Force Attack Tool

This Python script performs a **real-time brute-force attack** against a specified login form. By leveraging multithreading, it attempts multiple password combinations to find the correct credentials for a target username.

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes only** and to highlight the vulnerabilities of poorly secured login systems. Unauthorized use of this script against systems you do not own or have explicit permission to test is **illegal** and unethical. Always seek proper authorization before conducting any security tests.

---

## Features

- **Real-time Brute-Force Attack:** Continuously generates random passwords and attempts to log in.
- **Multithreading Support:** Allows multiple threads to work simultaneously, increasing efficiency.
- **Configurable Parameters:** Easy to adjust target URL, username field, password field, and thread count.
- **Graceful Shutdown:** Handles user interruptions cleanly.

---

## How It Works

1. **Setup:**
   - Provide the login URL and form field names for username and password.
   - Input the target username when prompted.
2. **Password Generation:**
   - Random passwords of a specified length (default: 7 characters) are generated.
3. **Login Attempts:**
   - The script parses the login form to gather necessary fields and attempts login using the generated passwords.
4. **Multithreading:**
   - Multiple threads work in parallel to speed up the brute-force process.
5. **Success or Failure:**
   - If a password works, the tool reports success and stops further attempts. If interrupted or no match is found, the process halts.

---

## Requirements

- Python 3.7+
- Required libraries:
  - `requests`
  - `bs4` (BeautifulSoup)

Install dependencies using:
```bash
pip install requests beautifulsoup4
```

---

## Usage

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo-name/brute-force-tool.git
cd brute-force-tool
```

### 2. Run the Script
```bash
python brute_force_tool.py
```

### 3. Input Parameters
- Enter the target username when prompted.
- Adjust thread count, if needed (default: 2).

### 4. Monitor Progress
- The script displays real-time password attempts and reports success or failure.

---

## Example Output
```
Enter the target username: test@example.com
Starting real-time brute-force attack with 2 threads for username: test@example.com
Trying password: AaBcDeF
Trying password: XyZaBcd
Success! Password found: XyZaBcd
Time taken: 12.34 seconds
Brute-force process finished.
```

---

## Customization

### Adjust Password Length
Modify the `generate_random_password` function:
```python
def generate_random_password(length=7):
    """Generates a random password of specified length."""
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))
```

### Change Number of Threads
Set the `num_threads` variable:
```python
num_threads = 4  # Increase or decrease thread count as needed
```

### Update Target URL and Fields
Edit the following variables:
```python
login_url = "http://example.com/login"
username_field = "txtEmail"
password_field = "txtPassword"
```

---

## Limitations

- **Password Complexity:** Only works for passwords using lowercase and uppercase letters.
- **Network Speed:** Performance depends on network latency and server response time.
- **Account Lockouts:** May trigger lockout mechanisms on target systems.

---

## Legal Responsibility

By using this tool, you agree to take full responsibility for your actions. Always ensure you have permission to perform security testing.

---

## Author
Developed by atreeshine. Contributions and feedback are welcome!

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.


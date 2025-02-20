import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, init
import getpass

# Initialize colorama
init(autoreset=True)

def print_logo():
    """Prints the Dark Men ASCII logo with random colors."""
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    logo_color = random.choice(colors)

    logo = """
██████╗ ███████╗██╗   ██╗██╗██╗     
██╔══██╗██╔════╝██║   ██║██║██║     
██║  ██║█████╗  ██║   ██║██║██║     
██║  ██║██╔══╝  ╚██╗ ██╔╝██║██║     
██████╔╝███████╗ ╚████╔╝ ██║███████╗
╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝
                                    
    """
    print(f"{logo_color}{logo}")
    print(f"{Fore.WHITE}Coded by: https://t.me/devil_mae | Contact for the premium version.")
    print("-" * 60)

def get_credentials():
    """Prompt user for login credentials securely."""
    username = input("Enter your username or email: ").strip()
    password = getpass.getpass("Enter your password (hidden): ").strip()
    return username, password

def login_facebook(driver, username, password):
    """Logs into Facebook using provided credentials."""
    print(f"{Fore.CYAN}[*] Logging into Facebook...")
    driver.get("https://www.facebook.com/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)
    print(f"{Fore.GREEN}[+] Facebook login successful!")

def login_instagram(driver, username, password):
    """Logs into Instagram using provided credentials."""
    print(f"{Fore.CYAN}[*] Logging into Instagram...")
    driver.get("https://www.instagram.com/accounts/login/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    print(f"{Fore.GREEN}[+] Instagram login successful!")

def search_account(driver, query, site):
    """Navigates to the target account."""
    print(f"{Fore.YELLOW}[*] Searching for the account...")
    if site == "facebook":
        driver.get(query)
    elif site == "instagram":
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
        )
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
    print(f"{Fore.GREEN}[+] Account located successfully!")

def report_user(driver, site):
    """Attempts to report the user account."""
    print(f"{Fore.RED}[*] Initiating report process...")
    if site == "facebook":
        try:
            three_dots = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Actions for this post']"))
            )
            three_dots.click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Find Support or Report')]"))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@aria-label, 'Report')]"))
            ).click()
            print(f"{Fore.GREEN}[+] Report submitted successfully!")
        except Exception as e:
            print(f"{Fore.RED}[!] Error during Facebook report: {e}")

    elif site == "instagram":
        try:
            three_dots = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@aria-label='More options']"))
            )
            three_dots.click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Report')]"))
            ).click()
            print(f"{Fore.GREEN}[+] Report submitted successfully!")
        except Exception as e:
            print(f"{Fore.RED}[!] Error during Instagram report: {e}")

def main():
    print_logo()

    while True:
        site = input("Choose platform (facebook/instagram): ").strip().lower()
        if site not in ["facebook", "instagram"]:
            print(f"{Fore.RED}[!] Invalid option.")
            continue

        target = input("Enter the target profile URL (Facebook) or username (Instagram): ").strip()

        try:
            repeat_count = int(input("How many times to report?: ").strip())
        except ValueError:
            print(f"{Fore.RED}[!] Enter a valid number.")
            continue

        username, password = get_credentials()

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)

        try:
            for i in range(repeat_count):
                print(f"{Fore.MAGENTA}[#] Report attempt {i + 1}/{repeat_count}")
                if site == "facebook":
                    login_facebook(driver, username, password)
                else:
                    login_instagram(driver, username, password)

                search_account(driver, target, site)
                report_user(driver, site)
                time.sleep(3)

            print(f"{Fore.GREEN}[*] All reports completed.")
        except Exception as e:
            print(f"{Fore.RED}[!] Unexpected error: {e}")
        finally:
            driver.quit()

        action = input("Do you want to [restart/exit]?: ").strip().lower()
        if action == "restart":
            continue
        elif action == "exit":
            print(f"{Fore.BLUE}[*] Exiting. For premium version, contact: https://t.me/devil_mae")
            break
        else:
            print(f"{Fore.RED}[!] Invalid input, exiting.")
            break

if __name__ == "__main__":
    main()

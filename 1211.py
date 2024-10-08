import requests
import random
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def display_intro():
    print(Fore.CYAN + Style.BRIGHT + r"""
    _________   ____ ___.___________________   
   /   _____/  |    |   \   \______   \     \  
   \_____  \   |    |   /   ||     ___/  |   \ 
   /        \  |    |  /|   ||    |   |  |___\ 
  /_______  /  |______/ |___||____|   |_____  /
          \/                               \/ 
    """)
    print(Fore.GREEN + "OSINT Username Checker")
    print(Fore.WHITE + "Author: " + Fore.YELLOW + "GORLAMI")
    print(Fore.WHITE + "Description: " + Fore.YELLOW + "Checks for the presence of a username across multiple popular social media platforms.")
    print(Fore.WHITE + "-" * 60 + "\n")

# List of user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/604.1"
]

# Platforms and their URL format
platforms = {
    "Facebook": "https://www.facebook.com/{}",
    "Twitter": "https://www.twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "GitHub": "https://www.github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "YouTube": "https://www.youtube.com/{}",
    "Flickr": "https://www.flickr.com/people/{}"
}

def check_username(username):
    session = requests.Session()
    results = {}
    for platform, url in platforms.items():
        profile_url = url.format(username)
        headers = {
            "User-Agent": random.choice(user_agents),
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Cache-Control": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "Referer": "https://www.google.com/"
        }
        
        print(Fore.YELLOW + f"Checking {platform}: {profile_url}")

        try:
            time.sleep(random.uniform(1, 3))
            response = session.get(profile_url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                results[platform] = Fore.GREEN + f"Username found: {profile_url}"
            else:
                results[platform] = Fore.RED + "Username not found"
        
        except requests.Timeout:
            results[platform] = Fore.MAGENTA + "Error: Request timed out"
            print(Fore.MAGENTA + f"Timeout while checking {platform}")
        except requests.RequestException as e:
            results[platform] = Fore.MAGENTA + f"Error: {str(e)}"
            print(Fore.MAGENTA + f"Request exception while checking {platform}: {e}")
            
    return results

if __name__ == "__main__":
    display_intro()
    username = input(Fore.CYAN + "Enter the username to search for: " + Fore.RESET)
    results = check_username(username)
    print(Fore.WHITE + "\nResults:\n" + "-" * 60)
    for platform, result in results.items():
        print(Fore.CYAN + f"{platform}: " + result)
input("ENTER TO EXIT")

            
"""
Coded by : king ♚ Tanin ♚ ♚ 
"""
import requests
import random
from getuseragent import UserAgent
from rich import print
from rich.panel import Panel

class TikTokBooster:
    def __init__(self):
        self.ua = UserAgent("ios").Random()
        self.base_url = 'https://api.likesjet.com/freeboost/3'

    def boost_video(self, user: str, link: str) -> dict:
        email = f"x_spoilt{random.randint(10000,99999)}@gmail.com"
        headers = {
            "Host": "api.likesjet.com",
            "content-length": "137",
            "sec-ch-ua": "\"Google Chrome\";v\u003d\"119\", \"Chromium\";v\>
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "sec-ch-ua-mobile": "?1",
            "user-agent": self.ua,
            "sec-ch-ua-platform": "\"Android\"",
            "origin": "https://likesjet.com",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://likesjet.com/",
            "accept-language": "en-XA,en;q\u003d0.9,ar-XB;q\u003d0.8,ar;q\u>
        }
        data = {"link": link, "tiktok_username": user, "email": email}
        response = requests.post(self.base_url, json=data, headers=headers)>
        return response

def main():
    print(Panel("[bold cyan]TikTok Video Booster[/]\nCoded by : @x_spoilt",>
    user = input('> TikTok UserName: ')
    link = input('> Video Link: ')

    booster = TikTokBooster()
    response = booster.boost_video(user, link)

    if response.get('status'):
        status = "[bold green]Success[/]"
    else:
        status = "[bold red]Failed[/]"

    result_message = f"Status: {status}\nMessage: {response.get('message')}"

    print(Panel(result_message, title="[bold blue]Boost Result[/]"))

if __name__ == "__main__":
    main()

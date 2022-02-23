import asyncio
from selenium import webdriver
from bs4 import BeautifulSoup
from config import Settings
from utilities import sync_to_async
from healthcheck import selenium_health_check
import pickle


def url_parser(html: str) -> set[str]:
    soup = BeautifulSoup(html, 'html5lib')
    posts = soup(attrs={'data-e2e': 'user-post-item'})
    urls = {post.find('a')['href'] for post in posts}
    return urls


@sync_to_async
def fetch_tiktok_html(username: str, webdriver_port: str | int) -> str:
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://selenium:' + str(webdriver_port).strip(),
        options=chrome_options
    )
    driver.get("https://www.tiktok.com/@" + username.strip())
    html = driver.page_source
    driver.quit()
    return html


async def main(username: str, webdriver_port: str | int) -> set[str]:
    html = await fetch_tiktok_html(username, webdriver_port)
    urls = url_parser(html)
    print(urls)
    return urls

if __name__ == '__main__':
    settings = Settings()
    selenium_health_check('selenium', settings.webdriver_port)
    if not settings.windows:
        from uvloop import EventLoopPolicy
        asyncio.set_event_loop_policy(EventLoopPolicy())
    asyncio.run(main(settings.username, settings.webdriver_port), debug=settings.debug)

import requests
import asyncio
from pyppeteer.launcher import launch
from getAuth import getOnsAuthCookie

async def downloadOnsFile(url):
    browser = await launch(args=["--no-sandbox"])
    page = await browser.newPage()
    cookie = await getOnsAuthCookie(page)
    await browser.close()
    r = requests.get(url, cookies=cookie)
    open("acomph.xlsx", "wb").write(r.content)

def main(): 
    asyncio.get_event_loop().run_until_complete(downloadOnsFile("https://sintegre.ons.org.br/sites/9/13/56/Produtos/230/ACOMPH_12.04.2020.xls"))

main()


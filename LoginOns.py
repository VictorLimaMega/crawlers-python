import asyncio
from pyppeteer.launcher import launch
from getAuth import getCookieOns

async def getLastNews():
	browser = await launch(args=["--no-sandbox"])
	page = await browser.newPage()
	await getCookieOns(page)
	await redirectNoticias(page)
	await browser.close()

async def redirectNoticias(page):
	await page.goto("https://sintegre.ons.org.br/Paginas/servicos/noticias.aspx")
	await page.waitForSelector("[class*='corpocard']")
	await page.screenshot({'path': "noticias.png"})
	cards = await page.querySelectorAll("[class*='corpocard']")
	for card in cards:
		title = await card.querySelector("[class*='titulo']")
		label = await title.querySelector("label")
		value = await page.evaluate("(el) => el.textContent", label)
		print(value)

def main(): 
	asyncio.get_event_loop().run_until_complete(getLastNews())

main()
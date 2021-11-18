import asyncio
from pyppeteer.launcher import launch

async def getLastNews():
	browser = await launch(args=["--no-sandbox"])
	page = await browser.newPage()
	await page.goto("https://sintegre.ons.org.br")
	await loginOns(page)
	await redirectNoticias(page)
	await browser.close()

async def loginOns(page):
	await page.screenshot({'path': "sintegre_inicial.png"})
	await page.type("#username", "precos@megawhat.energy")
	await page.click('[name="submit.IdentificarUsuario"]')
	await page.waitForNavigation()
	await page.screenshot({'path': "sintegre_pos_user.png"})
	await page.type("#password", "SintegrandoComMega473$")
	await page.click('[name="submit.Signin"]')
	await page.waitFor(10000)
	await page.screenshot({'path': "sintegre_pos_senha.png"})

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
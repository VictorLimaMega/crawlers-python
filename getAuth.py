import asyncio
from pyppeteer.launcher import launch

async def loginOns(page):
    await page.goto("https://sintegre.ons.org.br")
    await page.type("#username", "precos@megawhat.energy")
    await page.click('[name="submit.IdentificarUsuario"]')
    await page.waitForNavigation()
    await page.type("#password", "SintegrandoComMega473$")
    await page.click('[name="submit.Signin"]')
    await page.waitFor(10000)

async def getCookies(page):
    cookies = await page.cookies()
    return cookies

async def getOnsAuthCookie(page):
	await loginOns(page)
	cookies = await page.cookies()
	for cookie in cookies:
		if cookie["name"] == "FedAuth":
			return {"FedAuth": cookie["value"]}
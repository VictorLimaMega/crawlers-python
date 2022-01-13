import asyncio
from pyppeteer.launcher import launch

async def scrapTableau():
    browser = await launch(args=["--no-sandbox"])
    page = await browser.newPage()
    await page.goto("https://tableaupub.ccee.org.br/t/CCEE/views/PreoHistrico/HistricodoPreoHorrio?%3Aembed=y")
    await page.waitFor(10000)
    await page.click('.tab-tvLeftAxis .tabCanvas')
    await page.waitFor(5000)
    await page.click('div.tabToolbarButton.tab-widget.download')
    await page.waitFor(5000)
    await page.click('div.tab-downloadDialog > div:nth-child(3)')
    await page.waitFor(5000)
    pages = await browser.pages()
    for page in pages:
        link = await page.querySelector('a.csvLink_summary')
        if link:
            await page._client.send('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': '/tmp/test/'});
            await page.waitFor(5000)
            url = await page.evaluate("(el) => el.href", link)
            try:
                await asyncio.wait([
                    page.goto(url),
                    page.waitFor(5000),
                ])
            except:
                pass
    await browser.close()

def main(): 
    asyncio.get_event_loop().run_until_complete(scrapTableau())

main()
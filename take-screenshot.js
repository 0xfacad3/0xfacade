const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://honzaap.github.io/GithubCity/?name=Once-a-deadcat&year=2023', {waitUntil: 'networkidle2'});
  await page.setViewport({
    width: 1200,
    height: 800,
    deviceScaleFactor: 1,
  });
  await page.screenshot({path: 'screenshot.png'});
  await browser.close();
})();

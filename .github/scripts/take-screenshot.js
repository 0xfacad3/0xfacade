const puppeteer = require('puppeteer');

async function run() {
  const browser = await puppeteer.launch({headless: true, executablePath: '/usr/bin/chromium-browser',args: ['--no-sandbox', '--disable-setuid-sandbox']});
  const page = await browser.newPage();
  await page.goto('https://honzaap.github.io/GithubCity/?name=Once-a-deadcat&year=2023', {waitUntil: 'networkidle2', timeout: 1800000});
  await page.screenshot({path: 'screenshot.png'});

  await browser.close();
}

run();

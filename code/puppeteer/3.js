const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('http://rennaiqian.com');
  await page.screenshot({path: 'example.png'});
  await page.pdf({path: 'example.pdf', format: 'A4'});
  await browser.close();
})();
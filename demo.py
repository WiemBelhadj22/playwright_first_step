from playwright.sync_api import sync_playwright , Playwright, expect
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False , slow_mo=50)
    page = browser.new_page()
    page.goto('https://instagram.com')
    page.fill('input[name=username]','orthlaner')
    page.fill('input[name=password]','1234orthlane')
    page.click('button[type=submit]')

    try:
        page.click('button:has-text("Plus tard")')
    except:
        pass
    try:
        page.click('button:has-text("Plus tard")')
    except:
        pass
#boucle

    page.locator("div[role=\"button\"]:has-text(\"Rechercher\")").click()
    # Fill [placeholder="Rechercher"]
    page.locator("[placeholder=\"Rechercher\"]").fill("#teeth")
    # Press ArrowDown
    page.locator("[placeholder=\"Rechercher\"]")
    page.keyboard.press("ArrowDown")
    # Press Enter
    page.locator("[placeholder=\"Rechercher\"]")
    page.keyboard.press("Enter")
    # expect(page).to_have_url("https://www.instagram.com/explore/tags/teeth/")

    # Click ._aagw >> nth=0
    page.locator("._aagw").first.click()

    #page.locator("text=42025").click()
    page.locator("article[role=\"presentation\"] [aria-label=\"Suivant\"]").click()

#fin boucle 

    page.pause()
   
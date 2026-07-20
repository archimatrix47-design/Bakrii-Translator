from playwright.sync_api import sync_playwright
import os

html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "translator.html")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    page.goto(f"file:///{html_path.replace(os.sep, '/')}")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="screenshot.png", full_page=True)
    browser.close()

"""Print ballot details from MA ballot tracker."""
import pathlib
from typing import NamedTuple

import environ
from dotenv import load_dotenv
from playwright import sync_playwright


@environ.config(prefix="TMB")
class FormInputs:
    """Values for the MA ballot tracker form."""

    election = environ.var()
    first_name = environ.var()
    last_name = environ.var()
    street_number = environ.var()
    street_name = environ.var()
    street_suffix = environ.var()
    zip_code = environ.var()


load_dotenv()
INPUTS = FormInputs.from_environ()


class BallotDetails(NamedTuple):
    """A row of details from the MA ballot tracker."""

    election: str
    mailed: str
    received: str
    status: str


def main():
    """Set up playwright and print ballot details."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.newContext()
        page = context.newPage()

        details = get_details(page, INPUTS)

        page.close()
        context.close()
        browser.close()

    for field, value in details._asdict().items():
        print(f"{field:10} {value}")


def get_details(page, inputs):
    """Return ballot details from MA ballot tracker."""
    page.goto("https://www.sec.state.ma.us/wheredoivotema/track/trackmyballot.aspx")
    save_screenshot(page, "form")

    page.fill('input[name="ctl00$MainContent$txtFirstName"]', inputs.first_name)
    page.fill('input[name="ctl00$MainContent$txtLastName"]', inputs.last_name)
    page.fill('input[name="ctl00$MainContent$txtStreetNo"]', inputs.street_number)
    page.fill('input[name="ctl00$MainContent$txtStreetName"]', inputs.street_name)
    page.selectOption(
        'select[id="MainContent_ddlStreetSuffix"]', inputs.street_suffix.upper()
    )
    page.fill('input[name="ctl00$MainContent$txtZip"]', inputs.zip_code)

    page.click('input[name="ctl00$MainContent$btnSearch"]')
    save_screenshot(page, "details")

    detail_cells = page.querySelectorAll(f'//td[text()="{inputs.election}"]/../td')
    details = BallotDetails(*[el.textContent() for el in detail_cells])

    return details


def save_screenshot(page, name):
    """Save a PNG of the current page."""
    screenshots = pathlib.Path("screenshots")
    screenshots.mkdir(exist_ok=True)
    page.screenshot(path=screenshots / f"{name}.png", fullPage=True)


if __name__ == "__main__":
    main()

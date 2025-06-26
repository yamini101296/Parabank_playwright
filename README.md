# Parabank Playwright Automation Framework

## Description
This is a Playwright + Pytest automation framework for testing the Parabank website:
https://parabank.parasoft.com/parabank/index.htm

## Features
- ✅ Page Object Model (POM) structure
- ✅ Reusable fixtures
- ✅ HTML Reporting with `pytest-html`
- ✅ Screenshot capture on test failures
- ✅ Detailed logging for every test

## Folder Structure
- `pages/` - Page classes
- `tests/` - Test cases
- `utils/` - Logger
- `logs/` - Log files
- `screenshots/` - Failure screenshots
- `reports/` - HTML reports

## Installation
1. Install dependencies:
```bash
pip install -r requirements.txt
playwright install

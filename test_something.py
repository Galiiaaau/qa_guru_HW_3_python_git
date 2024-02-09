from selene import browser, be, have


def test_find_selen(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_no_results(open_browser):
    browser.element('[name="q"]').should(be.blank).type('ggkjlkjlhjv').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))


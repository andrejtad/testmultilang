import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_exists(browser):
    browser.get(link)
    time.sleep(10)
    try:
        btn_to_add_basket = browser.find_element_by_css_selector(".btn-add-to-basket")

    except:
        btn_to_add_basket = False

    assert btn_to_add_basket, "The 'Add to basket' button is missing from the page"

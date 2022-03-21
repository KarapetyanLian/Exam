from BDJ_project_agoda import *

browser.get(base_url)
browser.get(base_url)
sign_up()
login()
click_a_hotel(hotel_location, 0)
room_list = get_room_list()

for room in room_list:
    try:
        room.click()
        add_to_card()
    except NoSuchElementException:
        browser.close()
        browser.switch_to.window(browser.window_handles[1])
        continue
    else:
        break

customer_info_filler()
url = browser.current_url
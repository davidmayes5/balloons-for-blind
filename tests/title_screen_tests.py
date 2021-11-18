from framework import interactions, coordinates
import time

def test_title_buttons():
    for button_name in coordinates.title:
        print(f"Attempting click of {str(button_name)}...")
        interactions.click_title_button(button_name)
        time.sleep(2)
        interactions.click_title_button("back")
        time.sleep(2)
import coordinates, interactions
import time

def test_title_buttons():
    for button_name in coordinates.title:
        button = coordinates.title[button_name]
        print(f"Attempting click of {str(button)}...")
        interactions.click(button)
        time.sleep(2)
        interactions.click(coordinates.navigation["back"])
        time.sleep(2)

# Execute tests
test_title_buttons()
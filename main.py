import pyautogui, os, keyboard
from time import sleep

def image():
    image_path = os.path.join(os.path.dirname(__file__), 'skip_button.png')
    return image_path
def find_button(image_path):
    try: 
        button_pos = pyautogui.locateOnScreen(image_path, region=region, confidence=0.7)
        print(button_pos)
        print(f"Found button at {button_pos}")
        
    except:
        print("Not found...")
        button_pos = None
    return button_pos
image_path = image()

# Get screen size
screen_width, screen_height = pyautogui.size()
region = (screen_width // 2, screen_height // 2, screen_width // 2, screen_height // 2)

while __name__ == '__main__':
    button_pos = find_button(image_path)
    if button_pos:
        pyautogui.click(button_pos)
        print("Button clicked!")
        button_pos = None
    if keyboard.is_pressed('esc'):
        print("Stopping Ad-skipper...")
        break
    sleep(3)
    
import pyautogui
import time
import pyperclip
# from openai import OpenAI


#pip install OpenAI
client = OpenAi(
    api_key = "",
)


def is_last_message_from_sender(chat_log,sender_name="mansi"):
    #split the chat log into individual message
    messages = chat_log.strip().split("/2024")[-1]
    if sender_name in messages:
        return True
    return False


#click on chrome icon
pyautogui.click(998,1047)


# Give some time to switch to the desired window
time.sleep(1)
    
# Click on the icon at (988, 1047)
while True:
    time.sleep(1)  # Wait a bit to ensure the action completes

    # Move to the start position and drag to the end position to select text
    pyautogui.moveTo(578, 191)
    pyautogui.dragTo(1822, 902, duration=1, button='left')
    time.sleep(1)  # Wait a bit to ensure the selection completes

    # Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.click(1778,849)
    # Wait a bit to ensure the copy action completes

    # Get the text from the clipboard
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)

    if is_last_message_from_sender(chat_history):


        completion = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [{"role":"system","content":"you are a person named muskan who speaks hindi as well as english.you are from inda.you analyse chat history and respond like muskan."},
            {"role":"user","content":chat_history}
        ]
    )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        #clicking at writing text message point
        pyautogui.click(731,955)
        time.sleep(1)

        # paste the text
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)

        #press enter
        pyautogui.press('enter')
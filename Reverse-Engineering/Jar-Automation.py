import pyautogui

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        for g in range(2):
                            for h in range(2):
                                for i in range(2):
                                    for x in (a, b, c, d, e, f, g, h, i):
                                        if x == 0:
                                            pyautogui.moveTo(169, 177, duration = 0.25)
                                            pyautogui.click()
                                        else: # 1
                                            pyautogui.moveTo(229, 186, duration = 0.25)
                                            pyautogui.click()
                                    print(a, b, c, d, e, f, g, h, i)
                                    # Reset
                                    pyautogui.moveTo(220, 235, duration = 0.5)
                                    pyautogui.click()

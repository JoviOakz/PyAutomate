import pyautogui as bot

bot.FAILSAFE = True

bot.hotkey('win', 'r')
bot.write('cmd')
bot.press('enter')
bot.sleep(0.75)
bot.write('notepad')
bot.press('enter')
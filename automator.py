

# prerequisites:
# 1. browser open to Adobe Sign Documents - half screen left side on 1920 * 1080
# 2. screenshot of signature block in same directory ex) AdobeSign_Automator/signatureBlock.png

import pyautogui

print('Press Ctrl-C to Quit.')

sigBlock = 'signatureBlock.png'
def locateSigBlock(sigBlock):
    # sigBlockList = list(pyautogui.locateAllOnScreen(sigBlock))
    # print(sigBlockList)
    # for pos in pyautogui.locateAllOnScreen(sigBlock):
    #     print(pos)
    try:
        # x, y = pyautogui.locateCenterOnScreen('sigBlock.png')
        # pyautogui.click(x, y)
        sigBlockList = list(pyautogui.locateAllOnScreen('sigBlockLg.png'))
        print(sigBlockList)
        # sigBlockList2 = list(pyautogui.locateAllOnScreen('sigBlockSm.png'))
        # print(sigBlockList2)
        sigBlockList3 = list(pyautogui.locateAllOnScreen('sigBlockFooter.png'))
        print(sigBlockList3)
    except TypeError:
        print('not found')



try:
    # while True:
    locateSigBlock(sigBlock)
except KeyboardInterrupt:
    print('\nDone.')
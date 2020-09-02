

# prerequisites:
# 1. browser open to Adobe Sign Documents - half screen left side on 1920 * 1080
# 2. screenshot of signature block in same directory ex) AdobeSign_Automator/signatureBlock.png

import pyautogui
import time

print('Press Ctrl-C to Quit.')

sigBlockList = ['sigBlockLg.png', 'sigBlockSm.png', 'sigBlockFooter.png']
signInButtonLoc = (406, 649)
signingReasonLoc = (492, 411)
validDocLoc = (412, 460)
okButtonLoc = (709, 456)

def locateSigBlock(sigBlockList):
    try:
        # x, y = pyautogui.locateCenterOnScreen('sigBlock.png')
        # pyautogui.click(x, y)
        # sigBlockList = list(pyautogui.locateAllOnScreen('sigBlockLg.png'))
        # print(sigBlockList)
        # sigBlockList2 = list(pyautogui.locateAllOnScreen('sigBlockSm.png'))
        # print(sigBlockList2)
        # sigBlockList3 = list(pyautogui.locateAllOnScreen('sigBlockFooter.png'))
        # print(sigBlockList3)

        for sigBlock in sigBlockList:
            sigBlockLoc = pyautogui.locateCenterOnScreen(sigBlock)
            if sigBlockLoc:
                print(sigBlockLoc)
                pyautogui.click(sigBlockLoc)
                # wait
                time.sleep(2)
                pyautogui.click(signInButtonLoc)
                time.sleep(2)
                pyautogui.click(signingReasonLoc)
                time.sleep(1)
                pyautogui.click(validDocLoc)
                time.sleep(1)
                pyautogui.click(okButtonLoc)
            else:
                print('No signature on this page')
                pyautogui.scroll(-400)
                time.sleep(1)

        pyautogui.scroll(-400)
    except TypeError:
        print('not found')



try:
    while True:
        locateSigBlock(sigBlockList)

except KeyboardInterrupt:
    print('\nDone.')
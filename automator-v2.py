

# prerequisites:
# 1. browser open to Adobe Sign Documents - half screen left side on 1920 * 1080
# 2. screenshot of signature block in same directory ex) AdobeSign_Automator/signatureBlock.png

import pyautogui
import time

print('Press Ctrl-C to Quit.')

sigBlockList = ['sigBlockLg.png', 'sigBlockSm.png', 'sigBlockFooter.png']

# nextButtonList = ['next1.png', 'next2.png', 'next3.png']
nextButtonList = ['nextRequired.png']
clickToSign = 'clickToSign.png'
signInButtonLoc = (406, 649)
signingReasonLoc = (492, 411)
validDocLoc = (412, 460)
okButtonLoc = (709, 456)

def locateSigBlock(nextButtonList):
    try:
        for next in nextButtonList:
            print(next)
            nextButtonLoc = pyautogui.locateCenterOnScreen(next)

            if nextButtonLoc is not None:

                pyautogui.click(nextButtonLoc)

                time.sleep(1)
                # locate clickToSign
                x, y = pyautogui.locateCenterOnScreen(clickToSign)

                pyautogui.click(x, y+40)
                print('sig block clicked')
                time.sleep(2)
                pyautogui.click(signInButtonLoc)
                time.sleep(2.5)
                pyautogui.click(signingReasonLoc)
                time.sleep(2)
                pyautogui.click(validDocLoc)
                time.sleep(1)
                pyautogui.click(okButtonLoc)

                

        #     sigBlockLoc = pyautogui.locateCenterOnScreen(sigBlock)
        #     if sigBlockLoc:
        #         print(sigBlockLoc)
        #         pyautogui.click(sigBlockLoc)
        #         # wait
        #         time.sleep(2)
        #         pyautogui.click(signInButtonLoc)
        #         time.sleep(2)
        #         pyautogui.click(signingReasonLoc)
        #         time.sleep(1)
        #         pyautogui.click(validDocLoc)
        #         time.sleep(1)
        #         pyautogui.click(okButtonLoc)
        #     else:
        #         print('No signature on this page')
        #         pyautogui.scroll(-400)
        #         time.sleep(1)

        # pyautogui.scroll(-400)
    except TypeError:
        print('not found')
        pyautogui.scroll(-400)



try:
    while True:
        locateSigBlock(nextButtonList)

except KeyboardInterrupt:
    print('\nDone')
import subprocess
import os


def screenshot(savePath):
    subprocess.call(['adb', 'shell', 'screencap',
                     '-p', '/sdcard/screencap.png'])
    print('Screenshotted')

    subprocess.call(
        ['adb', 'pull', '/sdcard/screencap.png', savePath])
    print('Pulled screenshot')


if __name__ == "__main__":
    index = 0
    savePath = './screenshots/screencap-{}.png'.format(index)

    while(True):
        while (os.path.exists(savePath)):
            index += 1
            savePath = './screenshots/screencap-{}.png'.format(index)

        input('Press enter when ready.')
        screenshot(savePath)
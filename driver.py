from uiautomator import device as d
from uiautomator import Device

notepad = App('notepad.exe')
notepad.open()
sleep(1)
type("It is working!")
notepad.close()

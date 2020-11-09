from uiautomator import device as d
from uiautomator import Device
from time import sleep
import json
import random
import subprocess
import os
import cv2
import csv
import org.sikuli.script.SikulixForJython
from sikuli.Sikuli import *
#from skimage.measure import compare_ssim
from xml.dom import minidom

notepad = App('notepad.exe')
notepad.open()
sleep(1)
type("It is working!")
notepad.close()

def loadRandomEvent():
    #eventList = ['click','drag','swipe','press','freeze']  
    eventList = ['click']
    return random.choice(eventList)

def compareImage(eventMessage):
    #imageA = cv2.imread("BeforeEvent.png")
    #imageB = cv2.imread("AfterEvent.png")
    #convert between RGB and grayscale
    # gray_imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    #ssim_score = compare_ssim(gray_imageA, gray_imageB)
    # Compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    ###if score == 1:
    ###    compare ="Images are not identical"
    write_output("BeforeEvent.png","AfterEvent.png",eventMessage,"score","diff","compare")

def remove_old_result():
    if os.path.exists('result.csv'):
        os.remove('result.csv')
    else:
        print("This is the first time you running this tool or you have deleted the previous result file")
        return;
        
#Write the headline of the result file
def write_headline(c1, c2, c3, c4,c5,c6):
    with open('result.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([c1, c2, c3, c4,c5,c6])

#Write a row of compare result into result.cvs
def write_output(image1, image2,eventMessage,ssimScore,ssimDifference,compare):
    with open('result.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([image1, image2,eventMessage,"ssimScore","ssimDifference","compare"])
    csvFile.close()

def getCurrentPackageName():
    jsonData=json.dumps(d.info)
    jsonLoadData=json.loads(jsonData)            
    return jsonLoadData["currentPackageName"]
def performEventsOnApp():
    max_iterations =5
    i=1
    print ("Current Package") 
     
    while(i <= max_iterations):
        d.dump("Output3.xml")
        doc = minidom.parse("Output3.xml")
        nodes = doc.getElementsByTagName("node")
        package=doc.getElementsByTagName("node")[0].getAttribute("package")
        length = nodes.length
        print(d(text="START").exists)
        num_events_iteration =50
        for x in range(num_events_iteration):
            print (package)
            print (getCurrentPackageName())
            if(package != getCurrentPackageName()):
                d.press.back()
            node=  nodes[random.randint(1, length-1)]  
            print(node.getAttribute("class"))
            axisCoordinates = node.getAttribute("bounds").split("]")
            xAxis =axisCoordinates[0].replace('[','').split(",")
            xCoordinate =(int(xAxis[0]) + int(xAxis[1]))/2    
            yAxis = axisCoordinates[1].replace('[','').split(",")
            yCoordinate =(int(yAxis[0]) + int(yAxis[1]))/2  
            #screenshot before event --ss1
            #d.click(xCoordinate, yCoordinate)
            randomEvent =loadRandomEvent()
            eventMessage="No Event"
            #d.screenshot("BeforeEvent.png")
            if randomEvent == 'click':
                d.click(xCoordinate, yCoordinate)
                eventMessage ="Performed click at",  str(xCoordinate), str(yCoordinate)
            elif  randomEvent == 'swipe':
                d.swipe(xAxis[0], xAxis[1], yAxis[0], yAxis[1])
                eventMessage ="Performed Swipe at",  xAxis, yAxis
            elif randomEvent == 'press':
                d.press(xCoordinate, yCoordinate)
                eventMessage ="Performed press at",  str(xCoordinate), str(yCoordinate)
            elif randomEvent == 'freeze':
                d.freeze_rotation()   
                eventMessage ="Performed freeze rotation"                
            #d.screenshot("AfterEvent.png")
            compareImage(eventMessage) 
        #screenshot after event -ss2
        #use some kind of image similarity algorithm: open cv(computer vision library) for 
        #comparing these screenshots
        #identify threshold %
        i = i + 1
    
def main():
    remove_old_result()
    write_headline("image1", "image2","eventMessages","ssimScores","ssimDifferences", "comparisonResults")
    performEventsOnApp()
if __name__ == "__main__":
    main()
 # what kind of events we can send it to the device?
 # like tap, swipe, click, etc..--- Manual events is it possible to automate
 #tap and swipe are most common events on games
 #reinforcement learning
 # First stage learn probabilties
 # Second stage use these probabilties- assign probabilties
 #How can I decide if an event is good or not?
 #The event we are sending is effective or not? 
 #classical descriptions of reinforcement learning
 
 #For Friday meeting add, one more event. Open CV library comparison
 #build a dictionary to identify these nodes, the event is effective or not?
 
 
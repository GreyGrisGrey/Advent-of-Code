import requests
from os import path
from os import makedirs

# WIP, functions but not well

def mainManager():
    while input("Collect input data? Y/N ").upper() == "Y":
        res = input("Collect day or year? D/Y ").upper()
        if res == "D":
            dayManager()
        elif res == "Y":
            yearManager()
    return


def dayManager():
    year = input("Input year: ")
    day = input("Input day: ")
    checkYearDir(year)
    createInput(year, day)
    return


def yearManager():
    year = input("Input year: ")
    checkYearDir(year)
    for i in range(1, 26):
        createInput(year, str(i))
    return


def checkYearDir(year):
    res = path.abspath(__file__)
    temp = (res.split("\\"))
    res = "\\".join(temp[0:len(temp)-1:]) + "\\" + str(year)
    if not path.isdir(res):
        makedirs(res)
    

def createInput(year, day):
    string = "https://adventofcode.com/" + year + "/day/" + day + "/input"
    data = collect(string)
    res = path.abspath(__file__)
    temp = (res.split("\\"))
    res = "\\".join(temp[0:len(temp)-1:]) + "\\" + str(year)
    f = open(res + "\\in" + str(day) + ".txt", "w")
    f.write(data)
    

def collect(url):
    #Input session cookie for AoC here.
    sessionCookie = None
    return requests.get(url, cookies={"session": sessionCookie}).text
    
if __name__ == "__main__":
    mainManager()
import requests
from bs4 import BeautifulSoup
from random import randint
import webbrowser
import sys

animals = []

def main():
    URL = "https://a-z-animals.com/animals/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    major_division =  soup.find_all('ul', class_= "list-unstyled row")
    for subsection in major_division:
        anchors = subsection.find_all('a')
        for a in anchors:
            animals.append(a.string)
    if len(animals) == 0:
        print('There was an error when requesting data, please try again')
        sys.exit()
    
    
    random_number = randint (0, len(animals))
    chosen_animal = animals[random_number]
    try:
        webbrowser.open("https://en.wikipedia.org/wiki/" + chosen_animal)
    except:
        webbrowser.open("https://en.wikipedia.org/w/index.php?search=" + chosen_animal + "&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1")


    
   

if __name__ == "__main__":
    main()

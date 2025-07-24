# يقوم البرنامج بجمع 100 منشور و100 صديق, وهذا العديد قابل للتغيير على حسب قيمة المتغير: num_records
# وذلك على 4 مستويات, على حسب المتغير: num_levels
# وحال لم يتواجد هذا العدد من المنشورات والاصدقاء سيتجاوز البرنامج ذلك دون اعطال, اعتماداً على المتغير: allowed_div_down

import time
from bs4 import BeautifulSoup
from selenium import webdriver
import re

def selectUserName(soup):
    time.sleep(1)
    user_name_path = soup.find("span",
                               class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 l1jc4y16 rwim8176 mhxlubs3 p5u9llcw hnhda86s oo9gr5id hzawbc8m")
    user_name = user_name_path.find("div").find("h1", class_="gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl").text
    print("user name: " + user_name)
    # write user's name into the file
    collectionFile.write("user name: " + user_name + "\n")

def collectPosts(browse, url, level):
    if level <= num_levels:
        print("\n" + ("*" * 40) + "\nlevel", level)
        level += 1
    else:
        return

    browse.get(url)
    soup = BeautifulSoup(browse.page_source, "html.parser")
    selectUserName(soup)

    postsList = []
    dive_down = 0
    while True:
        if dive_down > allowed_dive_down:
            break

        browse.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        soup = BeautifulSoup(browse.page_source, "html.parser")
        divs = soup.findAll("div", class_="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q")
        if len(divs) >= num_records:
            break
        else:
            dive_down += 1

    # save them into list
    num_posts = 0
    for div in divs:
        try:
            postsList.append(div.get_text())
            num_posts += 1
            if num_posts == num_records:
                break
        except:
            print("pass post")

    # save them into the file
    collectionFile.write("Posts:\n")
    print("Posts:")

    counter = 0
    for post in postsList:
        counter += 1
        collectionFile.write((str(counter) + " - " + post + "\n"))
        print((str(counter) + " - " + post + "\n"))
    collectionFile.write("\n")
    time.sleep(1)
    openFriendsPage(browse, level)

def openFriendsPage(browse, level):
    soup = BeautifulSoup(browse.page_source, "html.parser")
    friendsPageLinkTag = soup.find("a", attrs={'href': re.compile("friends$")})

    # go to user's friends
    try:
        browse.get(friendsPageLinkTag['href'])
        time.sleep(1)
        collectFriends(browse, level)
    except:
        print()

def collectFriends(browse, level):
    # collect
    friendsList = []
    dive_down = 0
    while True:
        if dive_down > allowed_dive_down:
            break

        browse.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        soup = BeautifulSoup(browse.page_source, "html.parser")
        divs = soup.findAll("div",
                            class_="bp9cbjyn ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi n1f8r23x rq0escxv j83agx80 bi6gxh9e discj3wi hv4rvrfc ihqw7lf3 dati1w0a gfomwglr")
        if len(divs) >= num_records:
            break
        else:
            dive_down += 1

    # save them into list
    num_friends = 0
    for div in divs:
        try:
            friendsList.append(div.find("div").find("a")['href'])
            num_friends += 1
            if num_friends == num_records:
                break
        except:
            print("pass friend")

    # save them into the file
    collectionFile.write("\nFriends Links:\n")
    print("Friends Links:")
    counter = 0
    for friend_url in friendsList:
        counter += 1
        collectionFile.write((str(counter) + "- " + friend_url + "\n"))
    collectionFile.write(("*" * 20) + "\n\n")
    print(friendsList)

    for friend_url in friendsList:
        collectPosts(browse, friend_url, level)


# for login process
email = input("enter your email: ")
password = input("enter your password: ")
num_levels=int(input("أدخل عدد المستويات التي تود النزول اليها في البحث : "))
num_records=int(input("أدخل عدد المنشورات والأصدقاء الذين تود أن تجمعهم للشخص الواحد: "))

# Initialize configurations and Login @
# create file to save (user's posts and Friends Pages) into.
collectionFile = open("collection.txt", "w", encoding="utf8")
# num_records = 2  # how many records of each user's (posts and friends)
# num_levels = 2
allowed_dive_down = 40  # times of diving down through page to collect posts and friends until finishes

base_url = "https://www.facebook.com/login"
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
browse = webdriver.Chrome(options=options)
browse.maximize_window()
browse.get(base_url)

browse.find_element("name", "email").send_keys(email)
browse.find_element("name", "pass").send_keys(password)
browse.find_element("name", "login").click()

time.sleep(1)

# get the url of profile page
soup = BeautifulSoup(browse.page_source, "html.parser")
profile_page_url = \
    soup.find("a",
              class_="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 p7hjln8o kvgmc6g5 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of n00je7tq arfg74bv qs9ysxi8 k77z8yql l9j0dhe7 abiwlrkh p8dawk7l lzcic4wl j83agx80 oi9244e8")[
        'href']

# Collect Posts => Friends => Posts @
collectPosts(browse, profile_page_url, level=1)

# close @
collectionFile.close()
time.sleep(2)
browse.quit()

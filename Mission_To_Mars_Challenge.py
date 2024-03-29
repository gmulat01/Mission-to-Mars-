#!/usr/bin/env python
# Import Splinter and BeautifulSoup
from splinter import Browser
import pandas as pd
import numpy as np
import time
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert browser html to soup object then quit browser
html = browser.html
news_soup = bs(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ## Space Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = bs(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


## Facts about Mars

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


df.to_html()


# # D1: Scrape Hempisphere Images and Titles
# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')

items = soup.find("div", {"class":"results"}).find_all("div", {"class", "item"})
len(items)

test = items[0]
link = test.find("a", {"class": "itemLink"})["href"]
link

full_url = url + link
full_url

browser.visit(full_url)

html = browser.html
soup = bs(html, 'html.parser')

soup.find("img", {"class", "wide-image"})["src"]

soup.find("h2", {"class": "title"}).text.split("Enhanced")[0].strip()

# 2. Create a list to hold the images and titles.
# 3. Write code to retrieve the image urls and titles for each hemisphere.

# base
url = 'https://marshemispheres.com/'

browser.visit(url)

# Soupify main page 
html = browser.html
soup = bs(html, 'html.parser')
items = soup.find("div", {"class":"results"}).find_all("div", {"class", "item"})


# Initiate return 
hemisphere_image_urls = []

#Each Hemisphere on Main Page 
for item in items:
    
    #grab link 
    link = item.find("a", {"class": "itemLink"})["href"]
    full_url = url + link
    
    #Visit link 
    browser.visit(full_url)
    time.sleep(1)
    
    #Soupify 
    html = browser.html
    soup = bs(html, 'html.parser')
    
    #Grab Data
    img = soup.find("img", {"class", "wide-image"})["src"]
    img_url = url + img
    
    title = soup.find("h2", {"class": "title"}).text
    title = title.split("Enhanced")[0].strip()
    
    data = {"img_url": img_url, "title": title}
    
    hemisphere_image_urls.append(data)

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

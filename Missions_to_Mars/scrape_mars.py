#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import BeautifulSoup, Pandas, and Requests/Splinter
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Setup Splinter
executable_path = {"executable_path": ChromeDriverManager().install()}
browser = Browser("chrome", **executable_path, headless=False)


# In[3]:


# Scrape https://redplanetscience.com/ and collect the latest News Title and Paragraph Text
url = "https://redplanetscience.com/"
browser.visit(url)
html = browser.html
soup = bs(html, "html.parser")
news_title = soup.find("div", class_="content_title").text.strip()
news_p = soup.find("div", class_="article_teaser_body").text.strip()
print(news_title)
print(news_p)


# In[4]:


# Use Splinter to navigate https://spaceimages-mars.com/ and find the image url for the current Featured Mars Image
url = "https://spaceimages-mars.com/"
browser.visit(url)
html = browser.html
soup = bs(html, "html.parser")
featured_image_url = soup.find("img", class_="headerimage fade-in")["src"]
featured_image_url = "https://spaceimages-mars.com/" + featured_image_url
print(featured_image_url)


# In[5]:


# At https://galaxyfacts-mars.com/ use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
url = "https://galaxyfacts-mars.com/"
tables = pd.read_html(url, header=0)
mars_df = tables[0]
mars_df.head()


# In[6]:


# Use Pandas to convert the data to a HTML table string
html_table = mars_df.to_html()
html_table


# In[7]:


# Obtain high resolution images for each of Mar's hemispheres at https://marshemispheres.com/
url = "https://marshemispheres.com/"
browser.visit(url)
html = browser.html
soup = bs(html, "html.parser")

# Locate the links to the four hemispheres
links = []
location_data = soup.find_all("div", class_="description")
for location in location_data:
    link = location.find("a")["href"]
    links.append(link)

# Go to each link and pull the image and hemisphere data
hemisphere_image_urls = []
for link in links:
    browser.visit(url + link)
    html = browser.html
    soup = bs(html, "html.parser")
    image_url = soup.find("img", class_="wide-image")["src"]
    image_url = url + image_url
    hemisphere = soup.find("div", class_="cover")
    hemisphere = hemisphere.find("h2").text.strip()
    hemisphere = hemisphere.rsplit(' ', 1)[0]
    print(image_url)
    print(hemisphere)
    hemisphere_dict = {"title": hemisphere, "img_url": image_url}
    hemisphere_image_urls.append(hemisphere_dict)

print(hemisphere_image_urls)


# In[ ]:





# In[8]:


browser.quit()


# In[ ]:





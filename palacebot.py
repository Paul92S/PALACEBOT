#Bot checking for page updates on Palace Skate shop server

#
#      ___  ___   __   ___  _________
#     / _ \/ _ | / /  / _ |/ ___/ __/
#    / ___/ __ |/ /__/ __ / /__/ _/  
#   /_/  /_/ |_/____/_/ |_\___/___/  
#
#
# Developed by Paul92S
# Date 14/11/16
# Version 0.1

# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time
import re

# Import smtplib (to allow us to email)
import smtplib

#import selenium for for browser autonomous browser interaction
from selenium.webdriver.common.by import By

try:
    from selenium import webdriver   
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import Select
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)

while True: 
	# set url of the web shop
	url = "https://shop.palaceskateboards.com/"
	# imitate browser with header set updates
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	# download the webpage
	response = requests.get(url, headers=headers)
	# parse the downloaded page
	soup = BeautifulSoup(response.text, "html5lib")

	# checking for the new release text on webpage "palace x adidas" 
	# if the webpage does not contain this it waits a set time repeats download and check
	if str(soup).find("PALACE BOLTS") == -1:
		# initialise wait 1 second
		time.sleep(1)
		print "No Match...waiting"
		# contain script
		continue 

	# else if the product is now found on the page excute following commands
	else:
		# String search for specific product
		# str(soup).find("TRI-FERG") == 1:
		print "Match found"

		# Location of the chrome web Driver
		driver = webdriver.Chrome()
		driver.get("https://shop.palaceskateboards.com/")
		print driver.title
		# Find element that contains the string of the product you are looking for
		# Eg "TRI-FERG CREW NECK" Drop info (product) usually out before website release
		# Ideally you will have the right info 
		product = driver.find_element_by_link_text("TRI-FERG COAT")
		product.submit()
		time.sleep(2.5)
		# now to add item to cart (with size choice)
		select = Select(driver.find_element_by_id('product-select'))
		select.select_by_visible_text('LARGE')
		driver.find_element_by_name('button').click()
		cart = driver.find_element_by_link_text("Cart")
		cart.submit()
		time.sleep(2.5)
		driver.find_element_by_name('checkout').click()
		checkout = Select(driver.find_element_by_id('paypal-express-checkout-btn'))
		checkout.submit()
		driver.quit()

		break

        




































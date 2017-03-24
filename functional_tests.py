from selenium import webdriver # import selenium lib  


browser = webdriver.Firefox()  # Get local session of firefox

broswer.get('http://localhost:8080')  # Load page

assert 'Django' in broswer.title
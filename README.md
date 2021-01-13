# 10 day coding challenge with Python
These are my solutions for the 10 day winter-break coding challenge. Event link: https://www.facebook.com/events/843253696243420?active_tab=about
Each day there was a problem to solve. The idea of the challenge is to learn something new and adapt the problem to own programming skills. 

## 📖 Table of contents:
  • [Day 1: Palindromes, web scraping](#Day-1:-Palindromes,-web-scraping)
  
  • [Day 2: API, openpyxl](#Day-2:-API,-openpyxl)
  
  • [Day 3: Automatic email sending](#Day-3:-Automatic-email-sending)
  
  • [Day 4: BMI calculator](#Day-4:-BMI-calculator)
  
  • [Day 5: Movie API](#Day-5:-Movie-API)
  
  • [Day 6: Image resizer](#Day-6:-Image-resizer)
  
  • [Day 7: Password_generator](#Day-7:-Password-generator)
  
  • [Day 8: Geo locator](#Day-7:-Geo-locator)


## 🧐 Day 1: Palindromes, web scraping
  ❗ Requirements (from prompt):
  
  1) Check if an inputted word is a palindrome, display adequate message.
  
  2) Run a webpage that displays anagrams of an inputted word.
  
  ↗️ My extension:
  
  ad 2) Use selenium library to web scrape in search for data which I display in the terminal.
  
  🧠 Learned today: 
  
  •  web scraping basics, finding specific tags and classes on a page
  
  •  selenium library for Python
  
  🔗 Helpful links:
  https://selenium-python.readthedocs.io/
  https://www.w3schools.com/python/python_regex.asp
  https://sites.google.com/a/chromium.org/chromedriver/downloads

## ⛅ Day 2: API, openpyxl
  ❗ Requirements (from prompt):
  
  1) Display date, time, day of the week, temperature in a given city. Use https://rapidapi.com/commu.../api/open-weather-map/endpoints

  2) Display a random quote https://type.fit/api/quotes

  3) Use datetime and request libraries

  
  ↗️ My extensions:
  
  Create a calendar card in excel with data from the weather API.
  
  Error messages for requests with error codes other than 200.
  
  🧠 Learned today: 
  
  •  a few useful options for editing spreadsheet (merging, coloring cells, changing font, style)
  
  •  method for calculations on dates (timedelta), strftime for date formatting
  
  🔗 Helpful links:
  https://openweathermap.org/current
  https://rapidapi.com/community/api/open-weather-map/
  https://requests.readthedocs.io/en/master/user/quickstart/#response-content

## 📧 Day 3: Automatic email sending

 ❗ Requirements (from prompt):
  
  1) Send emails to people from a mailing list (in csv or xls), with a message and an image

  2) Secure program for edge cases (no image file, no mailing list etc.)

  
  ↗️ My extensions:
  
  I used a function for getting random quotes from API (from Day 2) as a message content.
  
  I used bing_image_downloader to download an image that represents the quote.  
  
  🧠 Learned today: 
  
  •  smtplib for sending emails
  
  🔗 Helpful links:
  
  https://pypi.org/project/bing-image-downloader/
  https://docs.python.org/3/library/email.examples.html
  https://www.youtube.com/watch?v=m9ojKEBYCvQ
  
## ⚖️ Day 4: BMI calculator
  
  ❗ Requirements (from prompt):
  
  1) Write a program that, given weight in kgs and height in cms calculates BMI.

  2) Then, a program at random chooses a sport activity and time (less or equal to the one given by user).
  
  3) Create a training plan in a text file for the next 7 days.

  
  ↗️ My extensions:
  
  Instead of if-else statements for BMI, I used a map (keys: description, values: smallest and largest value of the index for this category)
  
  Time of activity selected at random, min time is the value of index for given person (people with higher index ought to exercise more) max time is specified by user
  
  In any case time of the activity should be no shorter than 10 minutes.
  
  🧠 Learned today: 
  
  •  "string".format() - formatting string to include values in it, instead of using the + operator many times
  
## 🎞️ Day 5: Movie API
  
 ❗ Requirements (from prompt):
  
  1) Find info about all the parts of movie that a user searches.
  
 ↗️ My extensions:
  
  Used a library terminaltables to display information.
  
 🧠 Learned today: 
 
  • A new, useful API: https://rapidapi.com/apidojo/api/imdb8/endpoints
  
## 🖼️ Day 6: Image resizer
  
 ❗ Requirements (from prompt):
  
  1) Compress image
  
  2) Calculate saved space
  
 ↗️ My extensions:
  
  Used a tkinter library to select origin and destination folder.
  
 🧠 Learned today: 
 
  • Basics of Pillow library.
  
  • How to use tkinter directory selection. 
  
  🔗 Helpful link:
  
  https://auth0.com/blog/image-processing-in-python-with-pillow/
  
  ##  Day 7: Password generator
  
 ❗ Requirements (from prompt):
  
  1) Generate password of a specified length.
  
 ↗️ My extensions:
  
  Used Datamuse API to get words to help remember their password.
  
  For letters - find words that start with a given letter. For special characters - find words that sound familliar or rhyme with, ex. brackets rhymes with jackets.
  
  These words than can be used to create a story / association to quickly remember secure and complicated password.
  
  ##  🌏 Day 8: Geo locator
  
 ❗ Requirements (from prompt):
  
  1) Calculate geo location between your location and any given.
  
 ↗️ My extensions:
  
  Used geocoder to get current location.
  
  🧠 Learned today: 
 
  •  How to get current location with geocoder
  
  🔗 Helpful links:
  
  https://pl.wikibooks.org/.../Astrono.../Odleg%C5%82o%C5%9Bci

  https://rapidapi.com/trueway/api/trueway-geocoding

  
  
 

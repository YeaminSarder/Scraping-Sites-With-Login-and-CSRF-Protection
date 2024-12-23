The script can scrape the https://www.scrapingcourse.com/login/csrf website which requires login and has CSRF protection.

The site generates a dynamic token that requires to be sent in addion to the email and
password in order for the login to succeed.

The script can bypass the protection and scrapes the product names and prices.

if you want to try the script make sure pprint, requests and beautifulsoup are intalled.

sample output:
```
200
Success Page - ScrapingCourse.com
[{'name': 'Chaz Kangeroo Hoodie', 'price': '$52'},
 {'name': 'Teton Pullover Hoodie', 'price': '$70'},
 {'name': 'Bruno Compete Hoodie', 'price': '$63'},
 {'name': 'Frankie  Sweatshirt', 'price': '$60'},
 {'name': 'Hollister Backyard Sweatshirt', 'price': '$52'},
 {'name': 'Stark Fundamental Hoodie', 'price': '$42'},
 {'name': 'Hero Hoodie', 'price': '$54'},
 {'name': 'Oslo Trek Hoodie', 'price': '$42'},
 {'name': 'Abominable Hoodie', 'price': '$69'},
 {'name': 'Mach Street Sweatshirt', 'price': '$62'},
 {'name': 'Grayson Crewneck Sweatshirt', 'price': '$64'},
 {'name': 'Ajax Full-Zip Sweatshirt', 'price': '$69'}]
```

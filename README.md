# articleemailsender
Program making use of Google's APIs and Beautiful Soup web-scraping to automatically send article links via email.

The functionality of this program has been tailored specifically to my use, the uses of the two files are as follows:

### articles.py
This file scrapes two British media sites, the Guardian and the BBC, and finds articles in the categories of Prisons and Criminal
justice. The two functions in this file find such information, and find the title, link and date. The date is then compared to the
current date, to determine whether or not the article's information will then be added to the corresponding lists.

### sender.py
This file deals with Google's authentication, and then creates a message using the information from articles.py, combining the three
lists into an ordered tuple. The items in the list are then iterated through to create a HTML message which is then sent via email
to the recipient.

I personally used this program at Python Anywhere as a scheduled task, allowing me to send newly created articles to my partner.

### Important Notes

This program includes [Gmail's Python Quickstart](https://developers.google.com/gmail/api/quickstart/python), you should make sure to keep the "credentials" function, otherwise you will not be able to begin authenticating this program.

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64 #imports for message sending start here
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from apiclient import errors
import articles

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]

#credentials function
def credentials():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service

#EVERYTHING BELOW THIS LINE CREATES AND SENDS THE MESSAGE

#Article finder function and lists from articles.py

message_text="""
<h1>Good Afternoon!</h1>
<p>Here are some links:</p>
""" # message text that will have links added to it

merged = tuple(zip(articles.titles, articles.links)) #tuple of tuples from scraped links and titles

for item in merged: # for loop adding link html to the message text
    message_text += "<a href='" + item[1] + "'" + ">" + item[0] + "</a>"
    message_text += "<br>"
    if len(message_text) == 60:
        message_text += "<br>" + "<p>Sorry, no links for today!</p>"

print(message_text)

#subject, sender and to for create function
subject = "Hi"
sender = "#"
to = "#"

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text, "html")
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

#---------------------------------------------------------------

#service, id and message for the send function
service = credentials()
user_id = "#"
message = create_message(sender, to, subject, message_text) #create message

def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError:
        print("An error occured")

send_message(service, user_id, message) #send message

#----------------------------------------------------------------

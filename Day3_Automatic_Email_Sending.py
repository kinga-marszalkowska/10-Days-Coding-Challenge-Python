import smtplib
import os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bing_image_downloader import downloader

# function that calls quotes api to get a random quote
from Day2_API_excel import get_random_quote

# save random quote to a map
data = {'quote': get_random_quote()['text'], 'author': get_random_quote()['author']}

# download an image, search by the contents of a quote
downloader.download(query=data['quote'], limit=1, output_dir='attachment//', adult_filter_off=True, force_replace=False, timeout=60)

# save downloaded image,  by default bing downloader creates a folder with query as a name
img_file_name = r"current_project's_path\attachment\\" + data['quote'] + "\Image_1.jpg"

# prepare message
img_data = open(img_file_name, 'rb').read()
msg = MIMEMultipart()

msg['Subject'] = 'A quote from ' + data['author']
msg['From'] = 'e@mail.cc'
msg['To'] = 'e@mail.cc'

# write content of the email
text = MIMEText(data['quote'])

# and attatch it to the message
msg.attach(text)

# attatch the image to the message
image = MIMEImage(img_data, name=os.path.basename(img_file_name))
msg.attach(image)

# data for sending the email
sender = ''
receiver = ''
password = ''

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(sender, password)
s.sendmail(sender, receiver, msg.as_string())
s.quit()

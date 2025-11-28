#Whatsapp automation scheduler

import pywhatkit

phone_number = "Enter the phone number with country code" 
message = "Hello! This is an automated message sent via PyWhatKit."
send_hour = 18 
send_minute = 30 

pywhatkit.sendwhatmsg(phone_number, message, send_hour, send_minute)
print("Message scheduled to be sent at {}:{}".format(send_hour, send_minute))


#Whatapp at the moment sender

import pywhatkit
phone_number = "Enter the phone number with country code" 
message = "Hello! This is an instant message sent via PyWhatKit."
pywhatkit.sendwhatmsg_instantly(phone_number, message)
print("Instant message sent!")

#whatsapp group message sender
import pywhatkit
group_id = "
message="Hello everyone! This is a message sent to the group via PyWhatKit."
pywhatkit.sendwhatmsg_to_group_instantly(group_id, message)
print("Message sent to the group!")

#whatsapp image sender
import pywhatkit
phone_number = "Enter the phone number with country code" 
image_path = "path/to/your/image.jpg"
caption = "Check out this image!"
pywhatkit.sendwhats_image(phone_number, image_path, caption)
print("Image sent successfully!")


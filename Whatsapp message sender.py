# Task 4: Use Python Code to send WhatsApp to everyone


import pywhatkit as kit

# Replace with the recipient's WhatsApp number (in international format)
recipient_number = "+917014471298"

# Send WhatsApp message
kit.sendwhatmsg_instantly(recipient_number, "Hello from Python using PyWhatKit!")



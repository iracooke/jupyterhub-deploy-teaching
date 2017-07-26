#!/usr/bin/env python

#
# Usage:
# email_passwords.py <student_id> | osascript -
#

from string import Template
import argparse
import sys
import yaml

message= """
set theAccount to "Ira Cooke <ira.cooke@jcu.edu.au>"
set recipientName to "{} {}"
set recipientAddress to "{}"
set theSubject to "Login information for BC2023 Bioinformatics Workshops"
set theContent to "Dear {} 

You are being sent this email because you are enrolled in BC2023 (Molecular Genetics). 

In order to complete the Bioinformatics Workshops for this subject 
you will need to be able to login to the notebook server at https://nb2.bioinformatics.guide

Your login details for this server are;

username: {}
password: {}

Please keep these login details private as they will be used to identify you and your work.

Further information on the bioinformatics section of the subject is available on LearnJCU and at http://bc2023.bioinformatics.guide 


"

tell application "Mail"

        ##Create the message
        set theMessage to make new outgoing message with properties {{sender:theAccount, subject:theSubject, content:theContent, visible:true}}

        ##Set a recipient
        tell theMessage
                make new to recipient with properties {{name:recipientName, address:recipientAddress}}

                ##Send the Message
                send

        end tell
end tell
"""



# Command line arguments
#
parser = argparse.ArgumentParser(description='Email login details')

parser.add_argument('student',type=str,
	help='ID of specific student to email',default=sys.stdin)

args  = parser.parse_args()

with open('roles/users/vars/user_info.yml','r') as usersyml:
	users = yaml.safe_load(usersyml)

for user in users['user_info']:
	if user['username'] == args.student:

		filled_message = message.format(user['first'],user['last'],user['email'],user['first'],user['username'],user['password'])

		print(filled_message)

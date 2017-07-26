#!/usr/bin/env python

from xkcdpass import xkcd_password as xp
import yaml
import csv

wordfile = xp.locate_wordfile()
mywords = xp.generate_wordlist(wordfile=wordfile, min_length=3, max_length=5)




def create_user(userdict):
	userdict['password'] = xp.generate_xkcdpassword(mywords, delimiter="-", numwords=3)
	del userdict['role']
	return(userdict)


with open('roles/users/vars/user_info.yml','r') as usersyml:
	users = yaml.safe_load(usersyml)
	usersyml.close()

existing_usernames = [ users['user_info'][i]['username'] for i in range(len(users['user_info'])) ]


with open('BC2023Students2.tsv','r') as tsvfile:
	# dialect = csv.Sniffer().sniff(tsvfile.read(1024))
	# tsvfile.seek(0)
	# reader = csv.reader(tsvfile, dialect)
	reader = csv.DictReader(tsvfile, delimiter="\t", fieldnames = ['username', 'first', 'last', 'email', 'role'])
	for row in reader:
		if row['username'] not in existing_usernames:
			print(row['username'])
#			users['user_info'].append(create_user(row))


with open('roles/users/vars/user_info.yml','w') as usersyml:
	usersyml.write(yaml.dump(users))
	usersyml.close()


with open('roles/students/vars/student_info.yml','w') as studentsyml:
	students = {}
	students['student_info']=users['user_info']
	studentsyml.write(yaml.dump(students))
	usersyml.close()



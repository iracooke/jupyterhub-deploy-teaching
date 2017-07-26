# Setup Base Server

- Start from Ubuntu 16.04
- Edit /etc/ssh/sshd_config to enable root login (Change PermitRootLogin to yes)
- Restart sshd
```
service ssh restart
```

# Run the ansible deploy scripts



```bash
ansible-playbook users.yml
ansible-playbook deploy.yml
ansible-playbook students.yml
```

# Notify students by email of their passwords

for id in $(grep 'Tutor' BC2023Students.tsv | awk '{print $1}' | tr '\n' ' ');do ./email_passwords.py  $id | osascript - ;done

# Certificate renewal

Auto-renewal will tend to fail because it requires nginx to be shutdown in order to perform the renewal process. 

To renew manually

```bash
ssh root@nb.bioinformatics.guide
systemctl stop nginx
certbot-auto renew --no-self-upgrade
systemctl start nginx
```

#Install additional software



# Email passwords to all students

for sid in $(tail -n +3 BC2023Students.tsv | awk '{print $1}' | tr '\n' ' ');do ./email_passwords.py $sid | osascript -;done


for sid in $(cat tricky_students.tsv | awk '{print $1}' | sed 's/\///' | tr '\n' ' ');do ./email_passwords.py $sid | sed 's/\\//'  | osascript -;done

for sid in $(cat BC2023Students_ids2.txt | tr '\n' ' ');do ./email_passwords.py $sid | osascript - ;done
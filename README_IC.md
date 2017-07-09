# Certificate renewal

Auto-renewal will tend to fail because it requires nginx to be shutdown in order to perform the renewal process. 

To renew manually

```bash
ssh root@nb.bioinformatics.guide
systemctl stop nginx
certbot-auto renew --no-self-upgrade
systemctl start nginx
```

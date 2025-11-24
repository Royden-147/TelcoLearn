!/bin/bash

# Count failed SSH login attempts
failed=$(grep -c "Failed password" /var/log/auth.log 2>/dev/null)

# Count successful SSH login attempts
success=$(grep -c "Accepted password" /var/log/auth.log 2>/dev/null)

# Ensure no empty values
[ -z "$failed" ] && failed=0
[ -z "$success" ] && success=0

# Log it cleanly on one line
echo "$(date): Success=$success | Failed=$failed" >> /home/royden147/Desktop/ss



# In the CRONTAB -  "by (crontab -e)"
# */5 * * * * /bin/bash /home/royden147/Desktop/Day_13/cronSSH.sh 
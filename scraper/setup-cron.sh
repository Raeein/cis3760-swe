poetry run python main.py


# set up cron schedule
mv /app/scraper-cron /etc/cron.d/scraper-cron
chmod 0644 /etc/cron.d/scraper-cron
crontab /etc/cron.d/scraper-cron
touch /var/log/cron.log


# set environment variable for cron job
printenv >> /etc/environment


cron && tail -f /var/log/cron.log
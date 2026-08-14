# 1. Install
apt update && apt install -y nginx certbot python3-certbot-nginx rsync

# 2. Buat direktori deploy (sesuai DEPLOY_PATH di secrets)
mkdir -p /var/www/pun.co.id
chown -R $USER:$USER /var/www/pun.co.id

# 3. Nginx config
cp deploy/nginx.conf.example /etc/nginx/sites-available/pun.co.id
ln -s /etc/nginx/sites-available/pun.co.id /etc/nginx/sites-enabled/
nginx -t && systemctl reload nginx

# 4. SSL (harus DNS sudah nunjuk ke IP VPS dulu)
certbot --nginx -d pun.co.id -d www.pun.co.id

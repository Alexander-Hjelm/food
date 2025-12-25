# food-app web

## Running on Raspberry PI

### 1. Installation

```sh
cd /home/pi/
git clone https://github.com/Alexander-Hjelm/food
sudo chmod +x /home/pi/food/web/run.sh
sudo chmod +x /home/pi/food/web/update.sh
```

### 2. systemd service files

#### /etc/systemd/system/food-app.service

```sh
[Unit]
Description=Alexanders Food
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/food/web
ExecStart=/home/pi/food/web/run.sh
Restart=always

[Install]
WantedBy=multi-user.target
```

#### /etc/systemd/system/food-app-update.service

```sh
[Unit]
Description=Update food
After=multi-user.target

[Service]
User=root
Type=simple
WorkingDirectory=/home/pi/food/web
ExecStart=/bin/bash /home/pi/food/web/update.sh

Restart=always
RestartSec=60

[Install]
WantedBy=multi-user.target
```

### 3. Start systemd services

```sh
systemctl daemon-reload
sudo systemctl start food-app
sudo systemctl start food-app-update
```
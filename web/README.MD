# food-app web

## Running on Raspberry PI

### 1. Installation

```sh
cd /home/pi/
git clone https://github.com/Alexander-Hjelm/food
touch /home/pi/food/web/run.sh
sudo chmod +x /home/pi/food/web/run.sh
touch /home/pi/food/web/update.sh
sudo chmod +x /home/pi/food/web/update.sh
```

### 2. create executables

#### /home/pi/food/web/run.sh

```sh
#!/usr/bin/env bash

export FLASK_APP="app"
export FLASK_ENV="development"

python3 init_db.py
flask run --host=0.0.0.0
```

#### /home/pi/food/web/update.sh

```sh
#!/usr/bin/env bash

systemctl stop food-app
git pull
systemctl start food-app
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
ExecStart=/home/pi/food/web/update.sh

Restart=always
RestartSec=86400

[Install]
WantedBy=multi-user.target
```

### 3. Start systemd services

```sh
systemctl daemon-reload
sudo systemctl start food-app
sudo systemctl start food-app-update
```
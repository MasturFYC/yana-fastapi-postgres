#!/usr/bin/env bash

echo "create a test service ..."
# cp test.sh /etc/init.d/test
cp test /etc/init.d/
#chmod +x /etc/init.d/test
chmod +x /etc/init.d/test
# sed -i "s/Your_User_Name/you_path/g" /etc/init.d/test
echo "created the test service"
# chmod 755 app.py
# sudo bash ./install.sh

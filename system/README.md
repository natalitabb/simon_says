# Setting up a Raspberry Pi as a Wireless Access Point

Source: [WIRELESS ACCESS-POINT](https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md)

```bash
sudo apt update
sudo apt upgrade

sudo apt install dnsmasq hostapd
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd

sudo cp /etc/dhcpcd.conf /etc/dhcpcd.conf.bkp
sudo vi /etc/dhcpcd.conf
```

Add to the end:

```text
interface wlan0
    static ip_address=192.168.0.10/24
    nohook wpa_supplicant
```

```bash
sudo service dhcpcd restart

sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.bkp
sudo vi /etc/dnsmasq.conf
```

Copy into the file:

```text
interface=wlan0
  dhcp-range=192.168.0.11,192.168.0.30,255.255.255.0,24h
```

```bash
sudo systemctl start dnsmasq
sudo vi /etc/hostapd/hostapd.conf
```

The file will have the following content, just replace `NETWORK` and `PASSWORD` for the WiFi name and password:

```text
interface=wlan0
driver=nl80211
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
ssid=NETWORK
wpa_passphrase=PASSWORD
```

```bash
sudo vi /etc/default/hostapd
```

Look for the line with `#DAEMON_CONF` and replace it for:

```text
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

```bash
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd

sudo systemctl status hostapd
sudo systemctl status dnsmasq
```

More information [here](https://thepi.io/how-to-use-your-raspberry-pi-as-a-wireless-access-point/)
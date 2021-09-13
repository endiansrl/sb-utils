# Installation

```
python3 -m venv .
. bin/activate
pip install wheel
pip install -r requirements.txt
```

Or

```
./run-in-docker.sh
```

# Usage

Create a credentials.txt file with the following content:

```
[credentials]
sb_url = your_switchboard_url_without_https.com
username = your_switchboard@username.com
password = YourPassword123
api_key = 75446b1b-8a43-4acc-aaab-138275bf63
```

Create a YAML test case file

```
---
  - description: Listing the users
    command: listUsers
  - description: Listing the gateways
    command: listGateways
```

```
---
  - description: List the gateways
    command: listGateways

  - description: Create a new gateway
    command: createGateway
    name: testgateway
    remark: this is a test gateway
    #domain: Endian

  - description: Listing gateways again
    command: listGateways

  - description: Delete the gateway
    command: deleteGateway
    name: testgateway
```

And run it:

```
python sb-exec.py testcases/test-case.yml
```

Watch the show:

```
2021-02-13 09:06:50.201 | DEBUG    | __main__:login:28 - Logging in at 192.168.30.61 with: g.tabacar@endian.com:**********
2021-02-13 09:06:50.230 | DEBUG    | __main__:login:39 - Login successful.
2021-02-13 09:06:50.230 | INFO     | __main__:exec:58 - Running: Listing the users
2021-02-13 09:06:50.230 | INFO     | __main__:exec:63 - {'api_key': '01245664-fda9-4862-ab83-3e6c5e3b8e35'}
2021-02-13 09:06:50.238 | DEBUG    | __main__:exec:listUsers:65 - b'[{"name": "croit"}, {"name": "testdc"}, {"name": "g.tabacar@endian.com"}]'
2021-02-13 09:06:50.238 | INFO     | __main__:exec:58 - Running: Listing the gateways
2021-02-13 09:06:50.238 | INFO     | __main__:exec:63 - {'api_key': '01245664-fda9-4862-ab83-3e6c5e3b8e35'}
2021-02-13 09:06:50.245 | DEBUG    | __main__:exec:listGateways:65 - b'[{"name": "polished-hill-7884"}]'
2021-02-13 09:06:50.246 | DEBUG    | __main__:logout:46 - Logged out.
```

```
021-02-13 09:08:46.499 | DEBUG    | __main__:login:28 - Logging in at 192.168.30.61 with: g.tabacar@endian.com:**********
2021-02-13 09:08:46.527 | DEBUG    | __main__:login:39 - Login successful.
2021-02-13 09:08:46.527 | INFO     | __main__:exec:58 - Running: List the gateways
2021-02-13 09:08:46.527 | INFO     | __main__:exec:63 - {'api_key': '01245664-fda9-4862-ab83-3e6c5e3b8e35'}
2021-02-13 09:08:46.534 | DEBUG    | __main__:exec:listGateways:65 - b'[{"name": "polished-hill-7884"}]'
2021-02-13 09:08:46.534 | INFO     | __main__:exec:58 - Running: Create a new gateway
2021-02-13 09:08:46.534 | INFO     | __main__:exec:63 - {'name': 'testgateway', 'remark': 'this is a test gateway', 'api_key': '01245664-fda9-4862-ab83-3e6c5e3b8e35'}
2021-02-13 09:08:46.650 | DEBUG    | __main__:exec:createGateway:65 - b'{"gateway_interfaces": [], "gateway_easyvpn_client_gateway": null, "gateway_timezone": "Europe/Rome", "gateway_red_dev": null, "gateway_red_dns": null, "gateway_wifi_hidden": null, "gateway_green_ips": "192.168.0.15/24", "gateway_vpn_server_ip": null, "gateway_orange_dev": null, "gateway_emc_profile": null, "gateway_address": null, "gateway_country": "Italy", "gateway_hostname": null, "gateway_longitude": null, "vpn_dnat": null, "gateway_auto_assigned_virtualnetwork": true, "gateway_red_type": "dhcp", "gateway_emc_version": null, "vpn_custom_dns": null, "gateway_wifi_red_dns": null, "gateway_emc_status": null, "vpn_remote_nets": ["100.64.0.4/30"], "gateway_red_apn": null, "gateway_virtualnetwork": "100.64.0.4/30", "gateway_red_ips": null, "name": "testgateway", "gateway_email": "g.tabacar@endian.com", "gateway_modem_port": "", "vpn_green": false, "vpn_domain": null, "ssh_public_key": null, "domain": null, "gateway_proxy_enabled": null, "sequence": 27, "gateway_blue_ips": null, "gateway_emc_maintenance_expiration": null, "gateway_blue_dev": null, "gateway_modem_type": null, "gateway_disable_virtual_ip": false, "gateway_proxy_ntlm": null, "gateway_manager": ["user:g.tabacar@endian.com"], "vpn_push_domain": false, "gateway_xmpp_status": null, "gateway_policies": null, "gateway_localnetwork": "", "gateway_easyvpn_client_enabled": null, "gateway_emc_profile_name": null, "gateway_emc_model": null, "vpn_explicit_routes": null, "vpn_blue": false, "gateway_model": "", "gateway_emc_release": null, "remark": "this is a test gateway", "vpn_red": false, "vpn_enabled": true, "gateway_wifi_bssid": null, "gateway_red_gw": null, "gateway_easyvpn_server_address": null, "gateway_located_ip": null, "gateway_endian": false, "vpn_static_ips": null, "vpn_pushed_networks": [], "gateway_vpn_fallback_ip": null, "gateway_easyvpn_server_enabled": null, "ID": "6027971e3b9ce90756eea871", "vpn_snat": [], "type": "gateway", "gateway_wifi_wpa_psk": null, "gateway_wifi_red_ips": null, "gateway_efw_git_hash": null, "vpn_dont_push_routes": false, "gateway_location_type": null, "gateway_proxy_port": null, "gateway_virtualnetwork_size": "/30", "vpn_orange": false, "enabled": true, "gateway_company": "switchboard", "gateway_devices": [{"remark": "Gateway", "physical_ip_address": "127.0.0.1", "name": "gateway@testgateway", "virtual_ip_address": "", "snat": false, "custom": "", "enabled": true, "ID": "6027971e3b9ce90756eea873", "action_profile": "5f453620cbb93e148e1b2ea4", "gateway": "6027971e3b9ce90756eea871"}], "gateway_wifi_red_gw": null, "gateway_domainname": null, "gateway_latitude": null, "gateway_regularuser": [], "gateway_port_forwarding": null, "gateway_poi": null, "gateway_wifi_ipv4_method": "dhcp", "vpn_push_gateways": true, "gateway_emc_git_hash": null, "otr_public_key": null, "gateway_wifi_ssid": null, "gateway_green_dev": null, "gateway_easyvpn_server_clients": null, "gateway_emc_product": null, "gateway_wifi_mode": null, "gateway_emc_group": null, "gateway_proxy_useragent": null, "gateway_wifi_key_mgmt": "wpa-psk", "gateway_emc_group_name": null, "gateway_memberof": [], "gateway_activationcode": null, "vpn_push_custom_dns": false, "gateway_openvpn_nat_support": true, "gateway_proxy_server": null, "gateway_auto_registration": false, "gateway_orange_ips": null, "gateway_serial": "", "time": 1613207326.646017, "gateway_emc_brand": null, "gateway_proxy_user": null, "old_password": null}'
2021-02-13 09:08:46.650 | INFO     | __main__:exec:58 - Running: Listing gateways again
2021-02-13 09:08:46.650 | INFO     | __main__:exec:63 - {'api_key': '01245664-fda9-4862-ab83-3e6c5e3b8e35'}
2021-02-13 09:08:46.657 | DEBUG    | __main__:exec:listGateways:65 - b'[{"name": "polished-hill-7884"}, {"name": "testgateway"}]'
2021-02-13 09:08:46.658 | INFO     | __main__:exec:58 - Running: Delete the gateway
2021-02-13 09:08:46.658 | INFO     | __main__:exec:63 - {'name': 'testgateway', 'api_key': '01245664-fda9-4862-ab83-3e6c5e3b8e35'}
2021-02-13 09:08:46.691 | DEBUG    | __main__:exec:deleteGateway:65 - b'{"info": "Gateway deleted", "code": "ACCESS-I-171", "time": 1613207326.686556}'
2021-02-13 09:08:46.692 | DEBUG    | __main__:logout:46 - Logged out.
```

Logs are displayed in stdout and saved in testcases/test-case.yml.log
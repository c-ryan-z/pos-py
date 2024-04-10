import platform
import uuid

import requests


def get_ip_info():
    ip = requests.get('https://api64.ipify.org').text
    ip_info = requests.get(f'https://ipinfo.io/{ip}/json').json()
    location = f"{ip_info['city']}, {ip_info['region']}, {ip_info['country']}"
    return ip, location


def device_infos():
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0, 8 * 6, 8)][::-1])
    os_info = platform.system() + " " + platform.release()
    return mac_address, os_info


def email_infos():
    ip, location = get_ip_info()
    mac_address, os_info = device_infos()
    return location, os_info


def reset_info():
    ip, location = get_ip_info()
    mac_address, os_info = device_infos()
    return ip, location, mac_address, os_info


if __name__ == '__main__':
    print(email_infos())
    print(device_infos())
    print(get_ip_info())

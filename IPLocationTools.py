import requests
from optparse import OptionParser

parser=OptionParser()
def get_ip():
    parser.add_option("-i","--ip",dest="ip",help="enter ip")
    options = parser.parse_args()[0]
    if not options.ip:
        print("Enter ip address")
    return options
def check():
    r = requests.get("https://ipinfo.io/")
    if r.status_code == 200:
        print("\n[+] server is online!\n")
    else:
        print("\n[!] offline server !\n")
        exit() #! Çıkış yapıyoruz
user_ip_address=get_ip()
user_ip=user_ip_address.ip


check()

country = requests.get("https://ipinfo.io/{}/country/".format(user_ip)).text
city = requests.get("https://ipinfo.io/{}/city/".format(user_ip)).text
region = requests.get("https://ipinfo.io/{}/region/".format(user_ip)).text
postal = requests.get("https://ipinfo.io/{}/postal/".format(user_ip)).text
timezone = requests.get("https://ipinfo.io/{}/timezone/".format(user_ip)).text
organization = requests.get("https://ipinfo.io/{}/org/".format(user_ip)).text
location =  requests.get("https://ipinfo.io/{}/loc/".format(user_ip)).text


print("İp: "+user_ip)
print("Country"+country)
print("City: "+city)
print("Region: "+region)
print("Postal: "+postal)
print("Timezone: "+timezone)
print("Organization: "+organization)
print("Location: "+location)
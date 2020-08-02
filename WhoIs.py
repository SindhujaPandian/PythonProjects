from ipwhois import IPWhois
import pprint

ip_address = input("Enter the Ip Address : ")

obj = IPWhois(ip_address)

results = obj.lookup_whois()

pprint.pprint(results)

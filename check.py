import sys
import re

######
# https://github.com/nyucel/pardus-check/blob/master/get_package_info.py
######

def get_package_info(package_info, info):
    return re.search(info+": (.*)", package_info).group(1)

def get_package_sha256sum(package_info):
    return get_package_info(package_info, 'SHA256')

def get_package_version(package_info):
    return get_package_info(package_info, 'Version')
    
def get_package_name(package_info):
	    return get_package_info(package_info, 'Package')

def get_package_filename(package_info):
    return './' + '/'.join(get_package_info(package_info, 'Filename').split('/')[2:])
###

###Debian###

dpackages_file_path = "/home/simgekabatas/Desktop/pardus_odev/debCompareRepo-master/DebianPackage/debPackages.txt"

dpackages_file = file(dpackages_file_path).read()

dpackages_list = dpackages_file.split('\n\n')

dpname=[]
dsha256 = {}
dversion = {}

print(len(dpackages_list))
for dpackage_info in dpackages_list:
    if len(dpackage_info) < 10:
          continue
    #package_name = get_package_name(dpackage_info)
    dpackage_filename = get_package_filename(dpackage_info)
    dpackage_sha256sum = get_package_sha256sum(dpackage_info)
    dpackage_version = get_package_version(dpackage_info)
    dpackage_name=get_package_name(dpackage_info)
    dsha256[dpackage_name] = dpackage_sha256sum
    dversion[dpackage_name] = dpackage_version
    dpname.append(dpackage_name)


###Pardus###



ppackages_file_path= "/home/simgekabatas/Desktop/pardus_odev/debCompareRepo-master/PardusPackage/pardusPackages.txt"

ppackages_file = file(ppackages_file_path).read()

ppackages_list = ppackages_file.split('\n\n')

ppname=[]
psha256 = {}
pversion = {}

print(len(ppackages_list))
for ppackage_info in ppackages_list:
    if len(ppackage_info) < 10:
        continue
    #package_name = get_package_name(ppackage_info)
    ppackage_filename = get_package_filename(ppackage_info)
    ppackage_sha256sum = get_package_sha256sum(ppackage_info)
    ppackage_version = get_package_version(ppackage_info)
    psha256[ppackage_name] = ppackage_sha256sum
    pversion[ppackage_name] = ppackage_version
    ppname.append(ppackage_name)

ppname2=ppname
aynı_paket_farklı_paket_sayısı=[]
 aynı_paket_surum=[]
#debpacketi kadar çalışcak   
 for debpacket in   dpn
    if debpacket==ppname 
     #aynı paket name ise
       if dsha256[debpacket]==psha256[debpacket] 
         #aynı sha ise surunde aynıdır           
            aynı_paket_surum.append(dpn)
            
       else
           #aynı paket sha farklı o zaman versiyon kontrol
           if dversion[debpacket]==pversion[debpacket] 
            #sha lar farklıysa surumde farklıdır o zaman ekranaa farklı sürümle
              aynı_paket_farklı_paket_sayısı.append("Debian Version:"+dversion(debpacket)+"Pardus Version:" +pversion(debpacket))
              ppname2.remove(debpacket) 


sadece_pardus=[]
     #paket nameler farklıysa 
  for par in  ppname2:
     sadece_pardus.append(ppname)

print(len(aynı_paket_surum)
print(len(aynı_paket_farklı_paket_sayısı)
print(len(ppname)-len(ppname2))









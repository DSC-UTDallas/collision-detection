import exifread
import csv 
f = open("C:/Users/Owner/source/repos/Exif_Exctractor/exif_test.jpg", 'rb')
tags = exifread.process_file(f)
#print(tags)

GPS = tags.get('Image GPSInfo')
dateTime = tags.get('Image DateTime')
print(dateTime)

with open('Ledger.csv', mode='w') as ledger:
    ledger = csv.writer(ledger, delimiter =',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    ledger.writerow([dateTime,GPS])



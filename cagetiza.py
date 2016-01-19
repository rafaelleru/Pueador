import os
import wget

url =  'http://jose-linares.com/scripts/caged.sh'
file=wget.download(url)

os.system('sh'+file)

print 'mejor no toques el log xD'

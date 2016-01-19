import os
import wget
import os.path

def cagetizar():
    url =  'http://jose-linares.com/scripts/caged.sh'
    if not os.path.exists('caged.sh'):
        file=wget.download(url)

    print 'ya descargado'
    os.system('sh '+file)

    print 'has sido cagetizado'
    print 'mejor no toques el log xD'

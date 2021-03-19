from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    '''Main program process'''
    print('*' * 80)

    #html = urlopen('https://refaccionariamario.com/categorias/1509-1954-1968-1200-carburado#/page-2')
    html = urlopen('https://refaccionariamario.com/categorias/1380-vw-sedan-tipo-1?id_category=1380&n=1264') 
    bs = BeautifulSoup(html.read(), 'html.parser')
    product_info = bs.find_all('div', {'class':'product-container'})
    
    # title
    # price
    # href
    
    '''    
    for name in product_info:
        print(name.contents)
    '''

    info = str(product_info[0])
    
    href_start= info.find('href') + 6
    href_finish = info.find('itemprop') - 2
    print(info[href_start:href_finish])

    print('*' * 80)





    














if __name__ == '__main__':
    main()

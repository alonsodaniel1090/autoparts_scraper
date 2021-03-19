from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    '''Main program process'''
    print('*' * 80)

    html = urlopen('https://refaccionariamario.com/categorias/1380-vw-sedan-tipo-1?id_category=1380&n=1264') 
    bs = BeautifulSoup(html.read(), 'html.parser')
    product_info = bs.find_all('div', {'class':'product-container'})
     
    # Get all the information for each product
    info = str(product_info[0])

    # href    
    href_start= info.find('href') + 6
    href_finish = info.find('itemprop') - 2
    href = info[href_start:href_finish]
    print(href)

    print('\n')

    # title
    title_start= info.find('title', href_start) + 7
    title_finish = info.find('>', title_start) - 1
    title = info[title_start:title_finish]
    print(title)

    print('\n')

    # price 
    price_start = info.find('<span') + 52
    price_finish = info.find('</span>', price_start) - 2
    price = str(info[price_start:price_finish])
    print(price.strip()) 




    print('*' * 80)





    














if __name__ == '__main__':
    main()

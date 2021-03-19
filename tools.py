from urllib.request import urlopen
from bs4 import BeautifulSoup
import parts

def main():
    '''Main program process'''

    html = urlopen('https://refaccionariamario.com/categorias/1380-vw-sedan-tipo-1?id_category=1380&n=1264') 
    bs = BeautifulSoup(html.read(), 'html.parser')
    product_info = bs.find_all('div', {'class':'product-container'})
    total_products = 1264 

    print('*' * 80)

    for i in range(total_products - 1): 
   
        # Get all the information for each product
        info = str(product_info[i])

        # Get the href link and the index start of the href tag
        href, href_start = parts.get_link(info)
        print(href)
        

        # Get the product title
        title = parts.get_title(info, href_start)
        print(title)

        
        # Get the product title 
        price = parts.get_price(info)
        print(price)


        print('*' * 80)





    














if __name__ == '__main__':
    main()

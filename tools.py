from urllib.request import urlopen
from bs4 import BeautifulSoup
import parts
from info_parts import InfoParts

def main():
    '''Main program process'''

    # Set the website to get the information
    html = urlopen('https://refaccionariamario.com/categorias/1380-vw-sedan-tipo-1?id_category=1380&n=1264') 
    bs = BeautifulSoup(html.read(), 'html.parser')
    product_info = bs.find_all('div', {'class':'product-container'})
    total_products = 1264 

    print('*' * 80)
    
    # Set the list of products 
    products = []

    # Get all the products information
    for i in range(total_products - 1): 
   
        # Get all the information for each product
        info = str(product_info[i])
        href, href_start = parts.get_link(info)
        title = parts.get_title(info, href_start)
        price = parts.get_price(info)

        # Create the objects
        product = InfoParts(title, price, href)         

        products.append(product)

    # Print the products
    for prod in products:
        print(prod.get_title())
        print(prod.get_price())
        print(prod.get_link())
        print('*' * 80)





    














if __name__ == '__main__':
    main()

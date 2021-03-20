from urllib.request import urlopen
from bs4 import BeautifulSoup
import parts
from info_parts import InfoParts
import csv


def main():
    '''Main program process'''

    # Set the website to get the information
    html = urlopen('https://refaccionariamario.com/categorias/1380-vw-sedan-tipo-1?id_category=1380&n=1264') 
    bs = BeautifulSoup(html.read(), 'html.parser')
    product_info = bs.find_all('div', {'class':'product-container'})
    total_products = 1264 

    print('*' * 80)
    
    # Set the list for all the products 
    products = []

    # Get all the products information
    for i in range(total_products - 1): 
   
        # Get the information for each product
        info = str(product_info[i])
        href, href_start = parts.get_link(info)
        title = parts.get_title(info, href_start)
        price = parts.get_price(info)

        # Create the object
        product = InfoParts(title, price, href)         
        
        # Set a list to store the values of the object
        product_list = []
        product_list.append(product.get_title())
        product_list.append(product.get_price())
        product_list.append(product.get_link())
        
        # Add the list with the object values to the all products list
        products.append(product_list)

    create_csv_file(products)






def create_csv_file(products):
    with open('products.csv', 'w', encoding='utf-8') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        for prod in products:
            filewriter.writerow(prod)
    print('File created!')

    














if __name__ == '__main__':
    main()

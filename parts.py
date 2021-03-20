'''
Helper functions to extract
the information from a 
website with BeautifulSoup
'''
import csv


def get_link(info):
    '''
    Gets a beautifulsoup object as info
    and parse it to return the link of 
    an specific product.
    '''
    href_start= info.find('href') + 6
    href_finish = info.find('itemprop') - 2
    href = info[href_start:href_finish] 
    return href, href_start

def get_title(info, reference):
    '''
    Gets a beautifulsoup object as info
    and the start of a href tag as referene
    to parse it and return the product title.
    '''
    title_start= info.find('title', reference) + 7
    title_finish = info.find('>', title_start) - 1
    title = info[title_start:title_finish]
    return title
 
def get_price(info):
    '''
    Gets a beautifulsoup objects as info 
    and parse it to find the price of the 
    product and then return it.
    '''
    price_start = info.find('<span') + 52
    price_finish = info.find('</span>', price_start) - 2
    price = str(info[price_start:price_finish])
    return price.strip()


def create_csv_file(products):
    '''
    Create a CSV file with
    a the list of products
    passed as an argument.
    '''
    with open('products.csv', 'w', encoding='utf-8') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        for prod in products:
            filewriter.writerow(prod)
    print('File created!')



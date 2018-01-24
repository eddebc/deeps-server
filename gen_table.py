#!/bin/env python
"""
This script fills up 10 rows of HTML table using the file
RowTemplate.html
with random values, currently.
"""
TEMPLATE = "RowTemplate.html"
PAGE_TEMPLATE = "NewbooTemplate.html"
PAGE_OUTPUT = "NewbooTabled.html"


def one_row(product_rank, product_image, product_link, product_name, 
            product_brand, star_ratings, review_count, *args, **kw):
    product_score = star_ratings/10
    with open(TEMPLATE) as fo:
        row = fo.read()
    return row.format(**locals())


def generate_table():
    rows = []
    product_image = "./newboo/shoe.jpg"
    product_link = "http://www.newboo.com"
    product_name = "Whatever product you wish for it to be"
    product_brand = "BestBrand"
    star_ratings = 95
    review_count = 67
    for i in range(1, 11):
        product_rank = i
        rows.append(one_row(**locals()))
        star_ratings = star_ratings - i
        review_count = review_count - i
    
    with open(PAGE_TEMPLATE) as fo:
        page = fo.read().format(table_rows='\n'.join(rows))
    with open(PAGE_OUTPUT, 'w') as fw:
        fw.write(page)


if __name__ == '__main__':
    generate_table()

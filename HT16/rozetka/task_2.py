import subprocess

category = 'mobile-phones/c80003/'
out_file = f'{category.split("/")[1]}.csv'
proc = subprocess.run(
    ['scrapy', 'crawl', 'rozetka', '-O', out_file,
     '-a', f'category={category}']
)


import subprocess

out_file = 'webstore_info.csv'
proc = subprocess.run(
    ['scrapy', 'crawl', 'webstore_spider', '-O', out_file]
)


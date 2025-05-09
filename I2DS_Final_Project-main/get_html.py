import requests
from bs4 import BeautifulSoup
import cloudscraper
import json
import re

def get_html():
    url = 'https://batdongsan.com.vn/nha-dat-cho-thue-tp-hcm'
    
    # Create a cloudscraper instance
    scraper = cloudscraper.create_scraper(delay=10, browser="chrome")
    
    try:
        # Get content of the first page
        content = scraper.get(url)
        content.encoding = 'utf-8'
        soup = BeautifulSoup(content.text, 'html.parser')
        
        # Get number of pages
        num_of_page = soup.find('span', class_='re__pagination-number').get('data-total-page')
        print(f"Tổng số trang: {num_of_page}")
        
        # Get url list in first page
        url_list = []
        a_tags_list = soup.find_all('a', class_='re__card-title')
        for a_tag in a_tags_list:
            href = a_tag.get('href')
            if href:
                url_list.append('https://batdongsan.com.vn' + href)
        
        # Similarly, let's scrape the rest of the pages 
        page = '/p'
        for num_page in range(2, int(num_of_page) + 1):
            print(f"Đang lấy trang {num_page}...")
            content = scraper.get(url + page + str(num_page))
            content.encoding = 'utf-8'
            soup = BeautifulSoup(content.text, 'html.parser')
            a_tags_list = soup.find_all('a', class_='re__card-title')
            for a_tag in a_tags_list:
                href = a_tag.get('href')
                if href:
                    url_list.append('https://batdongsan.com.vn' + href)
        
        # Save URLs to file
        with open('url_list.txt', 'w', encoding='utf-8') as f:
            for url in url_list:
                f.write(url + '\n')
                
        print(f"Đã lưu {len(url_list)} URLs vào file url_list.txt")
            
    except Exception as e:
        print(f"Lỗi khi lấy dữ liệu: {e}")

if __name__ == "__main__":
    get_html() 
import requests
import os

def download_file(url, file_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {url} to {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

def download_files():
    base_url = 'https://static.storm.tg/nft/'
    for i in range(1, 11):
        url = f"{base_url}{i}.json"
        file_path = os.path.join(os.getcwd(), f"{i}.json")
        download_file(url, file_path)
    print('All files downloaded.')

if __name__ == '__main__':
    download_files()

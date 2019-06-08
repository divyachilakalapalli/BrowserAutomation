from selenium import webdriver
import os
import json
import urllib.request
import time
# adding path to geckodriver to the OS environment variable
# assuming that it is stored at the same path as this script
os.environ["PATH"] += os.pathsep + os.getcwd()
download_path = "pawan_pics/"

def main():
    searchtext = 'pawan kalyan katamarayudu'
    num_requested =10
   
    if not os.path.exists(download_path + searchtext.replace(" ", "_")):
        os.makedirs(download_path + searchtext.replace(" ", "_"))

    url = "https://www.google.co.in/search?q="+searchtext+"&source=lnms&tbm=isch"
    driver = webdriver.Chrome("/home/divya/Desktop/Python/webdriver/chromedriver")
    driver.get(url)

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    extensions = {"jpg", "jpeg", "png", "gif"}
    
    img_count = 0
    downloaded_img_count = 0
    
    imges = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
    print("Total images:", len(imges), "\n")
    
    for img in imges:
        img_count += 1
        img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
        img_type = json.loads(img.get_attribute('innerHTML'))["ity"]
        print("Downloading image", img_count, ": ", img_url)
        try:
            if img_type not in extensions:
                img_type = "jpg"
            req = urllib.request.Request(img_url, headers=headers)
            opener = urllib.request.build_opener()
            raw_img = opener.open(req).read()
            f = open(download_path+searchtext.replace(" ", "_")+"/"+str(downloaded_img_count)+"."+img_type, "wb")
            f.write(raw_img)
            downloaded_img_count += 1
            print("download completed")
        except Exception as e:
            print("Download failed:", e)
        if downloaded_img_count >= num_requested:
            break
    print("Total downloaded: ", downloaded_img_count, "/", img_count)
    time.sleep(2)
if __name__ == "__main__":
    main()


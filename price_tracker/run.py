import time
import check_price
import send_mail

url = 'https://www.amazon.com/Nokia-Steel-Hybrid-Smartwatch-Resistant/dp/B0798GWRGG/ref=sr_1_9?keywords=activity%2Btrackers%2Band%2Bsmartwatches&pd_rd_r=a6c0a0a4-29d8-4cfd-921c-280c740d508b&pd_rd_w=JX9Xe&pd_rd_wg=FU6Y3&pf_rd_p=33f8f65b-b95c-44af-8b89-e59e69e79828&pf_rd_r=T1N28BM9FNAEA37ASGCN&qid=1663312795&sr=8-9&th=1'
target_price = 70
filename = "AmazonData.csv"
to_address = "olaitansalaam@outlook.com"

def track_price():
    url = input("Paste url: ")
    target_price = int(input("What is your target price? "))
    product = input("Product name: ")
    filename = product + ".csv"
    to_address = input("Email to get notification: ")
    
    while True: 
        price = check_price.check_price(url=url, filename=filename)
        if price <= target_price:
            send_mail.send_mail(price=price, to_address=to_address, product=product)
        else:
            time.sleep(86400)
            continue


if __name__ == "__main__":
    track_price()
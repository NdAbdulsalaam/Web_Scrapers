import time
import check_price
import send_mail

url = 'https://www.amazon.com/Nokia-Steel-Hybrid-Smartwatch-Resistant/dp/B0798GWRGG/ref=sr_1_9?keywords=activity%2Btrackers%2Band%2Bsmartwatches&pd_rd_r=a6c0a0a4-29d8-4cfd-921c-280c740d508b&pd_rd_w=JX9Xe&pd_rd_wg=FU6Y3&pf_rd_p=33f8f65b-b95c-44af-8b89-e59e69e79828&pf_rd_r=T1N28BM9FNAEA37ASGCN&qid=1663312795&sr=8-9&th=1'
target_price = 230
product = "Smartwatch"
to_address = "olaitansalaam@outlook.com"

def track_price(url=url, target_price=target_price, product=product, to_address=to_address):
    test = input("Do you want to use test data (y/n)?: ")
    if test.lower() == "y":
        filename = product + ".csv"
        # url = url
        # target_price = target_price
        # filename = filename
        # to_address = to_address
    else:
        url = input("Paste url: ")
        target_price = int(input("What is your target price? "))
        product = input("Product name: ")
        filename = product + ".csv"
        to_address = input("Email to get notification: ")
    
    while True: 
        price = check_price.check_price(url=url, filename=filename)
        if price <= target_price:
            send_mail.send_mail(price=price, to_address=to_address, product=product, target_price=target_price, url=url)
            break
        else:
            time.sleep(60) # sleep for 60 seconds


if __name__ == "__main__":
    track_price()
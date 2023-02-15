<h2 align= 'center' style = 'font-size:72px'>Web Scraping with Python</h2>


Python web scraping is a technique used for gathering data from web pages. This does the typical task of exploring and downloading the pages or grabbing content, and store in a specific data format.

I have demostrated in this notebook how to scrape [Amazon](Amazon_scraper.ipynb) and [Wikipedia](Wikipedia_scraper.ipynb) websites, stored output as csv format being the widely used format, and send notification to user when certain criteria are met.

## Price Tracker
Amazon scraping script that scrapes Amazon at intervals and sends noification to the email provided when the price the item being tracked is equal to or below the specified price.

## Functions in the script

- check_price:
  takes in two parameters, a filename and a URL, and scrapes the price and title of a product from the specified URL. It then saves the title, price, current date, and time in a CSV file with the specified filename in a subdirectory called 'output'. If the file does not exist, it creates a new file with a header row and writes the data. If the file already exists, it appends the data to the existing file. Finally, the function returns the price as a floating-point number.


- send_mail:
   sends an email notification when the price of a product hits below a certain level. The function takes in five parameters: the recipient email address (to_address), the current price of the product (price), the name of the product (product), the target price (target_price), and the URL of the product (url).
   Note that this code assumes that the sender has set up a Gmail account and provided the correct credentials and that the recipient's email server does not block the email as spam.

- track_price:
   tracks the price of a product on Amazon, and sends a notification email to the user when the price of the product falls below a certain level. The code first imports the time module, and two functions from external Python files: check_price() and send_mail(). The check_price() function checks the price of the product on Amazon and writes the product information (title, price, date, and time) to a CSV file, while the send_mail() function sends an email notification to the user. The code then sets the url, target_price, product, and to_address variables, which are used by the track_price() function. The track_price() function asks the user if they want to use test data or input their own data, and then repeatedly calls the check_price() function every sleep seconds to track the product's price. If the price falls below the target_price, the send_mail() function is called to send a notification email to the user.

## `run.py `
This code runs the track_price function, which tracks the price of a product on Amazon and sends an email notification if the price drops below a certain target price. The script prompts the user to select between using testing parameters or input the URL of the product, the target price, the name of the product, and the email address to send the notification to, manually. It then runs a loop that repeatedly checks the price of the product and sleeps for a certain amount of time before checking again. If the price drops below the target price, it calls the send_mail function to send an email notification. The if __name__ == "__main__": statement ensures that the track_price function is only run if the script is run as the main module, and not if it is imported into another script.

## How to Clone 
copy code and run in your terminal (while inside the folder for this project)
```
git clone https://github.com/nurudeenabdulsalaam/Web_Scrapers
cd /Web_Scrapers/price_tracker/
python run.py
```

## Others
- Notebooks are also provide to facilitate experimental learning 
  
- Periodic scraping was not used for Wikipedia because it is a static web page.

- Check my [WeRateDogs](https://github.com/nurudeenabdulsalaam/WeRateDogs_twitter_analysis) repository to see Twitter scraping in action
# Scrap google map reviews

Before proceeding,
### Note: As per terms and conditions of google services, they don't recommend you to scrap the data. Please [Terms and Service document](https://cloud.google.com/maps-platform/terms?hl=en) by google.

I scrapped the data for my specific personal use case I wanted to analyse few a place before visiting.
 
## How to use
- Step1 - Clone the repo on your machine, and install necessary libraries
- Step2 - Open https://www.google.com/maps in Google Chrome
- Step3 - Search the place and copy the link from address bar.
- Step4 - Open main.py
- Step5 - Locate website local variable and replace the existing link with your link
- Step6 - Run main.py, and scrapping will start.
- Step7 - You can convert the saved html file pandas dataframe and csv by using MapReviewProcessor class in review_process.py module

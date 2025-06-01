from helper.review_processor import MapReviewProcessor
from helper.web_page_constants import review_sec_constants

"""
This file processes the html and extract reviews and convert them to csv file
"""
review_html_file_path = 'Reviews for Phoenix Mall of the Millennium.html'
with open(review_html_file_path,'r', encoding='utf-8') as f:
    html_file = f.read()

# make review extractor object
reviews = MapReviewProcessor(html_file)

# convert html to dictionary by using the webpage constants
reviews.transform(constants=review_sec_constants)

# dictionary can be accessed with below attribute
# print(reviews.output_data)

# save the extracted data as csv
save_name = 'Pheonix_Millenium_Reviews.csv'
reviews.save_as_csv(save_name)
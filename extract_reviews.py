from helper.review_processor import MapReviewProcessor
from helper.web_page_constants import review_sec_constants


review_html_file_path = 'Reviews for Phoenix Mall of the Millennium.html'
with open(review_html_file_path,'r', encoding='utf-8') as f:
    html_file = f.read()

reviews = MapReviewProcessor(html_file)

reviews.transform(constants=review_sec_constants)

reviews.save_as_csv('Pheonix_Millenium_Reviews.html')
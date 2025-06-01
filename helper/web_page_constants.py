
page_constants = {
    "web_address" : "https://www.google.com/maps/place/",
    "review_button_section" : "hh2c6",
    "review_button" : "hh2c6 G7m0A",
    "review_scroll_section_class_name" : "m6QErb DxyBCb kA9KIf dS8AEf XiKgde",
    "individual_reviews": "jJc9Ad",
    "more_button" : "w8nwRe kyuRq",
    "review_html_body_class_name" : "m6QErb XiKgde",
    "review_elem_class_name": "jftiEf fontBodyMedium"
}

review_sec_constants = {
    "review_class": {
        "class":"jJc9Ad", "tag": 'div',
            "outer": {
                    "name_of_reviewer": {"class":"d4r55", "tag": 'div', "info_method":"text"},  # div
                    "reviewer_info": {"class": "RfnDt", "tag": 'div', "info_method":"text"},  # div how many reviews he has given
                    #"star_info_class": {"class": "DU9Pgb", "tag": 'div', "info_method":"text"},  # div
                    "stars": {"class": "kvMYJc", "tag": 'span', "info_method":"aria-label"},  # span, star info available in aria-label
                    "when_reviewed": {"class": "rsqaWe", "tag": 'span', "info_method":"text"},  # span
                    "review_text": {"class": "wiI7pd", "tag": 'span', "info_method":"text"},  # span
                    #"review_likes": {"class": "znYl0", "tag": 'span', "info_method":"text"},  # span
                    "review_like_count": {"class": "pkWtMe", "tag": 'span', "info_method":"text"},  # span, may need to check availability
                    },
            "nested": {
                "response_section": {
                    "class": "CDe7pd", "tag": 'div', "outer" : {
                                                "response_by": {"class": "nM6d2c", "tag": 'span', "info_method":"text"}, # span
                                                "when_responded": {"class": "DZSIDd", "tag": 'span', "info_method":"text"}, # span
                                                "what_response": {"class": "wiI7pd", "tag": 'div', "info_method":"text"},# div
                                                }
                                    }
                    }
                }

            }

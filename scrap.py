# import necessary libraries
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from helper.process_run_time_html import PageData, save_html_file
from helper.web_page_constants import page_constants

# ------------------------------Enter valid map link------------------------------------
# website = "https://www.google.com/maps/place/Dr.+Suraaj+Clinic+%E2%80%93+MD+Physician+%2F+clinic+and+wellness+center/@18.5962763,73.7703322,17z/data=!4m16!1m9!3m8!1s0x3bc2b9255067bb77:0x688a9d8672961266!2sDr.+Suraaj+Clinic+%E2%80%93+MD+Physician+%2F+clinic+and+wellness+center!8m2!3d18.5962712!4d73.7729071!9m1!1b1!16s%2Fg%2F11g9vvhgxy!3m5!1s0x3bc2b9255067bb77:0x688a9d8672961266!8m2!3d18.5962712!4d73.7729071!16s%2Fg%2F11g9vvhgxy?entry=ttu&g_ep=EgoyMDI1MDUyNi4wIKXMDSoJLDEwMjExNDU1SAFQAw%3D%3D"
website = "https://www.google.com/maps/place/Phoenix+Mall+of+the+Millennium/@18.6006257,73.7540085,17z/data=!3m1!4b1!4m6!3m5!1s0x3bc2b9dc4ce5ac9f:0x7fdeb0087efc3a7f!8m2!3d18.6006206!4d73.7565834!16s%2Fg%2F11flgdmx7v?entry=ttu&g_ep=EgoyMDI1MDUyNy4wIKXMDSoASAFQAw%3D%3D"

# this name will update_automatically to place name
save_file_name_html = "default_file_name"
# start chrome browser
driver = webdriver.Chrome()

# Navigate through link
driver.get(website)
# let the website load completely
time.sleep(4)

# load and save reviews
page_data = PageData()
html = driver.page_source

# read loaded page and check for availability of assumed constants
review_sec_button = page_data.get_review_button_section(html)

if review_sec_button is not None:
    review_button_click_status = False
    for button in review_sec_button:
        aria_label = driver.find_element(By.XPATH, button).get_attribute('aria-label')
        print(aria_label)
        if str(aria_label).startswith("Reviews"):
            save_file_name_html = str(aria_label).replace('/','').replace('\'', '')
            driver.find_element(By.XPATH, button).click()
            time.sleep(2)
            review_button_click_status = True
            break
    else:
        print("Cant find review button, checking if review page is directly available")
        xpaths = page_data.get_xpath_of_class(driver.page_source,
                                              class_name=page_constants['review_scroll_section_class_name'])
        if len(xpaths) == 0:
            print("Can't find review scroll section either!!!")
            driver.close()
            exit()

    time.sleep(2)

    xpaths = page_data.get_xpath_of_class(driver.page_source,
                                          class_name=page_constants['review_elem_class_name'])

    scroll_section_xpath = page_data.get_xpath_of_class(driver.page_source,
                                          class_name=page_constants['review_scroll_section_class_name'])
    scroll_element = None
    if len(scroll_section_xpath) != 0:
        scroll_element = driver.find_element(By.XPATH, scroll_section_xpath[0])
        scroll_base_height = driver.execute_script('return arguments[0].scrollHeight', scroll_element)
    retry_count = 0
    retry_threshold = 5
    if len(xpaths) != 0:

        next_idx = 0
        while True:
            review_xpaths = page_data.get_xpath_of_class(driver.page_source,
                                                         class_name=page_constants['review_elem_class_name'])
            if len(review_xpaths) == next_idx:
                # may be we are scrolling too fast
                while retry_count != retry_threshold:
                    # Try to scroll to the bottom
                    scrollable_page_height = driver.execute_script('return arguments[0].scrollHeight', scroll_element)
                    for i in range(scrollable_page_height-scroll_base_height, scrollable_page_height,20):
                        driver.execute_script(f'arguments[0].scrollTo(0,{i})', scroll_element)
                        # time.sleep(0.1)
                    time.sleep(4)
                    review_xpaths = page_data.get_xpath_of_class(driver.page_source,
                                                                 class_name=page_constants['review_elem_class_name'])
                    if len(review_xpaths) != next_idx:
                        retry_count = 0
                        break

                    # spend some time with data so browser get its time
                    for i in range(1,11):
                        elem = driver.find_element(By.XPATH, review_xpaths[-i])
                        driver.execute_script('arguments[0].scrollIntoView(true)', elem)
                        time.sleep(0.1)
                    review_xpaths = page_data.get_xpath_of_class(driver.page_source,
                                                                 class_name=page_constants['review_elem_class_name'])
                    if len(review_xpaths) != next_idx:
                        retry_count = 0
                        break
                    for i in range(11, 0, -1):
                        elem = driver.find_element(By.XPATH, review_xpaths[-i])
                        driver.execute_script('arguments[0].scrollIntoView(true)', elem)
                        time.sleep(0.1)
                    review_xpaths = page_data.get_xpath_of_class(driver.page_source,
                                                                 class_name=page_constants['review_elem_class_name'])
                    if len(review_xpaths) != next_idx:
                        retry_count = 0
                        break

                    retry_count += 1
                else:
                    # max retry limit reached
                    # time.sleep(200)
                    print("max retry limit reached","total review recorded: ", next_idx)
                    break
            for path in review_xpaths[next_idx:]:
                elem = driver.find_element(By.XPATH, path)
                driver.execute_script('arguments[0].scrollIntoView(true)', elem)
                try:
                    buttons = elem.find_elements(By.TAG_NAME, 'button')
                    for button in buttons:
                        if button.text == 'More' or button.text == 'See more':
                            button.click()
                            time.sleep(0.1)
                            break
                except:
                    pass
                time.sleep(0.1)
                next_idx += 1
            html = driver.page_source
            save_html_file(html, save_file_name_html)
            time.sleep(4)

        html = driver.page_source
        save_html_file(html, save_file_name_html)
        print("Total review captured: ",next_idx)
        # safely close the browser and exit the software
        driver.close()
        exit()

    else:
        print("Can't find review scroll section, cross check the class name.")
else:
    print("Can't find review button section with standard methods!")





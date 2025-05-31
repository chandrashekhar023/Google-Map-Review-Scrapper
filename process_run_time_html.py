from bs4 import BeautifulSoup
from lxml import html
from web_page_constants import page_constants
import os


class PageData:

    def get_xpath_of_class(self, html_page, class_name=page_constants['review_scroll_section_class_name'], index=0):
        """
        :param html_page: Provide entire html page. eg driver.page_source
        :param class_name: class name of html section
        :param index: default value is 0, modify this if more than 1 xpaths are to be expected under class name
        :return: returns full xpath of given class name
        """
        soup = BeautifulSoup(html_page,'lxml')
        xml_tree = html.fromstring(str(soup))
        elements = xml_tree.find_class(class_name)

        return [xml_tree.getroottree().getpath(path) for path in elements]

    def get_review_button_section(self, html_page):
        """
        Finds the xpath of review button stored in constants
        :param html_page:
        :return: xpath of element
        """
        soup = BeautifulSoup(html_page, 'lxml')
        xml_tree = html.fromstring(str(soup))
        review_button_section_xpath = xml_tree.find_class(page_constants['review_button_section'])
        xpaths = []
        for path in review_button_section_xpath:
            xpaths.append(xml_tree.getroottree().getpath(path))
        if len(xpaths) != 0:
            return xpaths
        else:
            return None


def save_html_file(html_page, file_name : str, path:os.path = None):
    if path is not None:
        if os.path.exists(path):
            if file_name.endswith('.html'):
                file_name = os.path.join(path, file_name)
            else:
                file_name += '.html'
                file_name = os.path.join(path, file_name)

        assert "Invalid save path, path does not exist"

    if not file_name.endswith('.html'):
        file_name += '.html'

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(html_page)


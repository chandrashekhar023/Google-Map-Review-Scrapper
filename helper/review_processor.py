from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from tqdm import tqdm

class MapReviewProcessor:

    def __init__(self, html_page=None):
        if html_page is not None:
            self.main_page_soup = BeautifulSoup(html_page, 'lxml')
        self.output_data = {}

    def transform(self, constants: dict):
        for sec in constants.keys():
            self.output_data[sec] = {}
            sec_soup_list = self.main_page_soup.find_all(constants[sec]['tag'], constants[sec]['class'])
            for idx, soup in enumerate(tqdm(sec_soup_list,postfix="Reviews")):
                for sub_sec in constants[sec].keys():
                    if sub_sec == "outer":
                        for key in constants[sec][sub_sec].keys():
                            if key not in self.output_data[sec].keys():
                                self.output_data[sec][key] = []
                            if constants[sec][sub_sec][key]['info_method'] == 'text':
                                data_soup = soup.find(constants[sec][sub_sec][key]['tag'], constants[sec][sub_sec][key]['class'])
                                if data_soup is not None:
                                    self.output_data[sec][key].append(data_soup.text)
                                else:
                                    self.output_data[sec][key].append(np.nan)
                            elif constants[sec][sub_sec][key]['info_method'] == 'aria-label':
                                data_soup = soup.find(constants[sec][sub_sec][key]['tag'], constants[sec][sub_sec][key]['class'])
                                if data_soup is not None:
                                    self.output_data[sec][key].append(data_soup.get('aria-label'))
                                else:
                                    self.output_data[sec][key].append(np.nan)

                    elif sub_sec == 'nested':
                        for nested in constants[sec][sub_sec].keys():
                            sub_soup = soup.find(constants[sec][sub_sec][nested]['tag'], constants[sec][sub_sec][nested]['class'])
                            if sub_soup is not None:
                                for nested_sub_sec in constants[sec][sub_sec][nested]:
                                    if nested_sub_sec == "outer":
                                        for key in constants[sec][sub_sec][nested][nested_sub_sec].keys():
                                            if key not in self.output_data[sec].keys():
                                                self.output_data[sec][key] = []
                                            if constants[sec][sub_sec][nested][nested_sub_sec][key]['info_method'] == 'text':
                                                data_soup = sub_soup.find(constants[sec][sub_sec][nested][nested_sub_sec][key]['tag'],
                                                                      constants[sec][sub_sec][nested][nested_sub_sec][key]['class'])
                                                if data_soup is not None:
                                                    self.output_data[sec][key].append(data_soup.text)
                                                else:
                                                    self.output_data[sec][key].append(np.nan)
                                            elif constants[sec][sub_sec][nested][nested_sub_sec][key]['info_method'] == 'aria-label':
                                                data_soup = sub_soup.find(constants[sec][sub_sec][nested][nested_sub_sec][key]['tag'],
                                                                      constants[sec][sub_sec][nested][nested_sub_sec][key]['class'])
                                                if data_soup is not None:
                                                    self.output_data[sec][key].append(data_soup.get('aria-label'))
                                                else:
                                                    self.output_data[sec][key].append(np.nan)
                            else:
                                for nested_sub_sec in constants[sec][sub_sec][nested]:
                                    if nested_sub_sec == "outer":
                                        for key in constants[sec][sub_sec][nested][nested_sub_sec].keys():
                                            if key not in self.output_data[sec].keys():
                                                self.output_data[sec][key] = []
                                            self.output_data[sec][key].append(np.nan)

    def elem_to_dict(self, html, constants: dict):
        self.main_page_soup = BeautifulSoup(html, 'lxml')
        for sec in constants.keys():
            if sec not in self.output_data.keys():
                self.output_data[sec] = {}
            soup = self.main_page_soup.find(constants[sec]['tag'], constants[sec]['class'])
            for sub_sec in constants[sec].keys():
                if sub_sec == "outer":
                    for key in constants[sec][sub_sec].keys():
                        if key not in self.output_data[sec].keys():
                            self.output_data[sec][key] = []
                        if constants[sec][sub_sec][key]['info_method'] == 'text':
                            data_soup = soup.find(constants[sec][sub_sec][key]['tag'],
                                                  constants[sec][sub_sec][key]['class'])
                            if data_soup is not None:
                                self.output_data[sec][key].append(data_soup.text)
                            else:
                                self.output_data[sec][key].append(np.nan)
                        elif constants[sec][sub_sec][key]['info_method'] == 'aria-label':
                            data_soup = soup.find(constants[sec][sub_sec][key]['tag'],
                                                  constants[sec][sub_sec][key]['class'])
                            if data_soup is not None:
                                self.output_data[sec][key].append(data_soup.get('aria-label'))
                            else:
                                self.output_data[sec][key].append(np.nan)

                elif sub_sec == 'nested':
                    for nested in constants[sec][sub_sec].keys():
                        sub_soup = soup.find(constants[sec][sub_sec][nested]['tag'],
                                             constants[sec][sub_sec][nested]['class'])
                        if sub_soup is not None:
                            for nested_sub_sec in constants[sec][sub_sec][nested]:
                                if nested_sub_sec == "outer":
                                    for key in constants[sec][sub_sec][nested][nested_sub_sec].keys():
                                        if key not in self.output_data[sec].keys():
                                            self.output_data[sec][key] = []
                                        if constants[sec][sub_sec][nested][nested_sub_sec][key]['info_method'] == 'text':
                                            data_soup = sub_soup.find(
                                                constants[sec][sub_sec][nested][nested_sub_sec][key]['tag'],
                                                constants[sec][sub_sec][nested][nested_sub_sec][key]['class'])
                                            if data_soup is not None:
                                                self.output_data[sec][key].append(data_soup.text)
                                            else:
                                                self.output_data[sec][key].append(np.nan)
                                        elif constants[sec][sub_sec][nested][nested_sub_sec][key][
                                            'info_method'] == 'aria-label':
                                            data_soup = sub_soup.find(
                                                constants[sec][sub_sec][nested][nested_sub_sec][key]['tag'],
                                                constants[sec][sub_sec][nested][nested_sub_sec][key]['class'])
                                            if data_soup is not None:
                                                self.output_data[sec][key].append(data_soup.get('aria-label'))
                                            else:
                                                self.output_data[sec][key].append(np.nan)
                        else:
                            for nested_sub_sec in constants[sec][sub_sec][nested]:
                                if nested_sub_sec == "outer":
                                    for key in constants[sec][sub_sec][nested][nested_sub_sec].keys():
                                        if key not in self.output_data[sec].keys():
                                            self.output_data[sec][key] = []
                                        self.output_data[sec][key].append(np.nan)

    def save_as_csv(self, filename: str):
        if not filename.endswith('.csv'):
            filename += '.csv'
        for idx, sec in enumerate(self.output_data.keys()):
            df = pd.DataFrame(self.output_data[sec])
            if idx == 0:
                df.to_csv(filename, index=False)
            else:
                df.to_csv(str(idx)+filename, index=False)

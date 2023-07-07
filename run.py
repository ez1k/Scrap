import os
import glob
import re
import requests
from bs4 import BeautifulSoup
import json
from classes.EnvVariables import EnvVariables
from classes.Quote import Quote
import codecs
def replace_unicode_escapes(text):
    decoded_text = codecs.decode(text, 'unicode_escape')
    return decoded_text
def remove_unwanted_characters(text):
    unwanted_chars = ["\u00e2\u0080\u009c", "\u00e2\u0080\u009d"]
    cleaned_text = text
    for char in unwanted_chars:
        cleaned_text = cleaned_text.replace(char, "")

    return cleaned_text


desktop_path = os.path.expanduser("~/Desktop")
env_file_path = os.path.join(desktop_path, "*.env")
env_files = glob.glob(env_file_path)

quote_list = []
if env_files:
    env_vars = EnvVariables(env_files[0])
    env_vars.print_values()

    if env_vars.are_defined():
        url = env_vars.input_url
        while True:
            base_url = env_vars.input_url
            response = requests.get(url)
            response.encoding = response.apparent_encoding
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')


            regex = r'var data = ([\s\S]*?)];'
            match = re.search(regex, str(soup))
            extracted_string = ""

            if match and match.group(1):
                extracted_string = match.group(1)
            extracted_string = extracted_string + "]"


            parsed_data = json.loads(extracted_string)
            for quote in parsed_data:
                quote_text = quote['text']
                quote_author = quote['author']['name']
                quote_tags = quote['tags']
                decoded_text = replace_unicode_escapes(quote_text)
                cleaned_text = remove_unwanted_characters(decoded_text)
                quote_obj = Quote(cleaned_text, quote_author, quote_tags)
                quote_list.append(quote_obj)

            next_list_item = soup.find('li', class_='next')
            if next_list_item:
                next_button = next_list_item.find('a')
                next_url = next_button['href']
                next_url = re.findall(r'page/\d+/', next_url)[0]
                next_url = f"{base_url}{next_url}"
                url = next_url
            else:
                break

    quote_dicts = [quote.__dict__ for quote in quote_list]

    for quote_dict in quote_dicts:
        quote_dict['tags'] = '[' + ', '.join(quote_dict['tags']) + ']'

    quote_json = json.dumps(quote_dicts, indent=4)

    with open(env_vars.output_file, 'w') as file:
        file.write(quote_json)
else:
    print("Nie znaleziono pliku .env na pulpicie.")






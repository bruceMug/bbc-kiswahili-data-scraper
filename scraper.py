from bs4 import BeautifulSoup
import requests

base_url = "https://www.bbc.com"


def write_to_file(category, paragraph):
    """ function that opens and writes to a file"""
    with open(f"{category}.txt", 'a', encoding='utf-8') as f:
        f.write(category + ',' + paragraph)
        f.write('\n')


def headline(category_link):
    """ function that captures all the links available for each headline """

    # empty list to store all links
    cat_link = []
    html_text = requests.get(category_link).text
    soup = BeautifulSoup(html_text, 'lxml')

    # this captures all headlines on the first page
    top_story = soup.find_all('li', class_="bbc-t44f9r")
    for story in top_story:
        # print(story.find('a')['href'])
        cat_link.append(story.find('a')['href'])

    return cat_link


def get_kiswahili_paragraphs(headline_link):
    """ function: when a certain headline under a category is clicked on, it returns list containing paragraphs of text
    for a given headline """

    # empty list to store all text
    paragraph_text = []
    response = requests.get(headline_link).text
    soup = BeautifulSoup(response, "html.parser")
    text_content = soup.find_all('div', class_="bbc-19j92fr ebmt73l0")

    for content in text_content:
        kiswahili_text = content.find('p', class_="bbc-1y32vyc e17g058b0")
        # print(kiswahili_text)
        if kiswahili_text is not None:
            # print(kiswahili_text.text)
            paragraph_text.append(kiswahili_text.text)

    return paragraph_text


def main():
    """ all the logic starts from here """

    html_text = requests.get("https://www.bbc.com/swahili").text
    soup = BeautifulSoup(html_text, "lxml")

    # this will store the names of the categories
    category_list = []
    categories = soup.find_all('li', class_="bbc-zakhp8 e11sm0on2")

    for category in categories:
        relative_path = category.find('a')['href']

        # add this logic because I need only four categories ie michezo, makala, afya and bururdani
        if len(relative_path) > 25 and category.text != 'Video':
            category_list.append(category.text)

            print(f'Obtaining Headlines & paragraphs text in the {category.text} >>>>>>>>\n')
            # define full url for a category
            full_url = base_url + str(relative_path)

            headline_links = headline(full_url)
            for link in headline_links:
                paragraphs = get_kiswahili_paragraphs(link)

                for paragraph in paragraphs:
                    # inorder for easy import into csv, all commas in paragraphs are replaced with space
                    write_to_file(category.text, paragraph.replace(",", " "))


if __name__ == '__main__':
    main()
    print('-----done----------')

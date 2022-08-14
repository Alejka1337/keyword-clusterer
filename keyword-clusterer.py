import requests
from bs4 import BeautifulSoup as bs


keyword_1 = input('Введите первое ключевое слово:')
list_worlds1 = keyword_1.lower().split(' ')
right_str1 = '+'.join(list_worlds1)

keyword_2 = input('Введите второе ключевое слово:')
list_worlds2 = keyword_2.lower().split(' ')
right_str2 = '+'.join(list_worlds2)

base_url = 'https://www.google.com/search?q='

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'accept': '*/*',
}

list_one = []
list_two = []


def request_first_page():
    url1 = f'{base_url}{right_str1}'
    r = requests.get(url=url1)
    return r.text


def request_second_page():
    url2 = f'{base_url}{right_str2}'
    r = requests.get(url=url2)
    return r.text


def parse_urls():
    res1 = request_first_page()
    res2 = request_second_page()
    soup1 = bs(res1, 'lxml')
    soup2 = bs(res2, 'lxml')
    pages1 = soup1.find_all('div', class_='egMi0 kCrYT')
    pages2 = soup2.find_all('div', class_='egMi0 kCrYT')

    for page1 in pages1:
        url1 = str(page1.find('a'))
        url1 = url1.split('<a href="/url?q=')
        del url1[0]
        str_url = ''.join(url1)
        url1 = str_url.split('">')
        page_url1 = url1[0]
        list_one.append(page_url1)

    for page2 in pages2:
        url2 = str(page2.find('a'))
        url2 = url2.split('<a href="/url?q=')
        del url2[0]
        str_url = ''.join(url2)
        url2 = str_url.split('">')
        page_url2 = url2[0]
        list_two.append(page_url2)


def get_correct_list1():
    correct_list1 = []
    for i in list_one:
        correct_list1.append(i[0:i.find('&')])
    return correct_list1


def get_correct_list2():
    correct_list2 = []
    for i in list_two:
        correct_list2.append(i[0:i.find('&')])
    return correct_list2


def coincidence():
    list1 = get_correct_list1()
    list2 = get_correct_list2()
    count_coincidence = 0
    url_coincidence = []
    for i in list1:
        for j in list2:
            if i == j:
                url_coincidence.append(j)
                count_coincidence += 1
    return print(count_coincidence, url_coincidence, sep='\n')


def main():
    request_first_page()
    request_second_page()
    parse_urls()
    coincidence()


if __name__ == '__main__':
    main()
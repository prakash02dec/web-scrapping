from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.worldometers.info/world-population/india-population/').text
info = BeautifulSoup(html_text,'lxml')

with open(f'population stats.text','w') as f:
    country_name=info.find('div',id='maincounter-wrap').h1.text.split()[0]
    f.write(f"country name:  {country_name}\n")

    country_detail= info.find('div',class_ ='col-md-8 country-pop-description').text
    f.write(country_detail+'\n')

    population_table=info.find('div',class_='table-responsive')
    country_population_info =population_table.find('table',class_ ='table table-striped table-bordered table-hover table-condensed table-list')
    all_head=country_population_info.find('thead')
    head=all_head.find('tr')
    titles=head.find_all('th')

    f.write("\nPOPULATION HISTORY OF "+country_name+'\n')
    for title in titles:
        f.write(title.text.replace('  ','')+'\t\t\t')

    f.write('\n')

    all_content=country_population_info.find('tbody')
    contents=all_content.find_all('tr')
    for content in contents:
        datas=content.find_all('td')
        for data in datas:
            f.write(data.text.replace('  ','')+'\t\t\t')
        f.write('\n')


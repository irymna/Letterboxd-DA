import requests
from bs4 import BeautifulSoup
import pandas as pd
import asyncio
import httpx


async def scrape_letterboxd(username):
    base_url = f'https://letterboxd.com/{username}/films/page/'
    film_data = []
    page_num = 1

    async with httpx.AsyncClient() as client:
        while True:
            url = base_url + str(page_num) + '/'
            response = await client.get(url, timeout=None)
            soup = BeautifulSoup(response.content, 'lxml')
            film_elements = soup.find_all('div', {'data-film-slug': True})
            if len(film_elements) == 0:
                break

            tasks = []
            for film_element in film_elements:
                film_slug = film_element['data-film-slug']
                film_link = f'https://letterboxd.com{film_slug}'
                tasks.append(extract_film_info(client, film_link))

            film_data += await asyncio.gather(*tasks)

            page_num += 1

    df = pd.DataFrame(film_data)
    return df

async def extract_film_info(client, film_link):
    response = await client.get(film_link, timeout=None)
    soup = BeautifulSoup(response.content, 'lxml')

    title = soup.find('meta', property='og:title')['content']

    director_element = soup.find('meta', {'name': 'twitter:label1', 'content': 'Directed by'})
    director = director_element.find_next_sibling('meta')['content'] if director_element else None

    year_element = soup.find('small', class_='number')
    year = year_element.find('a')['href'].split('/')[-2]

    country_element = soup.find('a', href=lambda href: href and href.startswith('/films/country/'))
    country = country_element.text if country_element else None

    language_element = soup.find('a', href=lambda href: href and href.startswith('/films/language/'))
    language = language_element.text if language_element else None

    genres = [genre.text for genre in soup.select('h3:has(span:contains("Genres")) + div.text-sluglist a.text-slug')]

    cast = [actor.text for actor in soup.select('.cast-list .text-slug.tooltip')]

    return {
        'Title': title,
        'Director': director,
        'Year': year,
        'Country': country,
        'Language': language,
        'Genres': genres,
        'Cast': cast,
        'Film Link': film_link
    }
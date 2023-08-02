import requests
from bs4 import BeautifulSoup
import pandas as pd
import asyncio
import httpx


async def scrape_letterboxd(username, num_pages_per_batch=3):
    base_url = f'https://letterboxd.com/{username}/films/page/'
    film_data = []
    page_num = 1

    async with httpx.AsyncClient() as client:
        while True:
            # Define o intervalo de páginas para coletar nesse lote
            start_page = page_num
            end_page = page_num + num_pages_per_batch - 1

            # Coleta os dados para todas as páginas desse lote
            for page in range(start_page, end_page + 1):
                url = base_url + str(page) + '/'
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

            page_num = end_page + 1

            # Verifica se ainda há mais páginas para coletar
            next_page_url = base_url + str(page_num) + '/'
            next_response = await client.get(next_page_url, timeout=None)
            next_soup = BeautifulSoup(next_response.content, 'lxml')
            next_film_elements = next_soup.find_all('div', {'data-film-slug': True})
            if len(next_film_elements) == 0:
                break

    df = pd.DataFrame(film_data)
    return df

async def extract_film_info(client, film_link):
    response = await client.get(film_link, timeout=None)
    soup = BeautifulSoup(response.content, 'lxml')

    director_element = soup.find('meta', {'name': 'twitter:label1', 'content': 'Directed by'})
    director = director_element.find_next_sibling('meta')['content'] if director_element else None

    country_element = soup.find('a', href=lambda href: href and href.startswith('/films/country/'))
    country = country_element.text if country_element else None

    language_element = soup.find('a', href=lambda href: href and href.startswith('/films/language/'))
    language = language_element.text if language_element else None

    genres = [genre.text for genre in soup.select('h3:has(span:contains("Genres")) + div.text-sluglist a.text-slug')]

    cast = [actor.text for actor in soup.select('.cast-list .text-slug.tooltip')]

    return {
        'Director': director,
        'Country': country,
        'Language': language,
        'Genres': genres,
        'Cast': cast,
        'Film Link': film_link
    }
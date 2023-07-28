from flask import Flask, render_template, request
from scraping import scrape_letterboxd
from analysis import perform_analysis
import asyncio

app = Flask(__name__)

@app.route('/')
def index():
    error_message = request.args.get('error_message')
    return render_template('index.html', error_message=error_message)

@app.route('/result', methods=['POST'])
async def result():
    username = request.form['username']
    try:
        df = await scrape_letterboxd(username)
        (
            genre_counts, year_counts, director_counts, actor_counts,
            genre_plot, year_plot, director_plot, actor_plot,
            country_counts, language_counts, country_plot, language_plot
        ) = await perform_analysis(df)

        return render_template('result.html', username=username,
                               genre_counts=genre_counts, year_counts=year_counts,
                               director_counts=director_counts, actor_counts=actor_counts,
                               genre_plot=genre_plot, year_plot=year_plot,
                               director_plot=director_plot, actor_plot=actor_plot,
                               country_counts=country_counts, language_counts=language_counts,
                               country_plot=country_plot, language_plot=language_plot)
    except:
        error_message = "Invalid username. Please enter a valid Letterboxd username and try again."
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.run())
import plotly.graph_objs as go
import plotly.io as pio

async def perform_analysis(df):
    # Gêneros mais assistidos
    genre_counts = df['Genres'].explode().value_counts().head(10)
    genre_counts = genre_counts.iloc[::-1]

    # Configuração do estilo de plotagem
    pio.templates.default = "plotly_white"

    # Gráfico de barras dos gêneros mais assistidos
    genre_bar = go.Bar(
        x=genre_counts,
        y=genre_counts.index,
        orientation='h',
        marker_color='rgba(31, 119, 180, 0.7)'
    )

    genre_fig = go.Figure(data=[genre_bar])

    genre_plot = genre_fig.to_html(full_html=False)

    # Mais assistido por diretor
    director_counts = df['Director'].value_counts().head(10)
    director_counts = director_counts.iloc[::-1]

    director_bar = go.Bar(
        x=director_counts,
        y=director_counts.index,
        orientation='h',
        marker_color='rgba(31, 119, 180, 0.7)'
    )

    director_fig = go.Figure(data=[director_bar])

    director_plot = director_fig.to_html(full_html=False)

    # Mais assistido por ator
    actor_counts = df['Cast'].explode().value_counts().head(10)
    actor_counts = actor_counts.iloc[::-1]

    actor_bar = go.Bar(
        x=actor_counts,
        y=actor_counts.index,
        orientation='h',
        marker_color='rgba(31, 119, 180, 0.7)'
    )

    actor_fig = go.Figure(data=[actor_bar])

    actor_plot = actor_fig.to_html(full_html=False)

    # Mais assistido por país
    country_counts = df['Country'].value_counts().head(10)
    country_counts = country_counts.iloc[::-1]

    country_bar = go.Bar(
        x=country_counts,
        y=country_counts.index,
        orientation='h',
        marker_color='rgba(31, 119, 180, 0.7)'
    )

    country_fig = go.Figure(data=[country_bar])

    country_plot = country_fig.to_html(full_html=False)

    # Mais assistido por linguagem
    language_counts = df['Language'].value_counts().head(10)
    language_counts = language_counts.iloc[::-1]

    language_bar = go.Bar(
        x=language_counts,
        y=language_counts.index,
        orientation='h',
        marker_color='rgba(31, 119, 180, 0.7)'
    )

    language_fig = go.Figure(data=[language_bar])

    language_plot = language_fig.to_html(full_html=False)

    # Return all the analysis results including the new ones
    return (
        genre_counts, director_counts, actor_counts,
        genre_plot, director_plot, actor_plot,
        country_counts, language_counts, country_plot, language_plot
    )


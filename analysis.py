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

    # Ano mais assistido
    year_counts = df['Year'].value_counts().head(10)
    year_counts = year_counts.iloc[::-1]

    year_bar = go.Bar(
        x=year_counts,
        y=year_counts.index,
        orientation='h',
        marker_color='rgba(31, 119, 180, 0.7)'
    )

    year_fig = go.Figure(data=[year_bar])

    year_plot = year_fig.to_html(full_html=False)

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

    return (
        genre_counts, year_counts, director_counts, actor_counts,
        genre_plot, year_plot, director_plot, actor_plot
    )

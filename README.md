# Letterboxd Data Analysis

O código é uma aplicação web que realiza a análise de dados de filmes do serviço Letterboxd. O usuário insere um nome de usuário do Letterboxd, e a aplicação coleta informações sobre os filmes assistidos pelo usuário, incluindo gêneros mais assistidos, ano de lançamento mais frequente, diretores mais vistos e atores/atrizes mais populares.

Resumo do funcionamento da aplicação:

1. O usuário acessa o site e insere um nome de usuário do Letterboxd.
2. A aplicação realiza o scraping (coleta de dados) dos filmes associados ao usuário no Letterboxd.
3. As informações coletadas são processadas para gerar estatísticas e gráficos.
4. A aplicação exibe os resultados da análise em uma página separada com gráficos interativos.
   
Funcionalidades adicionais:
Caso o usuário insira um nome de usuário inválido, a aplicação exibirá uma mensagem de erro solicitando que ele insira um nome de usuário válido.
A aplicação usa a biblioteca Flask para criar o servidor web e Plotly para gerar os gráficos interativos.
Aviso:
A aplicação está em sua versão beta, e o processo de coleta de dados pode levar um tempo dependendo da quantidade de filmes no perfil do usuário. O projeto pode ser expandido no futuro para adicionar mais funcionalidades e otimizar a coleta de dados.

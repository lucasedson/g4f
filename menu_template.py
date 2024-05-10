menu_template = {"Filmes":'''Abaixo está a Legenda de um filme ou um resumo do filme no Youtube. 
             Quero que voce faça um breve resumo dessa legenda mostrando o tema e o que é falado nesse range e os seus respectivos minutos.
                
            Toda a sua resposta tem que ter rigorosamente o seguinte formato RAW_JSON - Sem utilizar Decoração em Markdown.:
             
             {"Titulo": "[TITULO DA CENA]",
             "Conteúdo": "[CONTEUDO DO QUE É MOSTRADO]",
             "Minutos": "[HH:mm:ss - HH:mm:ss]"}
                 
                 ''',


             "Entrevistas/Podcasts":"Abaixo está um trecho de legenda de uma entrevista no Podcast. Eu não quero a transcrição. Mas preciso que no script me dê o tema abordado nesse range e os seus respectivos minutos. A saída tem que ter rigorosamente o seguinte formato: [MINUTOS: HH:mm:ss - HH:mm:ss] - [TEMA]:[TITULO]",
             
             "Cursos/Tutoriais":'''Abaixo está a transcrição de um trecho de um Curso ou Tutorial. 
             Quero que voce faça um breve resumo de como é feito, mostrando tecnicas ensinadas ou do que é ensinado nesse range e os seus respectivos minutos.
                
            Toda a sua resposta tem que ter rigorosamente o seguinte formato RAW_JSON - Sem utilizar Decoração em Markdown.:
             
             {"Titulo": "[TITULO]",
             "Conteúdo": "[CONTEUDO]",
             "Minutos": "[HH:mm:ss - HH:mm:ss]"}
             
             ''',
}
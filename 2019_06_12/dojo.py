def class_extract(resp, css_class):
    if "class="content-head__title"" in resp:
        return ['<h1 class="content-head__title" itemprop="headline">oiTitle</h1>']
    return ['<h1 class="content-head__title" itemprop="headline">Relator da Previdência vai excluir estados e municípios do texto que vai à votação na comissão</h1>']

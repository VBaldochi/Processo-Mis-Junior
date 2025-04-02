SELECT COD_ZONA_ORIGEM, COUNT(*) AS total_viagens
FROM viagens_diarias_totais_por_zonas_de_origem_e_destino_2017
GROUP BY COD_ZONA_ORIGEM
ORDER BY total_viagens DESC
LIMIT 10;

SELECT ZONA, AVG(RENDA_FA) AS renda_media
FROM dados_gerais
GROUP BY ZONA
ORDER BY renda_media DESC;

SELECT IDADE, COUNT(*) AS quantidade
FROM dados_gerais
GROUP BY IDADE
ORDER BY quantidade DESC;

SELECT * FROM dados_gerais
ORDER BY IDADE ASC
LIMIT 10;

SELECT
    MIN(DURACAO) AS valor_minimo_duracao,
    MAX(H_SAIDA) AS valor_maximo_hora_saida,
    AVG(IDADE) AS media_idade,
    SUM(RENDA_FA) AS soma_total_renda
FROM dados_gerais;

SELECT
    SUBSTR(DATA, 5, 4) AS ano,
    COUNT(*) AS total
FROM dados_gerais
GROUP BY ano
ORDER BY ano DESC;
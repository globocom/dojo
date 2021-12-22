## Problema

Temos um mapa `string -> int` guardado em memória.

eg:
```
"metric1": 1
"metric2": 3
"metric3": 3
"metric4": 4
```

## Objetivo

Implementar a função `ParseMetrics`. Esta recebe dois argumentos:
- endereço de memória do mapa `inMemory`
- um novo mapa que vem de um servidor remoto

O Objetivo é alterar o mapa `inMemory`, para refletir os dados do `remoteMap`.
Temos que fazer tudo in-place, sem substituir o objeto original.

No final, o conteúdo do `inMemory` precisa ser igual ao conteúdo do `remoteMap`.

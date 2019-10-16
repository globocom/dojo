Repositório que armazena os Dojos acontecidos na Globo.com

INICIO: 08/02/2011

## Gerando um subprojeto dojo

Linguagens:

- go
- python
- java
- javascript

### Comandos para gerar um subprojeto dojo

Irá gerar uma pasta com a data atual com um projeto dentro para realizar TDD

- `make dojo-python`
- `make dojo-go`
- `make dojo-java`
- `make dojo-js`

**Exemplo**

```console
dojo@master:~$ make dojo-python
bash generate.sh "python"

Language selected: python
Creating directory...
Copying files to the directory ./2020_01_01 ...

Boilerplate successfully created: 2020_01_01

   _       ___ ______ __  _____     ___    ___   ____  ___       __
  | |     /  _|      |  |/ ___/    |   \  /   \ |    |/   \     |  |
  | |    /  [_|      |_ (   \_     |    \|     ||__  |     |    |  |
  | |___|    _|_|  |_| \|\__  |    |  D  |  O  |__|  |  O  |    |__|
  |     |   [_  |  |     /  \ |    |     |     /  |  |     |     __
  |     |     | |  |     \    |    |     |     \  `  |     |    |  |
  |_____|_____| |__|      \___|    |_____|\___/ \____j\___/     |__|


```

## License

Dojo is licensed under the [MIT license](LICENSE).
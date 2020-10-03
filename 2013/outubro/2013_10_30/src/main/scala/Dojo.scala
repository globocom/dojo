case class Musica(nome: String, artista: String, duracao: String)

case class Album(nome: String, override val musicas: List[Musica])
		extends Playlist(musicas) {
	def artista: String = {
		val artistas = musicas.map(_.artista)
		val distinctArtistas = artistas.distinct
		if (distinctArtistas.length > 1)
			return "Various artists"
		else
			return artistas.head
	}
}

class Playlist(val musicas: List[Musica])

case class Jukebox(playlist: Playlist) {
	def play = "Tocando %s".format(playlist.musicas.head.nome)
}
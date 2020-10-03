import org.specs2.mutable._

class DojoSpec extends Specification {
	"Musica" should {

		"possui nome" in {
			val musica = Musica("Sanitarium", "", "")

			musica.nome === "Sanitarium"
		}

		"possui artista" in {
			val musica = Musica("Sanitarium", "Metallica", "")

			musica.artista === "Metallica"
		}

		"possui duracao" in {
			val musica = Musica("Sanitarium", "Metallica", "4:23")

			musica.duracao === "4:23"
		}
	} 

	"Jukebox" should {
		"toca musica" in {
			val musicas = List(Musica("Time", "Pink Floyd", "3:47"), Musica("Money", "Pink Floyd", "2:35"))
			val album = Album("Dark Side of the Moon", musicas)
			val jukebox = Jukebox(album)

			jukebox.play === "Tocando Time"
		}
	}


	"Album" should {
		"possui nome" in {
			val musicas = List(Musica("Time", "Pink Floyd", "3:47"), Musica("Money", "Pink Floyd", "2:35"))
			val album = Album("Dark Side of the Moon", musicas)
			album.nome === "Dark Side of the Moon"
		}

		"possui artista" in {
			val musicas = List(Musica("Time", "Pink Floyd", "3:47"), Musica("Money", "Pink Floyd", "2:35"))
			val album = Album("Dark Side of the Moon", musicas)
			album.artista === "Pink Floyd"
		}

		"possui musicas" in {
			val musicas = List(Musica("Time", "Pink Floyd", "3:47"), Musica("Money", "Pink Floyd", "2:35"))
			val album = Album("Dark Side of the Moon", musicas)
			album.musicas === musicas
		}


		"possui multiplos artistas" in {
			val musicas = List(Musica("Time", "Pink Floyd", "3:47"), Musica("Flight of Icarus", "Iron Maiden", "2:35"))
			val album = Album("Dark Side of the Moon", musicas)
			album.artista === "Various artists"
		}
	}
}
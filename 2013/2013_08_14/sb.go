package sb

type Barbearia struct {
	barbeiro chan string
	fila     chan string
}

func (b *Barbearia) Entrar(cliente string) string {
	select {
	case b.barbeiro <- cliente:
		return cliente + " está sendo atendido."
	default:
		select {
		case b.fila <- cliente:
			return cliente + " está esperando."
		default:
			return cliente + " desistiu."
		}
	}
}

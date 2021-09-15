class Hannoy {

    constructor(size){
        this.size = size;
        this.towers = {0: [], 1:[], 2:[]};
        for (var i=0; i<size; i++){
            this.towers[0].push(size-i);
        }
    }

    move(origem, destino) {
        this.towers[destino].push(this.towers[origem].pop());
        console.log(":::::DEBUG::::")
        this.printMe()
    } 

    move3(origem, intermedio, destino) {
        this.move(origem, destino)
        this.move(origem, intermedio)
        this.move(destino, intermedio)
        this.move(origem, destino)
        this.move(intermedio, origem)
        this.move(intermedio, destino)
        this.move(origem, destino)
        // console.log(":::::DEBUG::::")
        // this.printMe()
    } 

    moveN(origem, intermedio, destino, nivel) {
        if (nivel === 3)
            this.move3(origem, intermedio, destino);
        else {
            this.moveN(origem, destino, intermedio, nivel - 1);
            this.move(origem, destino);
            this.moveN(intermedio, origem, destino, nivel - 1);
        }
    }

    solve() {
        h.moveN(0, 1, 2, this.size);
    }

    printMe() {
        console.log('Towers:');
        console.log(this.towers[0]);
        console.log(this.towers[1]);
        console.log(this.towers[2]);
    }
}

var h = new Hannoy(6);
h.printMe();
h.solve();
h.printMe();

// Construtor aceita quantas peças tem DONE
// três pilhas DONE
// método de mover => pilha de origem e de destino DONE
// método de movertop3 => pilha de origem e de destino DONE
// printMe => estado da torre DONE

// tres peças (destino pilha 3)=> segue a ordem dos 7 moviementos

// quatro peças (destino pilha 3) => 
//    tres primeira pro pilha 2 (seguindo os 7 movimentos), 
//    passa a quarta peça pra pilha 3 
//    e depois move as tres outras pra pilha 3 seguindo os 7 movimentos

// cinco peças (destino pilha 3) => 
//    aplica movimento de 4 peças com destino sendo pilha 2
//    move a quinta peça pra pilha 3
//    aplica movimento de 4 peças com destino sendo pilha 3

// Ordem:
// tcarreira
// nicolassantos
// ingridpacheco
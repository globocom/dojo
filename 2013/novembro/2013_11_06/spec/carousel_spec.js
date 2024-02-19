describe("Carousel", function() {
  var carousel, elemento;

  beforeEach(function() {
    elemento = $('<div id="container">' +
      '<ul class="carousel">' +
        '<li><h2>item 1</h2></li>' +
        '<li><h2>item 2</h2></li>'+
        '<li><h2>item 3</h2></li>'+
        '<li><h2>item 4</h2></li>'+
        '<li><h2>item 5</h2></li>'+
      '</ul>'+
      '<a href="#" class="arrow arrow-left"></a>'+
      '<a href="#" class="arrow arrow-right"></a>'+
    '</div>'
      );

    carousel = new Carousel(elemento);
  });

  describe("inicializa o carousel", function() {

    it("armazena um elemento", function() {
      expect(carousel.elemento).toEqual(elemento);
    });

    it("deveria troca o atual pelo próximo item", function() {
      expect(carousel.itemAtual().text()).toBe("item 1");
      $(".arrow-right", elemento).click();
      expect(carousel.itemAtual().text()).toBe("item 2");
    });
  });

  describe("numeroItens", function() {
    it("retorna o numero de itens", function() {
      expect(carousel.numeroItens()).toEqual(5);
    });
  });

  describe("itemAtual", function () {
    it("retorna o item atual", function(){
      expect(carousel.itemAtual().text()).toBe("item 1");
    });
  });

  describe("proximoItem", function () {
    it("retorna o proximo item quando existe", function(){
      carousel.proximoItem();
      expect(carousel.itemAtual().text()).toBe("item 2");
    });

    it("retorna o primeiro item", function () {
      carousel.proximoItem();
      carousel.proximoItem();
      carousel.proximoItem();
      carousel.proximoItem();
      carousel.proximoItem();
      expect(carousel.itemAtual().text()).toBe("item 1");
    });
  });

  describe("itemAnterior", function() {
    it("retorna o ultimo item quando o atual e o primeiro", function() {
      carousel.itemAnterior();
      expect(carousel.itemAtual().text()).toBe("item 5");
    });

    it("retorna o item anterior do item atual", function() {
      expect(carousel.itemAtual().text()).toBe("item 1");
      carousel.itemAnterior();
      carousel.itemAnterior();
      expect(carousel.itemAtual().text()).toBe("item 4");
    });
  });
});
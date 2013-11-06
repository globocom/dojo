function Carousel(elemento) {
  this.elemento = elemento;
  this.$elemento = $(elemento);
  this.init();
}

Carousel.prototype = {
  init: function() {
    this._primeiroItem().addClass("atual");
  },

  numeroItens: function() {
    return this.$elemento.find(".carousel li").length;
  },

  itemAtual: function() {
    return this.$elemento.find(".atual");
  },

  proximoItem: function() {
    var $proximoitem = this.itemAtual().removeClass("atual").next();

    if(!$proximoitem.length){
      $proximoitem = this._primeiroItem();
    }

    $proximoitem.addClass("atual");
  },

  _primeiroItem: function () {
    return this.$elemento.find(".carousel > li:first");
  }
}
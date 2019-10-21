function Carousel(elemento) {
  this.elemento = elemento;
  this.$elemento = $(elemento);
  this.init();
}

Carousel.prototype = {
  init: function() {
    this._primeiroItem().addClass("atual");
    this.bindEvents();
  },

  bindEvents: function(){
    var self = this;
    this.$elemento.find(".arrow-right").on('click', function(event){
      self.proximoItem();
    });
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

  itemAnterior: function() {
    var $itemAnterior = this.itemAtual().removeClass("atual").prev();
    if (!$itemAnterior.length){
      $itemAnterior = this._ultimoItem();
    }
    $itemAnterior.addClass("atual");

  },

  _primeiroItem: function () {
    return this.$elemento.find(".carousel > li:first");
  },

  _ultimoItem: function () {
    return this.$elemento.find(".carousel > li:last")
  }
}
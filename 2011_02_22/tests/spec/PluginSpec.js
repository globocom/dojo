
describe("Autocomplete", function() {
  
  
  beforeEach(function(){
      $('#suggest1').Autocomplete();
      $( '#suggest1' ).val('')
  });
  
  afterEach(function(){
    //destruir
  });
  
  it("deve abrir um suggest quando teclar uma letra", function() {
    
    $( '#suggest1' ).val( 'a' ).keydown();
    expect( $( 'div.ac_results ' ).is( ':visible' ) ).toBe( true );
    
  });  
  
  it('deve exibir elementos na lista', function() {
    
    $('#suggest1').val('A').keydown();
    expect($('div.ac_results ul li').size()).toBeGreaterThan(0);
    
  });
  
  it("deve exibir elements que começam com a letra digitada", function() {
    $('#suggest1').val('A').keydown();
    expect($('div.ac_results li').is(":contains('A')")).toBe(true);
  });
  
  it("deve exibir palavras que começam com a letra digitada", function() {
    $('#suggest1').val('A').keydown();
    expect($('div.ac_results li').is(":contains('Aberdeen')")).toBe(true);
  });
  
  it("deve exibir SOMENTE palavras que começam com a letra digitada", function() {
    $('#suggest1').val('A').keydown();
    expect( /<li>[^aA]/.test( $('div.ac_results').html() )).toBe( false );
  });
  
  it("deve com input vazio nao aparecer nada", function() {
    $('#suggest1').val('A').keydown();
    $('#suggest1').val('').keydown();
    
    expect( $( 'div.ac_results ' ).is( ':visible' ) ).toBe( false );
  });
  
  it("deve ter o numero correto de itens",function(){
    
    $('#suggest1').val('A').keydown();
    
    var itensIniciandoComA = $.grep(cities, function(word){
      return word.indexOf('A') == 0;
    }).length;
    
    expect($('div.ac_results > ul > li').length).toBe(itensIniciandoComA);
    
  });
  
});

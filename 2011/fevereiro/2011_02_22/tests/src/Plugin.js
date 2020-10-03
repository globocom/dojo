
// Plugin creation

(function ($) {
  var init = function(){
    var template = '<div class="ac_results"><ul></ul></div>';
    $(template).appendTo( "body" );
  };
  
  $.fn.Autocomplete = function ( arg ) {
    init();
    $(this).keydown(function(){
      
      if( $(this).val().length === 0 ){
    
        $(".ac_results").hide();
    
      }else{
        
        var template = '';

        $.each(cities, function(indice, cidade) {
          if (/^A/.test( cidade ) ) {
            template += '<li>' + cidade + '</li>';
          }
        
        });
         $(".ac_results ul").append(template);
        $(".ac_results").show();
      }
    });

  };

})( jQuery );

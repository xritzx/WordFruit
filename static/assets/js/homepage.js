//AJAX call for the love React Implementation
$(()=>{
    $('.lovedBtn').click(function(){         
        var id = String($( this ).attr('id'));        
        $.ajax({
            type: "GET",
            url: id,
            data: {},
            dataType: "html",
            success: (res,status,xhr)=> {
              if (res=="Liked"){
                $(this).css('color', 'red');
                $(this).css('font-size', '30px');
              }
              else if (res=="Unliked") {
                $(this).css('color', 'black');
                $(this).css('font-size', '20px');
              }
              else{
                window.location.href = '/accounts/login/';
              }
            }
        });
    });
  });
  
  $(()=>{
    $(".lovedBtn").each(function(e){
      var id = String($( this ).attr('id'))+"check/";    
      $.ajax({
        type: "GET",
        url: id,
        data: {},
        dataType: "html",
        success: (res,status,xhr)=> {
          if(res=="True"){
            $(this).css('color','red');  
            $(this).css('font-size', '30px');
          }
        }
      });
    });
  });


  //ajax for search

  $('.searchArea').keyup(()=>{
    var searchText = $('.searchArea').val();
    console.log(searchText.length);
    if(searchText.length > 0){
        $(".searchContent").css('display', 'block');
    }else{
        $(".searchContent").css('display', 'none');
    }
});

$(()=>{
  $('#search').keyup(()=> { 
      $.ajax({
          type: "POST",
          url: "/search/book/",
          data: {
              'search_text': $('#search').val(),
              'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
          },
          dataType: "html",
          success: (res,status,xhr)=> {
              $('#search_results').html(res);
              console.log(res);
          }
      });
  });
});


//AJAX call for the Read button Implementation
$(()=>{
  $('.readBtn').click(function(){         
      var id = String($( this ).attr('id'));        
      $.ajax({
          type: "GET",
          url: id,
          data: {},
          dataType: "html",
          success: (res,status,xhr)=> {
            if (res=="Liked"){
              $(this).css('color', 'violet');
              $(this).css('font-size', '25px');
            }
            else if (res=="Unliked") {
              $(this).css('color', 'black');
              $(this).css('font-size', '15px');
            }
            else{
              window.location.href = '/accounts/login/';
            }
          }
      });
  });
});

$(()=>{
  $(".readBtn").each(function(e){
    var id = String($( this ).attr('id'))+"check/";    
    $.ajax({
      type: "GET",
      url: id,
      data: {},
      dataType: "html",
      success: (res,status,xhr)=> {
        if(res=="True"){
          $(this).css('font-size', '25px');
          $(this).css('color', 'violet');
        }
      }
    });
  });
});

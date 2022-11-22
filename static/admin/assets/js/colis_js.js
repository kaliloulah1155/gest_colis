
$(document).on('change',"select[name='pays']",function(e){
   e.preventDefault();
   var $this=$(this);
   if($this.val() !=''){
       $.ajax({
          url:'/get_ville/'+$this.val(),
          type:'GET',
          success:function(response){
              let options ='';
              $("#id_ville").empty();
              $("#id_ville").append(
                 "<option value=''>Veuillez selectionnez</option>"
            );
            $("#id_commune").empty();
               $("#id_commune").append(
                  "<option value=''>Veuillez selectionnez</option>"
               );
              if(response.data.length !=0){
                    response.data.forEach(ville => {
                        $("#id_ville").append(
                            '<option value="' + ville.id + '">' + ville.libelle+'</option>'
                        ); 
                    });
              }
          },
          error:function(response){
              console.log('Something went wrong');
          }
       });
   }
});

$(document).on('change',"select[name='ville']",function(e){
    e.preventDefault();
    var $this=$(this);
    if($this.val() !=''){
        $.ajax({
           url:'/get_commune/'+$this.val(),
           type:'GET',
           success:function(response){
               
               $("#id_commune").empty();
               $("#id_commune").append(
                  "<option value=''>Veuillez selectionnez</option>"
               );
               if(response.data.length !=0){
                     response.data.forEach(commune => {
                         $("#id_commune").append(
                             '<option value="' + commune.id + '">' + commune.libelle+'</option>'
                         ); 
                     });
               }
           },
           error:function(response){
               console.log('Something went wrong');
           }
        });
    }
 });


$("input[name='colis-0-montant']").attr("readonly",true);
$("input[name='colis-0-montant']").css({"background-color":"lightgray","cursor":"not-allowed"});

$("input[name='colis-0-date_estimation']").attr("readonly",true);
$("input[name='colis-0-date_estimation']").css({"background-color":"lightgray","cursor":"not-allowed"});

 
 if ($('#id_colis-0-status_livraison').val()==="9" || $('#id_colis-0-status_livraison').val()==="29") {
    $("select[name='colis-0-status_livraison']").prop("disabled",true);
    
   $('.submit-row').remove();  
    
 }
 else {
    $("select[name='colis-0-status_livraison']").prop("disabled",false);
    
};



$("#colis_comp-group table").ready(function(){
   
   var table =$(this); 
   //var cells = currentRow.cells;
   $("#colis_comp-group table tr").each(function(){
        $(this).find("td:eq(2) input[type='number']").each(function(){
            //$(this).val(0);
            $(this).attr("readonly",true);
            $(this).css({"background-color":"lightgray","cursor":"not-allowed"});

        });
        $(this).find("td:eq(4) input[type='number']").each(function(){
            //$(this).val(0);
            $(this).attr("readonly",true);
            $(this).css({"background-color":"lightgray","cursor":"not-allowed"});

        });
    });
});

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


 //Modify period of estimated date by delay
 Date.prototype.addDays = function(days) {
    var date = new Date(this.valueOf());
    date.setDate(date.getDate() + days);
    return date.toLocaleDateString();
}

$(document).on('change','#id_colis-0-delai',function(e){
    e.preventDefault();
    var $this=$(this);
    var date_est1=$("input[name='date_depart']").val();
    if($this.val() !=''){
 
        $.ajax({
            url:'/get_delay/'+$this.val(),
            type:'GET',
            success:function(response){
                if(response.data.length !=0){
                    response.data.forEach(delay => {

                     if(date_est1 !=''){
                     
                       var fmt_date=date_est1.split("/");
                       var dd='';
                       var mm='';
                       var yyyy=fmt_date[2];
                        dd = fmt_date[0] > 9 ? fmt_date[0] : '0'+fmt_date[0];
                        mm = fmt_date[1] > 9 ? fmt_date[1] : '0'+fmt_date[1];
                        const formattedDate = yyyy+'-'+mm+'-'+dd;
                        var date_est2 = new Date(formattedDate);

                        var delay_date= date_est2.addDays(parseInt(delay.valeur));
                        if(delay.valeur!=''){
                            $("input[name='colis-0-date_estimation']").val(delay_date);
                        }  
                    } 
                    });
                }
            },
            error:function(response){
                console.log('Something went wrong');
            }
         });

    }else{
        $("input[name='colis-0-date_estimation']").val(date_est1);
    }
});



$("#colis_comp-group table").on('change','select',function(){
    // get the current row
    var currentRow = $(this).closest("tr")[0]; 
    var cells = currentRow.cells;
    var $this=$(this);
    $.ajax({
        url:'/get_product/'+$this.val(),
        type:'GET',
        success:function(response){
            if(response.data.length !=0){
                response.data.forEach(product => {
                    var pu=parseInt(product.valeur);
                    var qte=1;
                    var mtn=parseInt(pu)*parseInt(qte);
                    cells[2].getElementsByTagName('input')[0].value=pu;
                    cells[3].getElementsByTagName('input')[0].value=qte;
                    cells[4].getElementsByTagName('input')[0].value=mtn;
                });
            }
        },
        error:function(response){
            console.log('Something went wrong');
        }
     }); 
});

//On change price 
$("#colis_comp-group table").on('keyup','.field-qte input[type=number]',function(){
    var currentRow = $(this).closest("tr")[0]; 
    var cells = currentRow.cells;
    var $this=$(this);
    if($this.val() !='' || !isNaN($this)){
        var pu=parseInt(cells[2].getElementsByTagName('input')[0].value);
        var qte=parseInt($this.val());
        var mtn=parseInt(pu)*parseInt(qte);
        cells[4].getElementsByTagName('input')[0].value=mtn;
    }
});

// GET PRICE OF WEIGHT
$(document).on('change','#id_colis-0-poids',function(){
    var $this=$(this);
    if($this.val() !=''){
        $.ajax({
            url:'/get_poids_price/'+$this.val(),
            type:'GET',
            success:function(response){
                if(response.data.length !=0){
                    response.data.forEach(poids => {
                        var poids=parseInt(poids.valeur);
                        $("input[name='colis-0-montant']").val(poids);
                    });
                }
            },
            error:function(response){
                console.log('Something went wrong');
            }
        }); 
    }else{
        $("input[name='colis-0-montant']").val(0);
    }
});



var stt_etape=$('.field-etape .readonly').text();
var stt_colis =$('.field-num_colis .readonly').text();

//alert(stt_colis);
if(stt_etape==1 && $('.group_user').val()==2){ //Aucune actions disponible pour le gestionnaire des colis
   $('.submit-row').remove();  
 }

 if(stt_etape==1){
    $('.send_colis').remove();
   // $('.submit-row').remove();
    
 }
 if(stt_colis=="-"){
    $('.send_colis').remove();
 }


 //Changement de l'etat de livraison du colis 

 $(document).on('change','#id_colis-0-status_livraison',function(e){
    e.preventDefault();

    var valeur = $(this).val();
    var num_colis=stt_colis;
    //9 livrée
    if(valeur !=''){

        $.ajax({
            url:'/get_colis_clos/'+valeur+'/'+num_colis,
            type:'GET',
            success:function(response){
                //if(response.data.length !=0){    
                //}
                console.log(response);
            },
            error:function(response){
                console.log('Something went wrong');
            }
        }); 
    }
 });


 $(document).on('click',"input[name='_save']",function(){

    var valeur = $('#id_colis-0-status_livraison').val();
    var num_colis=stt_colis;
    //9 livrée  || 29 Annulée
    if(valeur !=''){

        $.ajax({
            url:'/get_colis_clos/'+valeur+'/'+num_colis,
            type:'GET',
            success:function(response){
                //if(response.data.length !=0){    
                //}
                console.log(response);
            },
            error:function(response){
                console.log('Something went wrong');
            }
        }); 
    }
 });

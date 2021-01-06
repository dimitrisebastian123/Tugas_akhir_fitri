$(".btn-cari-halaman").click(function (e) {
    let data = $('.cari_halaman').val()
    // window.location.href =  window.location.host+'/'+data
    window.location.href = (window.location.protocol+'//'+window.location.host+'/'+data)
}); 

// Add the following code if you want the name of the file appear on select
$(".custom-file-input").on("change", function() {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
  });
$(document).ready(function(){
    $(document).bind("contextmenu",function(e){
       return false;
    });
 });
(function(){
$("#employed_id").click(function(e){

	if (document.getElementById('id_employed').checked){
        document.getElementById('id_company').disabled = false;
        document.getElementById('id_workplace').disabled = false;
    } else {
        document.getElementById('id_company').disabled = true;
        document.getElementById('id_company').value = "";
        document.getElementById('id_workplace').disabled = true;
        document.getElementById('id_workplace').value = "";
    }
    
    
});
})();
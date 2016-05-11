(function(){
$(".delete_parent_link").click(function(e){
	e.preventDefault();
	var ok_cancel;
	var ok_cancel = confirm("Da li ste sigurni da želite da obrišete roditelja?");
	if (ok_cancel == true) {
    	window.location.href = e.target.href;
	} else {
	}
});
})();
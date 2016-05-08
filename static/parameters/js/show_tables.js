(function(){
$(".delete_table_link").click(function(e){
	e.preventDefault();
	var ok_cancel;
	var ok_cancel = confirm("Are you sure you want to delete this item?");
	if (ok_cancel == true) {
    	txt = "You pressed OK!";
    	var href = e.target.href;
    	window.location.href = href;
	} else {
    	txt = "You pressed Cancel!";
	}
});
})();
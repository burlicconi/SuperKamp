(function(){
$(".delete_line_link").click(function(e){
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
$(".edit_line_link").click(function(e){
	e.preventDefault();
	console.log("Radim edit sada" + e);
	var ok_cancel;
	var ok_cancel = confirm("Save  changes?");
	if (ok_cancel == true) {
    	txt = "You pressed OK!";
    	document.getElementById('update_form').submit();
	} else {
    	txt = "You pressed Cancel!";
	}
	console.log(txt);
});
})();

$( "#advance_button" ).click(function() {
  $( "#advance_search" ).slideToggle( "slow" );
});
$( "#close_advance" ).click(function() {
  $( "#advance_search" ).slideToggle( "slow" );
});
$( "#clear_advance_table" ).click(function() {
	$("#table_no").val('');
	$("#table_desc").val('');

});
$( "#clear_advance_line" ).click(function() {
	$("#line_no").val('');
	$("#line_desc").val('');
});

/**
 * 
 */

$(document).ready(function(){
	console.log("reaching here first");
	$("div input").keyup(function(){
		console.log(parseInt($(this).val()));
		if(parseInt($(this).val()) < 0){
			console.log("invalid input");
			$("div").addClass("has-error");
		}
	});
});
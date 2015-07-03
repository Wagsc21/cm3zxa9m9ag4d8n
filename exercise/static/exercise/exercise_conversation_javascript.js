$(document).ready(function(){
	//confirm("reaching here");
	var moduleId = $("input[name=\"module-specific-message\"]").val();
	$module_specific_message = $(".module-specific-message");
	//console.log($module_specific_message.text());
	setMessage(moduleId);
	var availableTechniques = [
		"suggest an opposite thought",
		"visualizing the situation",
	];

	$(document).on('click', 'input[name=\"submit-button\"]', function (ev) {
		ev.preventDefault();
		var $form = $("#exercise-form");
		var url = $form.attr("action");
		console.log(url);
		var conversationid = $form.find("input[name=\"conversationid\"]").val();
		console.log(conversationid);
		var technique = $form.find("input[name=\"technique\"]").val();
		console.log(technique);
	
	$.ajax({
		type: "POST",
		url: url, //get the url here
		data: {
				//csrftoken: csrftoken, 
				conversationid: conversationid, 
				technique: technique,
			},
			beforeSend: function(xhr){
				console.log("reaching here");
				xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
			},
			success:function(data){
				//console.log("it is being sent");
				if(!data){
					alert("you are dog man");
				}else{
					//alert(data);
					$(".to-be-replaced").replaceWith("<div class=\"to-be-replaced\">"+$(data).find(".to-be-replaced").html()+"</div>");
					//console.log($(data).text().includes("Great that worked"));
					if($(data).text().includes("Great that worked")){
						console.log($(data).find("#result-conversation").text());
						$(".result").addClass("bg-success");
					}else{
						console.log("incorrect");
						$(".result").addClass("bg-danger");
					}
				}
			},
			
			error: function(xhr,errmsg,err){
				alert(xhr.status + ": " + xhr.responseText);
			}
		});
	});
	
	//autocomplete textbox; currently suggests only on exact match
	$("input[name=\"technique\"]").autocomplete({
		source: availableTechniques
	});
	/*
	$("input[name=\"technique\"]").on("input", function(e){
		//alert("changed");
		//console.log($("input[name=\"technique\"]").val());
		var keywords = $("input[name=\"technique\"]").val().split(" ");
	});*/
});

var setMessage = function(moduleId){
	var message;
	switch(moduleId){
		case '1':
		message = "Psychoeducation";
		break;
		case '2':
		message = "Behavioral Activation";
		break;
		case '3':
		message = "Identifying NATs";
		break;
		case '4':
		message = "Challenging NATs";
		break;
		case '5':
		message = "Modifying Intermediate and Core Beliefs";
		break;
		case '6':
		message = "Relapse Prevention";
		break;
	}
	$module_specific_message.text(message);
}
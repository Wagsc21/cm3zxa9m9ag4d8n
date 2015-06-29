/*
$(document).ready(function(){
	//console.log(breaktext($('#choice-text').text()));
	//$choice_text = $(".choice-text");
	$dialog_text = $("#dialog-text");
	$user_avatar = $("#user-avatar");
	$button_class = $("#button-class");
	$to_be_updated = $(".to-be-updated");
	//$choice_text.replaceWith("<button type=\"submit\" name=\"option\" value={{choice.optionID}} class=\"btn btn-success\" id=\"choice-text\"><pre>"+breaktext($choice_text.text())+"</pre></button>");
	$dialog_text.textillate({ 
		in: { 
			effect: 'fadeIn',
			delay: 5
		},
	});
	$dialog_text.on("end.tlt", function(){
		//I am having to use button class here but ideally I should be using $choice_text; this might lead to problems later on, keep a watch on it
		$(".btn").removeClass("hidden");
		$user_avatar.removeClass("hidden");
	});
	/*
	$(".choice-text").click(function(event){
		console.log("reaching here");
		event.preventDefault();
		var $form = $("#conversation-form"),
			//name = $form.find("button[name=\"option\"]").val(),
			option = $(this).val();
			console.log(option);
			dialog = $form.find("input[name=\"dialog\"]").val(),
			console.log(dialog);
			url = $form.attr("action");
			console.log(option, dialog);
			confirm(option+" "+dialog);
		var csrftoken = getCookie("csrftoken");
		var ajaxPosting = $.ajax({
			type: "POST",
			//dataType: "json",
			url: url, 
			data: {
				csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value, 
				option: option, 
				dialog: dialog
			},
			//console.log("reaching here");
			success:function(data){
			
				$next_dialog = $(data).find("#dialog-text").text();
				//console.log($data);
				$dialog_text.replaceWith("<p id=\"dialog-text\">"+$next_dialog+"</p>");
				$button_class.replaceWith($(data).find("#button-class").html());
				$to_be_updated = $(".to-be-updated");
				$to_be_updated.replaceWith("<div class=\"to-be-updated\">"+$(data).find(".to-be-updated").html()+"</div>");
			}
		});
		
		posting.done(function(data){
			//$dialog_text.replaceWith("<p id=\"dialog-text\">{{"++"}}</p>");
			//confirm("reaching here");
			$data = $(data).find(dialog);
			console.log($data);
		});

	});
});

//apparently this is not needed; you can include a pre around the choice text in html and it will display a pre formatted text; if you feel a text is too long, then
// break it in various lines
var breaktext = function(inputString){
	var newString='';
	var stringArray = inputString.split(",");
	for(var i=0; i<stringArray.length; i++){
		newString+="\n"+stringArray[i];
	}
	console.log(newString);
	return newString;
}

var getCookie = function(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}*/

$(document).ready(function(){
	//this little code makes the dailog text fadeIn gradually and displays the user options and avatar only after the entire text is displayed
	/*
	$dialog_text = $("#dialog-text");
	$user_avatar = $("#user-avatar");
	$dialog_text.textillate({ 
		in: { 
			effect: 'fadeIn',
			delay: 5
		},
	});
	$dialog_text.on("end.tlt", function(){
		//I am having to use button class here but ideally I should be using $choice_text; this might lead to problems later on, keep a watch on it
		$(".btn").removeClass("hidden");
		$user_avatar.removeClass("hidden");
	});*/
	allEffects();
	//adding first conversation to conversation history


	var csrftoken = $.cookie('csrftoken');
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	$(".choice-text").click(function(event){
		console.log("reaching here");
		event.preventDefault();
		//appending option to conversation history
		
		$conversation_history.append("<p>"+$(this).text()+"</p>");
		var $form = $("#conversation-form"),
			//name = $form.find("button[name=\"option\"]").val(),
			option = $(this).val();
			console.log(option);
			dialog = $form.find("input[name=\"dialog\"]").val(),
			console.log(dialog);
			url = $form.attr("action");
			console.log(option, dialog);
			//confirm(option+" "+dialog);
			
			$.ajax({
				type: "POST",
				url: url, 
				data: {
					csrftoken: csrftoken, 
					option: option, 
					dialog: dialog
				},
				//console.log("reaching here");
				success:function(data){
					/*
					$next_dialog = $(data).find("#dialog-text").text();
					//console.log($data);
					$dialog_text.replaceWith("<p id=\"dialog-text\">"+$next_dialog+"</p>");
					$button_class.replaceWith($(data).find("#button-class").html());*/
					$to_be_updated = $(".to-be-updated");
					$to_be_updated.replaceWith("<div class=\"to-be-updated\">"+$(data).find(".to-be-updated").html()+"</div>");
					//this little code makes the dailog text fadeIn gradually and displays the user options and avatar only after the entire text is displayed
					allEffects();
				}
		});
		});
//this little code makes the dailog text fadeIn gradually and displays the user options and avatar only after the entire text is displayed

});

//for csrf hoopla
var csrfSafeMethod = function(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

//this little code makes the dailog text fadeIn gradually and displays the user options and avatar only after the entire text is displayed
var allEffects = function(){
	$dialog_text = $("#dialog-text");
	$user_avatar = $("#user-avatar");
	$choice_text = $(".choice-text");
	$dialog_text.textillate({ 
		in: { 
			effect: 'fadeIn',
			delay: 5
		},
	});
	$dialog_text.on("end.tlt", function(){
					//I am having to use button class here but ideally I should be using $choice_text; this might lead to problems later on, keep a watch on it
		$choice_text.removeClass("hidden");
		$user_avatar.removeClass("hidden");
		$conversation_history = $(".conversation-history");
		$conversation_history.append("<p>"+$("#dialog-text").text()+"</p>");
	});
}

var saveConversationHistory = function(dialog, option){
	$conversation_history = $(".conversation-history");
	$conversation_history.append("<pre></pre>");
}
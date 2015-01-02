jQuery(function($){
	var answerForm = $('.answer-form');
	if(!answerForm.length){ // If user is not authenticated.
		return;
	}
	var answerTemplate = _.template($('.answer-template').html());
	var answers = $('.answers');
	var textInput = answerForm.find('.answer-form-text');
	answerForm.validate({
		rules: {
			answer: {required: true}
		},
		submitHandler: function(form){
			var text = textInput.val();
			$.ajax({
				type: 'post',
				data: {
					answer: text
				},
				headers: {
					'X-CSRFToken': $.cookie('csrftoken')
				}
			})
				.always(function(){
					answerForm.find('.gauge').remove();
				})
				.success(function(){
					textInput.val('');
					$(answerTemplate({ text: text }))
						.appendTo(answers)
						.hide()
						.slideDown()
					;
				})
			;
			answerForm.find('button').after('<div class="gauge">');
		}
	});
});

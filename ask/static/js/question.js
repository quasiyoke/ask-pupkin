jQuery(function($){
	var answerForm = $('.answer-form');
	answerForm.validate({
		rules: {
			answer: {required: true}
		},
		submitHandler: function(form){
			var textInput = answerForm.find('.answer-form-text');
			$.ajax({
				method: 'POST',
				data: {
					answer: textInput.val()
				}
			})
				.always(function(){
					answerForm.find('.gauge').remove();
				})
				.success(function(){
					textInput.val('');
				})
			;
			answerForm.find('button').after('<div class="gauge">');
		}
	});
});

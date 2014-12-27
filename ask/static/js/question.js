jQuery(function($){
	var answerForm = $('.answer-form');
	answerForm.validate({
		rules: {
			answer: {required: true}
		},
		submitHandler: function(form){
			$.ajax({
				method: 'POST',
				data: {
					answer: answerForm.find('.answer-form-text').val()
				}
			})
				.always(function(){
					answerForm.find('.gauge').remove();
				})
			;
			answerForm.find('button').after('<div class="gauge">');
		}
	});
});

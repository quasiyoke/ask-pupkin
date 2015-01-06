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
			answerForm.find('button').append('<div class="gauge">');
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
		}
	});

	$('body')
		.on('change', '.correct-answer-checkbox', function(e){
			e.preventDefault();
			var isRight = $(this);
			var container = isRight.next();
			var id = /\d+/.exec(isRight.attr('id'))[0];
			container.append('<div class="gauge">');
			$.ajax({
				type: 'post',
				url: '/answers/' + id + '/',
				data: {
					is_right: isRight.prop('checked')
				},
				headers: {
					'X-CSRFToken': $.cookie('csrftoken')
				}
			})
				.always(function(){
					container.find('.gauge').remove();
				})
				.success(function(response){
					if('ok' === response.status){
						isRight.prop(response.is_right);
					}
				})
			;
		})
	;
});

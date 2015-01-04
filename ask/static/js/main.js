jQuery(function($){
	$('body')
		.on('click', '.vote-button', function(e){
			e.preventDefault();
			var button = $(this);
			var container = button.closest('.voting');
			var id = container.attr('data-id');
			var delta = button.is('.vote-button_up') ? 1 : -1;
			$.ajax({
				type: 'post',
				data: {
					delta: delta
				},
				url: '/profiles/' + id + '/',
				headers: {
					'X-CSRFToken': $.cookie('csrftoken')
				}
			})
				.always(function(){
					container.find('.gauge').remove();
				})
				.success(function(response){
					if('ok' === response.status){
						var amount = container.find('.vote-amount');
						amount.text(response.new_rating);
					}
				})
			;
			container.append('<div class="gauge">');
		})
	;
});

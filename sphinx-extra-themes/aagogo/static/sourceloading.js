$(document).ready(function(){
	$('<div/>', {id:'sessionDiv', style:'float:right'}).appendTo('div.rel');

	$.ajax({
		url: '/pyweb',
		data: { cmd: 'checklogin' },
		dataType: 'json',
		success: function(response) {
			if (response.logged) {
				userIsLogged(response.username);
				loadSolutions();
			} else {
				defaultuser();
			}
		},
		error: function() {
			$('#sessionDiv').html('Lahendusserveriga esines tõrge!');
		}
	});
});

function defaultuser() {
	var formhtml = [
		'<form id="loginform" method="post" action="">',
		'<input type="text" size="15" name="username" id="username" />',
		'<input type="password" size="15" name="password" id="password" />',
		'<input type="submit" id="login" value="Logi sisse" />',
		'</form>'
	];
	$('#sessionDiv').html(formhtml.join(''));

	$('#loginform').submit(function() {
		var usr = $('#username').val();
		var pw = $('#password').val();
		if (usr && pw) {
			login(usr, pw);
		} else {
			alert("Väljad on korrektselt täitmata.");
		}
		return false;
	});
}

function userIsLogged(username) {
	// show login info
	var formhtml = [
		'<span style="color:#fff">',
		'Oled sisse logitud: <strong>'+username+'</strong></span> | ',
		'<a href="javascript:void(0)" onclick="logout()">logi välja</a>'
	];
	$('#sessionDiv').html(formhtml.join(''));

	// set up custom divs
	$('div.autotest').each(function() {
		var parentid = $(this).attr('id');
		$('<div/>', {id: 'solution-'+parentid}).appendTo($(this));
		$('<div/>', {id: 'submit-'+parentid}).appendTo($(this));
		$('<textarea/>', {
			id: 'text-'+parentid, 
			text: 'Esita lahendus siia.', 
			rows: '15', 
			cols: '95'})
			.appendTo('#submit-'+parentid);
		$('<button/>', {
			onClick: 'submitSolution("'+parentid+'")',
			style: 'display: block;',
			text: 'Saada hindamiseks!'})
			.appendTo('#submit-'+parentid);
	});

}

function flushForms() {
	$('div.autotest').each(function() {
		$(this).children().empty();
	});
}

function login(usr, pw) {
	$.ajax({
		type: 'POST',
		url: '/pyweb',
		dataType: 'json',
		data: {
			cmd: 'login',
			user_id: usr,
			password: pw
		},
		success: function(json) {
			console.log(json.result);
			if (json.result == 'success') {
				userIsLogged(usr);
				loadSolutions();
			}
		},
		error: function() {
			$('#sessionDiv').html('Lahendusserveriga esines tõrge!');
		}
	});	
}

function logout() {
	$.ajax({
		type: 'POST',
		url: '/pyweb',
		dataType: 'json',
		data: {
			cmd: 'logout',
		},
		success: function() {
			flushForms();
			defaultuser();
		},
		error: function() {
			console.log('logout failed');
			defaultuser();
		}
	});
}

function loadSolutions() {
	$('div.autotest').each(function() {
		var id = $(this).attr('id');

		$.ajax({
			type: 'GET',
			url: '/pyweb',
			dataType: 'json',
			async: false,
			data: {
				cmd: 'get_solution',
				exercise_id: id
			},
			success: function(json){
				console.log(json.code);
				var html = [
					'<div class="highlight-py3 highlight">',
					'<p>Sinu esitatud lahendus:</p> <pre>',
					json.code,
					'</pre></div>'
				];
				$('#solution-'+id).html(html.join(''));
			},
			error: function(){
				console.log('could not fetch data');
			}
		});
	});
}

function submitSolution(id) {
	$.ajax({
		type: 'POST',
		url: '/pyweb',
		dataType: 'json',
		data: {
			cmd: 'submit_solution',
			exercise_id: id,
			solution: $('#text-'+id).val()
		},
		success: function(json) { 
			// TODO write these into the code
			console.log(json.points);
			console.log(json.comments);
		},
		error: function() {
			console.log('unable to post data');
		}
	});
}

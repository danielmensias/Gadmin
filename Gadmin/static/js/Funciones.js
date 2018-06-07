$(document).ready(function() {
	   //Funcion para datatables
		var table = $('#tabla').DataTable({
			"language" : {
				url : "/static/es/es_ES.json"
			}
		});

		$('#tabla tbody').on('click', 'tr', function() {
			if ($(this).hasClass('selected')) {
				$(this).removeClass('selected');

			} else {
				table.$('tr.selected').removeClass('selected');
				$(this).addClass('selected');
			}
		});
		
        //Funcion para despliegue de palabras informativas en la aplicacion
		$('[data-toggle="ayuda"]').tooltip();		
		
		
	});




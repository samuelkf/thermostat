$(function() {

    function updatevalues() {
	    $.get('http://localhost:7379/GET/targettemp.txt', function(data) {
		$('#target').text(data);
	    });

	    $.get('http://localhost:7379/GET/curtemp.txt', function(data) {
		$('#currenttemp').text(data);
	    });

	    $.get('http://localhost:7379/GET/curhum.txt', function(data) {
		$('#currenthum').text(data);
	    });

	    $.get('http://localhost:7379/GET/heat.txt', function(data) {
		if (data == 1) {
		  $('#heat').text('On');
		}
		else {
		  $('#heat').text('Off');
		}
	    });
    }

    updatevalues();

    $(".button").click(function() {
        var $button = $(this);
    
        if ($button.text() == "+") {
	  $.get('http://localhost:7379/INCR/targettemp.txt', function(data) {
	    $('#target').text(data);
	  });
    	} else {
	    $.get('http://localhost:7379/DECR/targettemp.txt', function(data) {
		$('#target').text(data);
	    });
    	}
	window.setTimeout(updatevalues, 1000);
    });

    window.setInterval(updatevalues, 10000);

});

SC.initialize({
		client_id: "5e878c0a4da753a596862a33ffbcc036",
});

function playSong(trackUrl) {
	$.ajax({
		url: "http://api.soundcloud.com/resolve.json?url=" + trackUrl + "&client_id=5e878c0a4da753a596862a33ffbcc036",
		success: function(data) {
			var track_id = results[0].id;
			SC.stream("/tracks/" + track_id, {autoPlay: true});
	});	

});
	
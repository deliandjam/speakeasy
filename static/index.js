
  SC.initialize({
		client_id: "5e878c0a4da753a596862a33ffbcc036",
	});

	$("#stream").click(function() {
    SC.stream("/tracks/212253345", {autoPlay: true});
  });

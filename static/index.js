
<script src="//connect.soundcloud.com/sdk-2.0.0.js"></script>
<script>
SC.initialize({
  client_id: '5e878c0a4da753a596862a33ffbcc036'
});

// permalink to a track
var track_url = 'https://soundcloud.com/astateoftrance/masoud-feat-melissa-loretta-best-days-progressive-mix-a-state-of-trance-episode-693';

SC.get('/resolve', { url: track_url }, function(track) {
  SC.get('/tracks/' + track.id + '/comments', function(comments) {
    for (var i = 0; i < comments.length; i++) {
      console.log('Someone said: ' + comments[i].body);
    }
  });
});
</script>
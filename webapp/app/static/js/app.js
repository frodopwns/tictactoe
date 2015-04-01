$(document).ready(function() {

    //handles click event for a cell on the game board
    $(".cell").click(function() {
        //get initial cell value so we don't update one that has already
        //been chosen by a player
        var cellValue = $(this).html().trim();

        //if the cell hasn't been filled and the game is not over we can make the move
        if (cellValue == '' && over != true && turn == side) {
            var elid = $(this).attr('id');
            var loc = $(this).attr('id').slice(5);
            //post clicked position to server to update the db and emit web socket broadcast to other players
            $.post( "/update", { id: gameId, turn: turn, loc: loc } ).done(
                function( data, loc ) {
                    //handle win or tie scenarios
                    var winner = data.winner;
                    var full = data.full;
                    //update other clients of this game
                    socket.emit('my broadcast event', {data: {
                        el: elid,
                        id: gameId,
                        turn: turn,
                        loc: loc,
                        winner: winner,
                        full: full,}
                    });
                });

            $(this).removeClass("hover");


        }
    });

    $( "td.cell" ).hover(
        function() {
            if ($(this).html().trim() == '') {
                $(this).addClass("hover");
            } else {
                $(this).css("cursor", "default");
            }
        }, function() {
            if ($(this).html().trim() == '') {
                $(this).removeClass("hover");
            }
        }
    );
});
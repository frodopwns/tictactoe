$(document).ready(function() {

    //handles click event for a cell on the game board
    $(".cell").click(function() {
        //get initial cell value so we don't update one that has already
        //been chosen by a player

        var cellValue = $(this).html().trim();
        console.log(turn);
        console.log(side);
        console.log(cellValue);
        console.log(over);
        //if the cell hasn't been filled and the game is not over we can make the move
        if (cellValue == '' && over != true && turn == side) {
            console.log('inside');
            var elid = $(this).attr('id');
            var winner = '';
            var full = '';
            //post clicked position to server to update the db
            $.post( "/update", { id: gameId, turn: turn, loc: $(this).attr('id').slice(5) } ).done(function( data ) {
                    //handle win or tie scenarios
                winner = data.winner;
                full = data.full;

                });
            $(this).removeClass("hover");
            //flip turn to next player
            socket.emit('my broadcast event', {data: {
                el: elid,
                id: gameId,
                turn: turn,
                loc: $(this).attr('id').slice(5) },
                winner: winner,
                full: full,
            });

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
$(document).ready(function() {

    //handles click event for a cell on the game board
    $(".cell").click(function() {
        //get initial cell value so we don't update one that has already
        //been chosen by a player
        var cellValue = $(this).html().trim();
        //if the cell hasn't been filled and the game is not over we can make the move
        if (cellValue == '' && over != true) {
            //set correct value in clicked cell
            $(this).html(turn);
            //post clicked position to server to update the db
            $.post( "/update", { id: gameId, turn: turn, loc: $(this).attr('id').slice(5) } ).done(function( data ) {
                    //handle win or tie scenarios
                    if (data.winner) {
                        $(".data").html("Game Over! " + data.winner + " wins.");
                        over = true;
                    } else if (data.full) {
                        $(".data").html("Game Over! Tie.");
                        over = true;
                    }
                    //set pointer to default if game over
                    if (over == true) {
                        $(".cell").css("cursor", "default");
                    }
                });
            //flip turn to next player
            turn = (turn == 'x') ? 'o': 'x';
            side = turn;
            //set turn indicator
            $("#turn").html(turn);
            //update instructions
            $(".data").html("Please place an " + side + " on the game board.");
        }
    });

});
$(document).ready(function() {

    rebuild = function(game) {
        console.log("in the rebuild");
        console.log(game);
        if (game.winner) {
            console.log("winner");
            $(".data").html("Game Over! " + game.winner + " wins.");
        } else if (game.full) {
            $(".data").html("Game Over! Tie.");
        } else if (game.turn == side) {
            $(".data").html("Please place an " + side + " on the game board..");
            $(".cell").css("cursor", "pointer");
        }
    }

    waitTurn = function(id) {
            setTimeout(function() {
                setInterval(function () {
                    $.ajax({
                        url: "/ajax/" + id, success: function (data) {

                            if (side == data.turn) {
                                rebuild(data);
                            }
                        }, dataType: "json"
                    });
                }, 3000);
            }, 3000);


    }

    if (turn != side) {
        $(".cell").css("cursor", "default");
    } else {
        $(".cell").css("cursor", "pointer");
    }
    $(".cell").click(function() {

        var cellValue = $(this).html().trim();
        console.log(cellValue);
        if (turn == side && cellValue == '') {
            $(this).html(turn);
            $.post( "/update", { id: gameId, turn: turn, loc: $(this).attr('id').slice(5) } ).done(function( data ) {
                    console.log(data);
                    if (data.winner) {
                        $(".data").html("Game Over! " + data.winner + " wins.");
                    } else if (data.full) {
                        $(".data").html("Game Over! Tie.");
                    }
                });

            $(".cell").css("cursor", "default");
            $(".data").html("Not your turn!");
            //waitTurn(gameId);
        }

    });



});
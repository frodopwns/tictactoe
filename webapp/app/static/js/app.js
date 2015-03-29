$(document).ready(function() {

    $(".cell").click(function() {

        var cellValue = $(this).html().trim();
        console.log(cellValue);
        console.log("turn " + turn + " side " + side);
        console.log(over);

        if (turn == side && cellValue == '' && over != true) {
            $(this).html(turn);
            $.post( "/update", { id: gameId, turn: turn, loc: $(this).attr('id').slice(5) } ).done(function( data ) {
                    console.log(data);
                    if (data.winner) {
                        $(".data").html("Game Over! " + data.winner + " wins.");
                        over = true;
                    } else if (data.full) {
                        $(".data").html("Game Over! Tie.");
                        over = true;
                    }
                    if (over == true) {
                        $(".cell").css("cursor", "default");
                    }
                });
            $("input[name='" + turn + "']").prop("checked", false)
            turn = (turn == 'x') ? 'o': 'x';
            side = turn;
            $("#turn").html(turn);
            $("input[name='" + turn + "']").prop("checked", true)

            $(".data").html("Please place an " + side + " on the game board.");

        }

    });



});
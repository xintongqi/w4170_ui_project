function incre_score(){
    console.log("incrementing score");
    $.ajax({
        type: "POST",
        url: "/quiz/incre_score",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        success: function(result){
            console.log(result['current_quiz_score'])
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error);
        }
    })
}
function add_choice(user_choice){
    console.log("adding choice");
    let data_to_save = {"id": id, "choice": user_choice}
    $.ajax({
        type: "POST",
        url: "/quiz/add_choice",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            console.log(result)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error);
        }
    })
}
// Function to show the "Next" button
function goBack() {
    // Implement logic for going back
    window.location.href = "/quiz/"+content['prev'];
}
function goNext() {
    // Implement logic for going next
    window.location.href = "/quiz/"+content['next'];
}
function goResult(){
    window.location.href = "/quiz/result";
}
function Acorrect(){
    $('#quiz_A_but').prop('disabled', true);
    $('#quiz_B_but').prop('disabled', true);
    $('#quiz_A_but').removeClass('btn-light').addClass('btn-success');
    $('#quiz_B_but').removeClass('btn-light').addClass('btn-danger');
}
function Bcorrect(){
    $('#quiz_A_but').prop('disabled', true);
    $('#quiz_B_but').prop('disabled', true);
    $('#quiz_B_but').removeClass('btn-light').addClass('btn-success');
    $('#quiz_A_but').removeClass('btn-light').addClass('btn-danger');
}
function correct(){
    $("#quiz_right_wrong").html("Correct!");
    $('#quiz_right_wrong').css("color","green");
    incre_score();
}
function wrong(){
    $("#quiz_right_wrong").html("Wrong :(");
    $('#quiz_right_wrong').css("color","red");
}
function showBackButton() {
    $('#quiz_backButton').show();
}
function showNextButton() {
    $('#quiz_nextButton').show();
}
$(document).ready(function(){
    $('#quiz_num').append(id+'.');
    $('#quiz_question').append(content['question']);
    if (id < 6){
        $('#basic_folds_bar').addClass('bold');
        $('#boat_bar').addClass('lighter');
    } else {
        $('#basic_folds_bar').addClass('lighter');
        $('#boat_bar').addClass('bold');
    }
    if (content['prev'] != null) {
        console.log("showing")
        showBackButton()
    }
    $('#quiz_backButton').click(function() {
        // Call the goBack function when the Back button is clicked
        goBack();
    });
    // Attach click event handler to the Next button
    $('#quiz_nextButton').click(function() {
        // Call the goNext function when the Next button is clicked
        if (content['next'] != null) {
            goNext();
        } else {
            goResult();
        }
    });

    // Attach click event handler to the Submit button
    $('#quiz_A_but').click(function() {
        // Call the showNextButton and submitForm functions when the Submit button is clicked
        showNextButton();
        add_choice('A')
        if (content['answer'] === 'A') {
            Acorrect();
            correct();
        } else {
            Bcorrect();
            wrong()
        }
        
    });
    $('#quiz_B_but').click(function() {
        // Call the showNextButton and submitForm functions when the Submit button is clicked
        showNextButton();
        add_choice('B')
        if (content['answer'] === 'B') {
            Bcorrect();
            correct();
        } else {
            Acorrect();
            wrong()
        }
    });
});
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
function submitForm() {
    // Implement logic for form submission
    // For example, you can validate the form fields here
}
function showBackButton() {
    $('#quiz_backButton').show();
}
function showNextButton() {
    $('#quiz_nextButton').show();
}
$(document).ready(function(){
    $('#step').append(id);
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
    $('#quiz_submitButton').click(function() {
        // Call the showNextButton and submitForm functions when the Submit button is clicked
        showNextButton();
        submitForm();
    });
});
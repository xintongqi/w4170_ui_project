$(document).ready(function () {
    $("#search-form").submit(function (event) {
        let searchText = $("#search-input").val().trim();
        if (searchText === "") {
            event.preventDefault(); 
            $("#search-input").val("");
            $("#search-input").focus();
        }
    });
});
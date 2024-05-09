$(document).ready(function () {
  $("#quiz_resultHome").click(function () {
    window.location.href = "/";
  });

  // Attach click event handler to the Next button
  $("#quiz_resultLearn").click(function () {
    window.location.href = "/learn_step/1";
  });

  // Attach click event handler to the Submit button
  $("#quiz_resultQuiz").click(function () {
    window.location.href = "/quiz/1";
  });
});

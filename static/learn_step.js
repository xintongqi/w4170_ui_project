function display_step(step) {
  var stepHtml = '<div class="col-md-6">';
  stepHtml += "<h2>" + step.name + "</h2>";
  stepHtml += "<p>" + step.diagram + "</p>";
  stepHtml += "</div>";
  stepHtml += '<div class="col-md-6">';
  stepHtml += "<p>" + step.video + "</p>";
  stepHtml += "</div>";
  $("#step").html(stepHtml);

  if (step.prev === null) {
    $("#prevButton").hide();
  } else {
    $("#prevButton").show();
  }

  if (step.next === null) {
    $("#nextButton").hide();
  } else {
    $("#nextButton").show();
  }
}

function fetchStep(stepId) {
  $.ajax({
    url: "/learn_step/" + stepId,
    type: "GET",
    success: function (response) {
      display_step(response.step);
    },
    error: function (xhr, status, error) {
      console.error("Error fetching step:", error);
    },
  });
}

$(document).ready(function () {
  display_step(s);

  $("#prevButton").click(function () {
    if (s !== null) {
      fetchStep(s.prev);
    }
  });

  $("#nextButton").click(function () {
    if (s !== null) {
      fetchStep(s.next);
    }
  });
});

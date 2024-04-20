function display_step(step) {
  var stepHtml = '<div class="row">';
  stepHtml += '<div class="col-md-4">';
  stepHtml += "<h2>" + step.name + "</h2>";
  stepHtml +=
    '<img src="' +
    step.diagram +
    '" alt="' +
    step.name +
    '" class="img-fluid"/>';
  stepHtml += "</div>";

  stepHtml += '<div class="col-md-8">';
  if (step.video) {
    stepHtml +=
      '<iframe src="' +
      step.video +
      '" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'; // Embed the video properly
  } else {
    stepHtml += "<p>No video available for this step.</p>";
  }
  stepHtml += "</div>";

  stepHtml += "</div>";

  stepHtml +=
    "<button id='prevButton' class='btn btn-primary'>Previous</button>";
  stepHtml += "<button id='nextButton' class='btn btn-primary'>Next</button>";

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

$(document).ready(function () {
  display_step(s);

  $("#prevButton").click(function () {
    if (s !== null) {
      location.href = s.prev;
    }
  });

  $("#nextButton").click(function () {
    if (s !== null) {
      location.href = s.next;
    }
  });
});

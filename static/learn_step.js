function display_step(step, totalSteps) {
  var stepHtml = "";
  var stepNumber = parseInt(step.id);
  var allChecked = false;

  // header
  stepHtml += '<div class="row text-center">';
  stepHtml += '<div class="col-md-12">';
  stepHtml +=
    "<h1>" + stepNumber + "/" + totalSteps + " " + step.name + "</h1>";
  stepHtml += "</div>";
  stepHtml += "</div>";

  // image
  stepHtml += '<div class="row">';
  stepHtml += '<div class="col-md-6">';
  stepHtml += '<div class="step-image">';
  stepHtml +=
    '<img src="' +
    step.diagram +
    '" alt="' +
    step.name +
    '" class="img-fluid">';
  stepHtml += "</div>";
  stepHtml += "</div>";

  // video
  stepHtml += '<div class="col-md-6">';
  stepHtml += '<div class="step-video">';
  if (step.video) {
    stepHtml +=
      '<iframe src="' +
      step.video +
      '" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
  } else {
    stepHtml += "<p>No video available for this step.</p>";
  }
  stepHtml += "</div>";
  stepHtml += "</div>";
  stepHtml += "</div>";

  // description
  stepHtml += '<div class="row">';
  stepHtml += '<div class="col-md-12 text-center">';
  stepHtml +=
    "<p>" + step.description + " In the diagram, characterized by:" + "</p>";
  stepHtml += "</div>";
  stepHtml += "</div>";

  // checklist
  stepHtml += '<div class="row">';
  stepHtml += '<div class="col-md-12 text-center">';
  stepHtml += "<ul class='notion-list'>";
  step.notion.forEach(function (item, index) {
    stepHtml += "<li>";
    stepHtml +=
      '<input type="checkbox" id="checkbox_' +
      index +
      '" class="notion-checkbox">';
    stepHtml += '<label for="checkbox_' + index + '">' + item + "</label>";
    stepHtml += "</li>";
  });
  stepHtml += "</ul>";
  stepHtml += "</div>";
  stepHtml += "</div>";

  // buttons
  stepHtml += '<div class="row justify-content-end">';
  stepHtml += '<div class="col-md-12 button-container">';
  stepHtml +=
    "<button id='prevButton' class='btn btn-primary'>Previous</button>";
  stepHtml += "<button id='nextButton' class='btn btn-primary'>Next</button>";
  stepHtml += "</div>";
  stepHtml += "</div>";

  // error message
  stepHtml += '<div class="row justify-content-end">';
  stepHtml += '<div class="col-md-12 text-right">';
  stepHtml += "<p id='errorMessage' class='text-danger'></p>";
  stepHtml += "</div>";
  stepHtml += "</div>";

  $("#step").html(stepHtml);

  $(".notion-checkbox").change(function () {
    allChecked = true;
    $(".notion-checkbox").each(function () {
      if (!$(this).is(":checked")) {
        allChecked = false;
      }
    });
  });

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

  $("#prevButton").click(function () {
    if (s !== null) {
      location.href = s.prev;
    }
  });

  $("#nextButton").click(function () {
    console.log(allChecked);
    if (!allChecked) {
      $("#errorMessage").text("Please check all checkboxes before proceeding.");
    } else if (s !== null) {
      $("#errorMessage").text("");
      if (s !== null && s.next !== "transition") {
        location.href = s.next;
      } else if (s !== null && s.next === "transition") {
        location.href = "/transition";
      }
    }
  });
}

$(document).ready(function () {
  display_step(s, Object.keys(ss).length);
});

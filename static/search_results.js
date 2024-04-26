function displaySearchResults(searchResults, searchText, noResults) {
  let container = document.getElementById("search-results-container");

  if (noResults) {
    container.innerHTML = '<h1>No results found for "' + searchText + '"</h1>';
  } else {
    let html =
      "<h1> Found " +
      Object.keys(searchResults).length +
      ' results for "' +
      searchText +
      '"</h1><ul>';

    for (let stepId in searchResults) {
      if (searchResults.hasOwnProperty(stepId)) {
        let step = searchResults[stepId];
        let highlightedTitle = highlightMatchingText(step.name, searchText);
        html +=
          "<li><a href='/learn_step/" +
          step.id +
          "'>" +
          highlightedTitle +
          "</a></li>";
      }
    }

    html += "</ul>";
    container.innerHTML = html;
  }

  // clear search input
  $("#search-input").val("");
  $("#search-input").focus();
}

function highlightMatchingText(text, searchText) {
  let regex = new RegExp(searchText, "gi");
  return text.replace(
    regex,
    (match) => `<span class="highlight">${match}</span>`
  );
}

$(document).ready(function () {
  displaySearchResults(sr, st, nr);
});

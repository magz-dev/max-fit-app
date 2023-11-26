 // Add an event listener to the 'change' event of the sort selector

 document.getElementById('sort-selector').addEventListener('change', function () {
    // Reference to the selector element
    const selector = this;

    // Get the current URL
    const currentURL = new URL(window.location);

    // Get the initial selected value from the selector
    const selectedValue = selector.value;

    // Check if the initially selected value is not "reset"
    if (selectedValue !== "reset") {
        // Split the initially selected value into sort and direction
        const sort = selectedValue.split("_")[0];
        const direction = selectedValue.split("_")[1];

        // Set the sort and direction parameters in the URL
        currentURL.searchParams.set("sort", sort);
        currentURL.searchParams.set("direction", direction);

        // Redirect to the updated URL
        window.location.replace(currentURL);
    } else {
        // If the initially selected value is "reset," remove sort and direction parameters from the URL
        currentURL.searchParams.delete("sort");
        currentURL.searchParams.delete("direction");

        // Redirect to the updated URL
        window.location.replace(currentURL);
    }
});
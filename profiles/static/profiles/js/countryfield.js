// Get the element with the id 'id_default_country'
let countrySelect = document.getElementById('id_default_country');

// Get the initial value of the country select
let countrySelected = countrySelect.value;

// Check if the initial value is empty and set the color accordingly
if (!countrySelected) {
    countrySelect.style.color = '#aab7c4';
}

// Add an event listener for the 'change' event on the country select
countrySelect.addEventListener('change', function () {
    // Update the countrySelected variable on change
    countrySelected = this.value;

    // Check if the new value is empty and set the color accordingly
    if (!countrySelected) {
        this.style.color = '#aab7c4';
    } else {
        this.style.color = '#000';
    }
});
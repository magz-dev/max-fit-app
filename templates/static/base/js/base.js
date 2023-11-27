 // Code from: https://www.youtube.com/watch?v=fbXHOVp_L_4
 // This script initializes a Bootstrap Toast notification once the window is fully loaded.
 // It selects an element with the class 'toast', creates a Bootstrap Toast instance, and displays the notification.

 window.onload = (event) => {
     let myAlert = document.querySelector('.toast');
     let bsAlert = new bootstrap.Toast(myAlert);
     bsAlert.show();
     // Hide the Bootstrap Toast after 5000 milliseconds
     setTimeout(() => {
         bsAlert.hide();
     }, 5000);
 }
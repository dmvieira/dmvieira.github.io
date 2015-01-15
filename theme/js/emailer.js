$(document).ready(function(){

  // Initialize Parse with your Parse application & javascript keys
  Parse.initialize("ZjSoFztJeoEjomUR7aLQzPDoBDaIxukqdMUVwmou", "FOMb0qEqFGae8GKOJtJYuIto1AMsM3YMhqBDpwT2");

  // Setup the form to watch for the submit event
  $('#contact-form').submit(function(e){
    e.preventDefault();

    // Grab the elements from the form to make up
    // an object containing name, email and message
    var data = {
      name: document.getElementById('name').value,
      email: document.getElementById('email').value,
      subject: document.getElementById('subject').value,
      message: document.getElementById('message').value
    }

    // Run our Parse Cloud Code and
    // pass our 'data' object to it
    Parse.Cloud.run("sendEmail", data, {
      success: function(object) {
        $('#response').html('Email sent!').addClass('success').fadeIn('fast');
      },

      error: function(object, error) {
        console.log(error);
        $('#response').html('Error! Email not sent!').addClass('error').fadeIn('fast');
      }
    });
  });

});

Parse.Cloud.define("sendEmail", function(request, response) {
  var sendgrid = require("sendgrid");
  sendgrid.initialize("user", "pass");
 
  var name = request.params.name;
  var email = request.params.email;
  var subject = request.params.subject;
  var message = request.params.message;
 
  sendgrid.sendEmail({
   to: "diogo.mvieira@gmail.com",
   from: email,
   fromname: name,
   subject: subject,
   text: "Name: "+name+"\nEmail: "+email+"\nMessage:\n\n"+message
   }, {
     success: function(httpResponse) {
       console.log(httpResponse);
       response.success("Email sent!");
    },
     error: function(httpResponse) {
       console.error(httpResponse);
       response.error("Uh oh, something went wrong");
    }
  });
});

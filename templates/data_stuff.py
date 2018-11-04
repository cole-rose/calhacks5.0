<html>
<head>
    <title>{% block title %}{% endblock %}Upload</title>

<style>
    	header {
    		font-size: 20px;
    		text-align: center;
    	}
    </style>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script>
    $(document).ready(function() {

    $("#myform").submit(function() { // intercepts the submit event
    console.log("fsd");
    return;
      $.ajax({ // make an AJAX request
        type: "POST",
        url: "/",
        data: $("#myform").serialize(), // serializes the form's elements
        success: function(data)
        {
          document.getElementById("dataOut").innerHTML = data;
        }
      });
      e.preventDefault(); // avoid to execute the actual submit of the form
    });

  });
</script>
</head>

<header>
    Machine Learning Cancerous Tumor Detection </header>
<body>
<form id="myform" method=POST enctype=multipart/form-data action="{{ url_for('upload') }}">
    <input type=file name=photo>
    <input type="submit">


    <img photo>

</form>
<div id="dataOut"></div>
</body>
</html>
<!DOCTYPE html>
<html>

<head>
<title>Bus Arrival Prediction</title>
<link rel="stylesheet" href="/static/style.css">
</head>

<body>

<header>Bus Arrival Time Prediction</header>

<div class="card">

<h2>Enter Bus Travel Details</h2>

<form action="/predict" method="post">

<label>Distance (km)</label><br>
<input type="number" name="distance" placeholder="Enter distance in km" required><br>

<label>Traffic Level</label><br>
<select name="traffic">
<option value="1">Low</option>
<option value="2">Medium</option>
<option value="3">High</option>
</select><br>

<label>Bus Speed (km/h)</label><br>
<input type="number" name="speed" placeholder="Enter bus speed" required><br>

<br>

<button type="submit">Predict Arrival Time</button>

</form>

</div>

</body>

</html>
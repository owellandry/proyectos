var count = 0;
var button = document.getElementById("button");
var countDisplay = document.getElementById("count");

button.addEventListener("click", function() {
	count++;
	countDisplay.innerHTML = count;
});

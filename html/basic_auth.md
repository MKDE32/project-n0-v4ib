```
<!DOCTYPE html>
<html>
<head>
<title>Geschützte Seite</title>
</head>

<body>

<form>
  Passwort: <input type="password" id="pw"><br>
  <input type="button" onclick="checkPassword()" value="Einloggen">
</form>

<script>
function checkPassword() {
  var password = document.getElementById("pw").value;
  if (password == "correctpassword") {
    window.open("protectedpage.html", "_self");
  } else {
    alert("Falsches Passwort!");
  }
}
</script>

</body>
</html>
```

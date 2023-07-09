<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My GitHub Page</title>
  <style>
    /* Add your custom CSS styles here */

    body {
      background-color: #222;
      color: #fff;
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }

    .container {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      text-align: center;
    }

    h1 {
      font-size: 3rem;
      text-shadow: 2px 2px 4px #000;
    }

    .button {
      display: inline-block;
      padding: 10px 20px;
      background-color: #555;
      color: #fff;
      text-decoration: none;
      border-radius: 4px;
      margin: 10px;
      transition: background-color 0.3s ease;
    }

    .button:hover {
      background-color: #777;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Welcome to My GitHub Page</h1>
    <button class="button" onclick="openURL('https://www.example.com')">Button 1</button>
    <button class="button" onclick="openURL('https://www.example.com')">Button 2</button>
  </div>

  <script>
    function openURL(url) {
      window.open(url);
    }
  </script>
</body>
</html>

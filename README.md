# Flask Website

## Shortcuts

- Starting the Flask website now for Hack Only.
- Ctrl+B - Close Bar
- Ctrl+PgUp/PgDown - Switch between docs
- Ctrl+Shift+PgUp/PgDown - Change doc place
- Alt+UpArrow/DownArrow - Move line
- Shift+Alt+UpArrow/DownArrow - Dublicate line
- Ctrl+Shift+{} - Collapse selection
- Ctrl+L - Select line
- Alt+Click - Multiple cursors
- Ctrl+Tab - Switch between opened files

## Routes

```python

-@app.route("/<a>")
-@app.route("/<string:a>")
-@app.route("/<int:a>")
-@app.route("/<float:a>")
-@app.route("/<path:a>")
-@app.route("/combineroute/<string:a>/<int:b>")

```

## Notes

```html

<link rel="icon" href="{{ url_for("static", filename="imgs/OBlogoIcon.ico") }}">
<link rel="icon" type="image/png" href="{{ url_for('static', filename='imgs/download.png')}}" sizes="480x480">
<meta http-equiv="Refresh" content="5; url=https://www.quackit.com/html/tags/">
<body style="background-image: url('/static/imgs/computer_light_neon_surface_50557_1600x900.jpg')">

```

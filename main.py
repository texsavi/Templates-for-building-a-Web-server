from flask import Flask, redirect

# Initialize Flask app and specify the location of static files
app = Flask(__name__, static_url_path="/static")

# Define the route for the home page
@app.route('/')
def index():
  # Return an empty string for now
  return ""

# Define the route for the "/plane" page
@app.route('/plane')
def entry0():
  # Set the heading, date, link, and text for the page
  heading = "Planes...Just planes flying fast"
  date = "23"
  link = "https://Templates-for-building-a-Web-server"
  text = "Before the take off, we ensure we have enough rest. The taxi is always first in the way. Time is essential whether you like it or not. You'd rather be calm. Yes, keep calm and come in on board our flight of the day."
  
  # Read the template HTML file and replace the placeholders with the appropriate values
  with open("template/blog.html", "r") as f:
    page = f.read()
  page = page.replace("{heading}", heading)
  page = page.replace("{date}", date)
  page = page.replace("{link}", link)
  page = page.replace("{text}", text)
  
  # Return the fully rendered HTML page
  return page

# Define the route for the "/taxii" page
@app.route('/taxii')
def entry():
  # Set the heading, date, link, and text for the page
  heading = "Taxiing"
  date = "22"
  link = "https://Templates-for-building-a-Web-server"
  text = "The Flight deck is all set for the run. It's gonna be long-haul enroute ONT, CAN. They named it the ice nation. Wonder what Iceman has to do with this top gun of a country."
  
  # Read the template HTML file and replace the placeholders with the appropriate values
  with open("template/blog.html", "r") as f:
    page = f.read()
  page = page.replace("{heading}", heading)
  page = page.replace("{date}", date)
  page = page.replace("{link}", link)
  page = page.replace("{text}", text)

  # Return the fully rendered HTML page
  return page

# Define the route for the "/plane" page, which redirects to an external URL
@app.route("/blog/mine")
def home():
  return redirect('/plane')

# Define the route for the "/taxii" page, which redirects to itself
@app.route('/blog/mine1')
def taxi():
  return redirect('/taxii')

# Run the app on port 81 and listen for incoming requests
app.run(host='0.0.0.0',port=81)
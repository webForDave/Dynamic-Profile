Dynamic Profile
These bunch of files are collectively organized by me :) to create a REST api. Do not be overwhelmed by how much folders and files it's got, Django contribunted a chunk to it (Thank you Django, I guess 🙂)

So, the rest api exposes just one endpoint:

/me

And sadly, the api responds only to GET requests, so to the technical people, when you make a request with not this method/verb, you'd surely get an error 🙂. When a GET request is made, the server responds with json, instead of regular text/html people are familiar with, there are many use cases of an API, but one of it is to serve as a bridge between systems.

The json returned contains my information (well, just a bit of my information), including my name, email address, and the stack I used to build the api. It also contains the current time and date dynamically and a radom cat fact fetched from an external API.

A typical response looks like this:

{
    "status": "success",
    "user": {
        "name": "Akinola David",
        "email": "dakinola54@gmail.com,
        "stack": "Python/Django"
    },
    "timestamp": "2025-10-16T08:33:29.769023Z",
    "fact": "A cat has the ability to rotate their ears 180 degrees,with the help of 32 muscles that they use to control them."
}
Notes
I learned a new way to use serializers. Initially, when I create a serializer class, I just go ahead and use data in the serializer call, eg:

serilizer = MySeralizer(data=...)

Building this api without a database taught me that I could use the intance keyword

Data: used for incoming information to be parsed into prgrammable objects
Instance: used for outgoing data to be parsed into programmable objects
Installation and usage Guide
To use this project locally, you need to have python installed, you can check the iternet on how to do that, it's really simple.

You should have a virtual environment running. A virtual environment is like a container for the project, it helps to isolate the project's dependencies from other python projects with different dependencies. You can also check how to do that. My favorte is venv ;)

Next, this project comes with a few dependencies so you need to install them before proceeding. A list of the dependencies is found in the requireents.txt file, you just need to run python -m pip install -r requirement.txt. This installs the dependencies required to run this project

Since you already have you virtual environment running, the next logical step is to have fun by running the project yourself. To do this, simply run python manage.py runserver this spins up the local server at a default port (8000), sure, you can change that. mange.py is a utility file that comes with Django which takes care of basically almost everything from creating users to getting the server up and running and numerous intersting stuff.
# ToDo List Library

## Context

This library is intended to complete a takehome assignment for Teachable.

The premise is that there is an existing REST web service that we are going to hit using various methods.

## About the project

This project uses Python with a few key libraries:

1. Click -- for CLI setup (as seen in `cli.py`)

2. Requests -- for easier REST calls (as seen in `interface.py`)

3. Flask -- for creating a test backend server (as seen in `fake_list_service.py`)

## Installation

1. Clone this library: `git clone  {this_library_url}`

2. Navigate to the library: `cd {clone_location}`

3. Install dependencies: `pipenv install`



At this point you have a few options.

1. If you have a url and credentials for an existing API you can fill them in `interface.py` within the `RequestMaker` class details. (You can just search for TODO and this will show up)

2. If you do not have credentials you can run `make mock-server` and this will allow you to run the test suite using `pytest`.



## Running commands

The easiest way to see a few things run is by running `$ python runner.py`



To run commands individually, you can run `$ python cli.py` which will produce a help menu that can guide you through the available commands.



## Further Reading

I have documented my notes and some ideas within [docs/notes.md](docs/notes.md)



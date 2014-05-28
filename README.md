## About the project
This project is for an EverQuest guild on the Bertoxxulous server.  It's goals are:

- Roster
- News Page
- DKP System
- Integration with phpbb3
- API for use with our desktop app to assist in handling DKP

## Progress
I'm using this as a tool to learn Django programming and generally flex my mental muscles when I'm not working and being a sysadmin.  So, progress may be slow, or non-existant

## Contributing
I welcome any contributions folks want to bring to the table.  I would love to make this generic and configurable so any guild could use it, and use our DKP system as wanted.  While there is already a great EQDKP project, it doesn't have the interface and rules flexibility we wanted.  Please fork and send me a pull request with your code.  I ask that you make sure all unit tests pass, and that you don't skimp on writing your own tests as needed.

## Requirements
I develop on a Mac, but this stuff should all work on any linux that supports python3 and has pip.

- Python 3
- pip
- Django

## Installing Dev Environment
I wrote a nice script to set things up for you.  Just invoke it:

```
./setup.sh
```

## Using the Dev Environment
Again, I wrote a nice fun script.  Make sure you have tmux installed, then invoke it:

```
./dev.sh
```

## Running in Prod
Deploy behind any typical nginx/wsgi or apache/mod_wsgi setup.  The dev environment uses the built in django server.
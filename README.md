
# Layer API

## Prerequisites

[VirtualBox](https://www.virtualbox.org/) and [Vagrant](http://www.vagrantup.com/) (minimum version 1.6)
Other providers, like VMWare may work, not tested!



## Up and SSH

To start the vagrant box run:

    vagrant up

To log in to the machine run:

    vagrant ssh

## Install & run

$ sh install.sh


## Run (edit databases settings in settings.py and import db before first launch )

$ sh run.sh
## API Endpoints



| ENDPOINT    		   | Method		     | Description    	     | Parameters			 				  							 |
| ---------------------|-----------------|-----------------------| ------------------------------------------------------------------|
| /register   		   | POST(body)	     |Create user		     | username,password,firstname,lastname,birthday,email,phone_number  |
| /login/access_token  | POST(urlencoded)|Generate access token  | client_id,username,password,grant_type(password)	 				 |
| /update  			   | PUT			 |Update user profile	 | profile_id,password,firstname,lastname,birthday,email,phone_number|
|					   |				 |	             		 |										                             |




# Layer API


## Install (Debian)

$ sh install.sh
$ sh run.sh ()

## Install (Other OS)

Required dependencies:
	- mysql
	- python pip
	- python 2.7

pip install -r requirements.txt


## Run (edit databases settings in settings.py before first launch)

## API Endpoints



| ENDPOINT    		   | Method		     | Description    	     | Parameters			 				  							 |
| ---------------------|-----------------|-----------------------| ------------------------------------------------------------------|
| /register   		   | POST(body)	     |Create user		     | username,password,firstname,lastname,birthday,email,phone_number  |
| /login/access_token  | POST(urlencoded)|Generate access token  | client_id,username,password,grant_type(password)	 				 |
| /update  			   | PUT			 |Update user profile	 | profile_id,password,firstname,lastname,birthday,email,phone_number|
|					   |				 |	             		 |										                             |



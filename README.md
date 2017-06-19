
# Layer API

| ENDPOINT    		   | Method		| Description    	     | Parameters			 				  							 |
| ---------------------|------------|------------------------| ------------------------------------------------------------------|
| /register   		   | 	POST	|Create user		     | username,password,firstname,lastname,birthday,email,phone_number  |
| /login/access_token  | 	POST	|Generate access token   | client_id,username,password,grant_type(password)	 			     |
| /update  			   | 	PUT		|Update user profile	 | profile_id,password,firstname,lastname,birthday,email,phone_number|
|					   |			|	             		 |										                             |

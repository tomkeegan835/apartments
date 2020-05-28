sftp -i "../../api-server.pem" ubuntu@ec2-52-27-61-84.us-west-2.compute.amazonaws.com <<EOF
put api.py
put craigslist.py

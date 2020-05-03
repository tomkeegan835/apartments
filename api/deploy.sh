sftp -i "../../../docker-server.pem" ubuntu@ec2-54-188-29-69.us-west-2.compute.amazonaws.com <<EOF
put api.py

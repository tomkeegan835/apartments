sftp -i "../../api-server.pem" ubuntu@ec2-52-27-61-84.us-west-2.compute.amazonaws.com <<EOF
put api.py
put craigslist.py
put crawl.py
put requirements.txt
put run.sh
put sql.py
put util.py
rm listings.db

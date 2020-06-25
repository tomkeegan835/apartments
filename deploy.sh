zip package.zip api.py craigslist.py crawler.py requirements.txt sql.py util.py crawl.py
sftp -i ../../api-server.pem ubuntu@ec2-52-27-61-84.us-west-2.compute.amazonaws.com <<EOF
put package.zip

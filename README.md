# OpenEBSAss1

## Steps to Run the app

1. Clone the repo with  
	```git clone https://github.com/prratadiya/OpenEBSAss1.git```  

2. Then goto that directory using  
	```cd OpenEBSAss1```  

3. Run all the yaml files through this command.(Make sure you have pip installed in the system if not then install it with this command ```sudo apt-get install python-pip```)  
	After this run these commands.

	```kubectl apply -f pods.yaml```  
	```kubectl apply -f deployments.yaml```  
	```kubectl apply -f services.yaml```

4. Now run the docker through this command  
	```docker run -e username="YOUR_USERNAME" -p 127.0.0.1:80:80 pratik1998/hellous:firsthello```

5. Now Open the browser on the link provided after running the command in step 4.

Note: If in case you have nginx installed and its page shows up instead of the app, set the port as `40:80` and open the browser at ```0.0.0.0:40```

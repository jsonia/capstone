Last login: Mon Nov 28 23:00:05 on ttys000
(base) soniajaiswal@Sonias-Air ~ % scp soniajaiswal@lion.cs.ucla.edu:/u/class/cs31/5pickup/2C.zip proj5
soniajaiswal@lion.cs.ucla.edu's password: 
2C.zip                                                                                                        100%  410KB   1.9MB/s   00:00    
(base) soniajaiswal@Sonias-Air ~ % ls
Applications			Library				Pictures			miniforge3
Desktop				Miniforge3-Linux-x86_64.sh	Postman				opt
Documents			Movies				Public				proj5
Downloads			Music				Untitled.ipynb			tensorflow_macos_venv
IdeaProjects			Parallels			VID_1_23.mp4			tmp_data
(base) soniajaiswal@Sonias-Air ~ % cd Documents 
(base) soniajaiswal@Sonias-Air Documents % ls
1_hw4_jaiswal_sonia_805525305.pdf			Screen Shot 2022-10-10 at 11.01.59 PM.png
905744996.pages						Screen Shot 2022-10-10 at 12.52.26 PM.png
Amazon							Screen Shot 2022-10-11 at 10.39.21 PM.png
Appointment Booked - OpenCommunicator.pdf		Screen Shot 2022-10-11 at 10.50.07 PM.png
Batch-Normalization_hw4.pdf				Screen Shot 2022-10-25 at 11.24.21 AM.png
Breadth-Requirement-2019-.pdf				Sonia_Jaiswal_CV.pdf
CS130Partc						Transcript1.pdf
Dropout_hw4.pdf						Transcript2.pdf
Dropout_latest_hw4.pdf					UCLA Important docs
Fidelity						Untitled.pages
Final_recording.mov					VID_1_16.mp4
Full Set Hiring Documents (Remote).pdf			Zoom
HW4_Optimization - Jupyter Notebook.pdf			[7]Teammate_Evaluation.pages
IIT-KGP 						cover.txt
Immigration						fc_net_hw3.pdf
JAM							hello.sh
MS_Proposed_Program_of_Study-9_23_15.pdf		hw1_jaiswal_sonia_805525305.ipynb - Colaboratory.pdf
Masters							hw3_jaiswal_sonia_805525305 .pdf
Movie on 5-23-22 at 12.59 PM.mov			hw3_jaiswal_sonia_805525305.ipynb
Optimization_hw3.pdf					hw4_Batch-Normalization - Jupyter Notebook.pdf
SSN							hw4_Dropout _Jupyter Notebook.pdf
School							hw4_fc_net_py.pdf
Screen Recording 2022-05-25 at 2.18.17 PM.mov		hw4_jaiswal_sonia_805525305.pdf
Screen Recording 2022-05-25 at 2.21.47 PM.mov		hw4_layer_py.pdf
Screen Recording 2022-05-25 at 2.34.48 PM.mov		hw4_optim_py.pdf
Screen Recording 2022-05-25 at 2.37.46 PM.mov		layer_hw3.pdf
Screen Shot 2022-05-01 at 12.41.19 PM.png		maatc.pdf
Screen Shot 2022-06-02 at 11.47.04 AM.png		optim_hw3.pdf
Screen Shot 2022-06-10 at 6.14.21 PM.png		rr_test.c
Screen Shot 2022-10-06 at 4.21.05 PM.png		rr_test.h
Screen Shot 2022-10-06 at 4.21.56 PM.png		ss-5.pdf
Screen Shot 2022-10-06 at 4.23.20 PM.png		vid1.mp4
(base) soniajaiswal@Sonias-Air Documents % cd Masters 
(base) soniajaiswal@Sonias-Air Masters % cd Quarter
cd: no such file or directory: Quarter
(base) soniajaiswal@Sonias-Air Masters % cd Quarter4
(base) soniajaiswal@Sonias-Air Quarter4 % ls
Amazon	EAD	Job	TA
(base) soniajaiswal@Sonias-Air Quarter4 % cd TA
(base) soniajaiswal@Sonias-Air TA % ls
2C					proj2					proj4
2C.zip					proj2_return				proj4_return
Sonia Jaiswal.pdf			proj3					proj5
SoniaJaiswal-SignedOfferLetter.pdf	proj3_return
(base) soniajaiswal@Sonias-Air TA % scp soniajaiswal@lion.cs.ucla.edu:/u/class/cs31/5pickup/2C.zip proj5
soniajaiswal@lion.cs.ucla.edu's password: 
2C.zip                                                                                                        100%  410KB   3.2MB/s   00:00    
(base) soniajaiswal@Sonias-Air TA % ssh sonia@wing2.cs.ucla.edu                                         
Last login: Tue Nov 29 21:38:42 2022 from 76.94.208.56
sonia@wing2:~$ sudo su
[sudo] password for sonia: 
root@wing2:/home/sonia# 
root@wing2:/home/sonia# 
root@wing2:/home/sonia# 
root@wing2:/home/sonia# vim webh2.py


@app.route('/join-accept', methods=['POST'])
def webhook3():
    print("hello")
    app.logger.info('Info level log')
    if(request.method == 'POST'):
        print(request.json)
   #     app.logger.error("BODY: %s" % request.get_data())
   #      url = 'https://lorala.nam1.cloud.thethings.industries/api/v3/as/applications/my-application/webhooks/test-webhook/devices/my-device/down/push'
   #      headers = {'Authorization': "Bearer NNSXS.QYNVIPCESUULZ73YK2CGM2KRBGSTIGVJXCZMRSY.CVA4L4P47W7PPYUTACCDOTR5DGKN3QGJMN2HFJ6AYNOPILY7KI4A",
   #    'Content-Type': "application/json",
  #     'User-Agent': "my-integration/my-integration-version"}
 #       data = {"downlinks":[{
  #    "frm_payload":"vu8=",
 #     "f_port":2,
#      "priority":"NORMAL"
#    }]
#  }
#        res = requests.post(url, json=data, headers=headers)
#        print (res.status_code)
#        print (res.raise_for_status())
    return 'success', 200

@app.route('/uplinks', methods=['POST'])
def webhook1():
    app.logger.info('Info level log')
    if(request.method == 'POST'):
        print(request.json)
        url = 'https://lorala.nam1.cloud.thethings.industries/api/v3/as/applications/my-application/webhooks/test-webhook/devices/my-device/down/push'
        headers = {'Authorization': "Bearer NNSXS.QYNVIPCESUULZ73YK2CGM2KRBGSTIGVJXCZMRSY.CVA4L4P47W7PPYUTACCDOTR5DGKN3QGJMN2HFJ6AYNOPILY7KI4A",
       'Content-Type': "application/json",
       'User-Agent': "my-integration/my-integration-version"}
        data = {"downlinks":[{
      "frm_payload":"vu8=",
      "confirmed":True,
      "f_port":2,
      "priority":"NORMAL"
    }]
  }
                                                                                                                              21,15         48%
